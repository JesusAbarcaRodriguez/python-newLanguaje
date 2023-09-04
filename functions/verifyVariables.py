def verify_variables(lines):
    valid_data_types = {"ENTERO", "BOOLEANO", "CADENA", "CARÁCTER", "FLOTANTE", "NULO"}

    declared_variables = {}

    error_message = ""

    for line in lines:
        line = line.strip()

        if not line or line.startswith("$"):
            continue

        words = line.split()

        if len(words) < 3:
            error_message += f"Error: Sintaxis incorrecta en la declaración de variables: {line}\n"
            continue

        data_type = words[0]
        variable_name = words[1]

        if data_type not in valid_data_types:
            error_message += f"Error: Tipo de dato no válido en la declaración de variables: {line}\n"
            continue

        if variable_name in declared_variables:
            error_message += f"Error: La variable '{variable_name}' ya ha sido declarada.\n"
            continue

        declared_variables[variable_name] = data_type

    if not error_message:
        return "Compilación exitosa"
    else:
        return error_message