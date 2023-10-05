from functions.utils.utils import is_called_fuction_procedure, is_declared_variable, is_same_type
def semantic_analysis_assigments(principal,variables,i,tokens):
    if is_declared_variable(tokens,i,variables):
        variable_to_assign = variables[tokens[i][1]]
        variable_name = tokens[i][1]
        i += 2
        while tokens[i][0] != 'FIN_DE_INSTRUCCION':
            if is_called_fuction_procedure(tokens,i):
                function_name= tokens[i][1]
                keys_functions = principal.functions.keys()
                if function_name in keys_functions:
                    if not principal.functions[function_name].data_type == variable_to_assign[0]:
                        return f"Error la asignación es de tipos diferentes, la variable '{variable_name}' no es de tipo {principal.functions[function_name].data_type}"
                else:
                    return f"Error la asignación es de tipos diferentes, la variable '{variable_name}' no es de tipo {tokens[i][0]}"
            elif tokens[i][0] == 'IDENTIFICADOR':
                if not (tokens[i][1] in variables  and (is_same_type(variable_to_assign,tokens,i,variables) or variable_to_assign[0] == 'FLOTANTE' and  variables[tokens[i][1]][0] == 'ENTERO')):
                    return f"Error semantico en {tokens[i][1]}"
            elif tokens[i][0] == 'NUMERO_ENTERO':
                if not (variable_to_assign[0] == 'ENTERO' or variable_to_assign[0] == 'FLOTANTE'):
                    return f"Error la asignación es de tipos diferentes, la variable '{variable_name}' no es de tipo {tokens[i][0]}"
                i += 1
            elif tokens[i][0] == 'NUMERO_FLOTANTE':
                if not (variable_to_assign[0] == 'FLOTANTE' ):
                    return f"Error la asignación es de tipos diferentes, la variable '{variable_name}' no es de tipo {tokens[i][0]}"
                i += 1
            elif tokens[i][0] == 'VALOR_BOOLEANO':
                if not (variable_to_assign[0] == 'BOOLEANO'):
                    return f"Error la asignación es de tipos diferentes, la variable '{variable_name}' no es de tipo {tokens[i][0]}"
                i += 1
            elif tokens[i][0] == "OPERADOR_ARITMETICO":
                i += 1
            elif tokens[i][0] == "VALOR_CARACTER":
                if not variable_to_assign[0] == 'CARACTER':
                    return f"Error la asignación es de tipos diferentes, la variable '{variable_name}' no es de tipo {tokens[i][0]}"
                i +=1
            elif tokens[i][0] == "CADENA_LITERAL":
                if not variable_to_assign[0] == 'CADENA':
                    return f"Error la asignación es de tipos diferentes, la variable '{variable_name}' no es de tipo {tokens[i][0]}"
                i +=1
            else:
                return f"Error semantico en {tokens[i][1]} no es una asignacion valida"
    else:
        return f"{tokens[i][1]} no ha sido declarada "
    return str(i+1)