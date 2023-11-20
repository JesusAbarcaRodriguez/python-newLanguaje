from functions.semantic_analysis.semantic_call_function_procedure import semantic_call_function_procedure
from functions.utils.utils import  error_message, is_array_call,is_called_fuction_procedure, is_declared_variable, is_read, is_same_type
def semantic_analysis_assigments(principal,variables,i,tokens):
    if is_declared_variable(tokens,i,variables):
        variable_to_assign = variables[tokens[i][1]]
        variable_name = tokens[i][1]
        parameters_input = []
        i += 2
        while tokens[i][0] != 'FIN_DE_INSTRUCCION':
            if is_called_fuction_procedure(tokens,i):
                function_name= tokens[i][1]
                keys_functions = principal.functions.keys()
                if function_name in keys_functions:
                    if principal.functions[function_name].data_type == variable_to_assign[0]:
                        i += 2
                        while tokens[i][0] != 'PARENTESIS_DER':
                            if tokens[i][0] == 'IDENTIFICADOR':
                                if is_declared_variable(tokens,i,principal.variables):
                                    parameters_input.append(principal.variables.get(tokens[i][1]))
                                i += 1
                            else:
                                parameters_input.append(tokens[i])
                                i += 1
                        if  len(parameters_input):
                            message = semantic_call_function_procedure(principal,function_name,parameters_input)
                            if not message == "OK":
                                return message
                        i+=1
                    else:
                        return f"Error la asignación es de tipos diferentes, la variable '{variable_name}' no es de tipo {principal.functions[function_name].data_type}"
                else:
                    return f"Error la asignación es de tipos diferentes, la variable '{variable_name}' no es de tipo {tokens[i][0]}"
            elif is_array_call(tokens,i):
                i+=2
            elif tokens[i][0] == 'IDENTIFICADOR':
                if not (tokens[i][1] in variables  and (is_same_type(variable_to_assign,tokens,i,variables) or variable_to_assign[0] == 'FLOTANTE' and  variables[tokens[i][1]][0] == 'ENTERO')):
                    return f"Error semantico en {error_message(tokens, i )}"
                i += 1
            elif is_read(tokens,i):
                i += 1
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
                return f"Error semantico en {error_message(tokens, i )} no es una asignacion valida"
    else:
        return f"{error_message(tokens, i )} no ha sido declarada "
    return str(i+1)