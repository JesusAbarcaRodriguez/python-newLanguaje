class DataTypeError:
    def __init__(self, isError, message):
        self.isError = isError
        self.message = message
def data_types_analysis(lines):
    data_type_error = DataTypeError(False, "")
    valid_asign_data = valid_data_types + {"ASIGNACIÓN"} + ";"
    valid_data_types = {"ENTERO", "BOOLEANO", "CADENA", "CARÁCTER", "FLOTANTE"}
    declared_variables = {}

    for line in lines:
        line = line.strip()

        if not line or line.startswith("$"):
            continue

        words = line.split()

        if len(words) < 3:
            data_type_error.isError = True
            data_type_error.message += f"Error: Sintaxis incorrecta en la declaración de variables: {line}\n"
            continue

        data_type = words[0]
        variable_name = words[1]

        if data_type not in valid_data_types:
            data_type_error.isError = True
            data_type_error.message += f"Error: Tipo de dato no válido en la declaración de variables: {line}\n"
            continue

        if variable_name in declared_variables:
            data_type_error.isError = True
            data_type_error.message += f"Error: La variable '{variable_name}' ya ha sido declarada.\n"
            continue

        declared_variables[variable_name] = data_type

    if not data_type_error.isError:
        data_type_error.message = "Compilación exitosa"
        return data_type_error
    else:
        return data_type_error