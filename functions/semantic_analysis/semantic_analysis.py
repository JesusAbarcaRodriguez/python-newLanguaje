import re

from functions.utils.utils import is_matrix_declaration
def semantic_analysis(tokens,principal):
    from functions.utils.utils import is_procedure_decalaration
    from functions.semantic_analysis.semantic_analysis_PRINCIPAL import semantic_analysis_PRINCIPAL
    from functions.semantic_analysis.semantic_analysis_FUNCION import semantic_analysis_FUNCION
    
    from functions.semantic_analysis.semantic_analysis_PROCEDIMIENTO import semantic_analysis_PROCEDIMENTO
    from functions.utils.utils import  error_message, is_array_declaration,is_main_procedure, is_function_declaration, is_variable_declaration

    i = 0
    while i < len(tokens):
        if is_variable_declaration(tokens,i):
            if principal.variables.get(tokens[i+1][1]) == None:
                principal.variables[tokens[i+1][1]] = [tokens[i][1],None]
                i += 3
            else:
                return f"Error semantico la variable {tokens[i+1][1]} ya esta declarada"
        elif is_array_declaration(tokens,i):
            size = re.search(r'\[(.*?)\]', tokens[i][1]).group(1)
            data_type_match = re.search(r'(ENTERO|BOOLEANO|FLOTANTE|CADENA|CARACTER)', tokens[i][1])
            if data_type_match:
                data_type = data_type_match.group(1)
            else:
                return f"Error semantico en {error_message(tokens, i )} no es un tipo de dato valido"
            if principal.arrays.get(tokens[i+1][1]) == None:
                principal.arrays[tokens[i+1][1]] = [data_type,{},size]
                i += 3
            else:
                return f"Error semantico el vector {tokens[i+1][1]} ya esta declarado"
        elif is_matrix_declaration(tokens,i):
            rows_match = re.search(r'\[(\d+)\]', tokens[i][1])
            columns_match = re.search(r'\[(\d+)\]\[(\d+)\]', tokens[i][1])
            if rows_match and columns_match:
                rows = int(rows_match.group(1))
                columns = int(columns_match.group(2))
            else:
                return f"Error semántico en {error_message(tokens, i )}. No se pudieron extraer los índices de filas y columnas correctamente."
            data_type_match = re.search(r'(ENTERO|BOOLEANO|FLOTANTE|CADENA|CARACTER)', tokens[i][1])
            if data_type_match:
                data_type = data_type_match.group(1)
            else:
                return f"Error semantico en {error_message(tokens, i )} no es un tipo de dato valido"
            if principal.matrix.get(tokens[i+1][1]) == None:
                principal.matrix[tokens[i+1][1]] = [data_type,[],rows,columns]
                i += 3
            else:
                return f"Error semantico la matriz {tokens[i+1][1]} ya esta declarada"
        elif is_function_declaration(tokens,i):
            message = semantic_analysis_FUNCION(principal,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
        elif is_procedure_decalaration(tokens,i):
            message = semantic_analysis_PROCEDIMENTO(principal,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
        elif is_main_procedure(tokens,i):
            principal.init_principal = i
            message = semantic_analysis_PRINCIPAL(principal,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
        else:
            return f"Error semantico en {error_message(tokens, i )} no es una declaracion valida"
    return "Analisis semantico exitoso"




