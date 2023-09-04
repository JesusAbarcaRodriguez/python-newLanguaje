# Función para verificar la sintaxis del código
def verify_syntax(code):
    # Dividir el código en líneas
    lines = code.split('\n')
    
    # Inicializar variables de contexto
    data_types = {"ENTERO", "BOOLEANO", "CADENA", "CARÁCTER", "FLOTANTE", "NULO"}
    variables = {}
    in_function = False
    in_for_loop = False
    in_while_loop = False
    output = ""
    
    for line in lines:
        line = line.strip()
        
        # Ignorar líneas vacías o comentarios
        if not line or line.startswith("$"):
            continue
        
        # Verificar declaración de variables
        if any(line.startswith(data_type) for data_type in data_types):
            parts = line.split()
            if len(parts) >= 3:
                data_type = parts[0]
                variable_name = parts[1]
                if variable_name not in variables:
                    variables[variable_name] = data_type
                else:
                    output += f"Error: La variable '{variable_name}' ya ha sido declarada.\n"
            else:
                output += f"Error: Sintaxis incorrecta en la declaración de variables: {line}\n"
        
        # Verificar declaración de funciones
        elif line.startswith("ENTERO FUNCION"):
            parts = line.split()
            if len(parts) == 4 and parts[3] == "EMPIEZA":
                function_name = parts[2]
                in_function = True
                output += f"Declaración de función: {function_name}\n"
            else:
                output += f"Error: Sintaxis incorrecta en la declaración de función: {line}\n"
        
        # Verificar fin de función
        elif line == "FIN":
            if in_function:
                in_function = False
                output += "Fin de función\n"
            else:
                output += "Error: 'FIN' fuera de una función\n"
        
        # Agregar más validaciones para bucles, condicionales, etc. aquí
        
        else:
            output += f"Error: Sintaxis desconocida: {line}\n"
    
    # Verificar variables no utilizadas
    for variable_name in variables:
        if in_function and variable_name not in code:
            output += f"Advertencia: Variable '{variable_name}' no utilizada en la función.\n"
    
    return output

# Ejemplo de uso:
code = """
ENTERO a = 0;
BOOLEANO bandera = falso;
CADENA frase= "Hola mundo";
ENTERO FUNCION PRINCIPAL()
EMPIEZA
a = a + 1;
FIN
"""
result = verify_syntax(code)
print(result)
