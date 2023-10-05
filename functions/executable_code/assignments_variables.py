def verify_assigments(principal,variables,i,tokens):
    from functions.executable_code.verify_FUNCION import verify_FUNCION
    from functions.semantic_analysis.semantic_call_function_procedure import semantic_call_function_procedure
    from functions.utils.utils import is_called_fuction_procedure, is_declared_variable, is_same_type
    if is_declared_variable(tokens,i,variables):
        variable_to_assign = variables[tokens[i][1]]
        index_variable_to_assign = i
        total_to_assign = []
        total_operators = []
        parameters_input = []
        is_int_assignments = False
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
                        init_function = principal.functions[function_name].init_function
                        verify_FUNCION(principal,init_function,tokens,function_name)
                        variables[tokens[index_variable_to_assign][1]][1] = principal.functions[function_name].return_data
                        i += 1
                    else:
                        return f"Error: La variable: '{variable_to_assign[1]}' no es del mismo tipo que la funcion {function_name} "
            if tokens[i][0] == 'IDENTIFICADOR':
                if tokens[i][1] in variables and not variables[tokens[i][1]][1] == None  and (is_same_type(variable_to_assign,tokens,i,variables) or variable_to_assign[0] == 'FLOTANTE' and  variables[tokens[i][1]][0] == 'ENTERO'):
                    if variable_to_assign[0] == 'ENTERO' or variable_to_assign[0] == 'FLOTANTE':
                        total_to_assign.append(variables[tokens[i][1]][1])
                        is_int_assignments = True
                    else:
                        variable_to_assign[1] = tokens[i][1]
                    i += 1
                else:
                    return f"Error semantico en {tokens[i][1]}"
            elif tokens[i][0] == 'NUMERO_ENTERO':
                if variable_to_assign[0] == 'ENTERO' or variable_to_assign[0] == 'FLOTANTE':
                    total_to_assign.append(int(tokens[i][1]))
                    is_int_assignments = True
                    i += 1
            elif tokens[i][0] == 'NUMERO_FLOTANTE':
                if variable_to_assign[0] == 'FLOTANTE' :
                    total_to_assign[0].append(int(tokens[i][1]))
                    is_int_assignments = True
                    i += 1
            elif tokens[i][0] == 'VALOR_BOOLEANO':
                if variable_to_assign[0] == 'BOOLEANO':
                    variables[tokens[index_variable_to_assign][1]][1] = tokens[i][1]
            elif tokens[i][0] == "OPERADOR_ARITMETICO":
                total_operators.append(tokens[i][1])
                i += 1
            elif tokens[i][0] == "CARACTER":
                if variable_to_assign[0] == 'CARACTER':
                    variables[tokens[index_variable_to_assign][1]][1] = tokens[i][1]
            elif tokens[i][0] == "CADENA_LITERAL":
                if variable_to_assign[0] == 'CADENA':
                    variables[tokens[index_variable_to_assign][1]][1] = tokens[i][1]
        if is_int_assignments:
            result = operation(total_operators,total_to_assign)
            variables[tokens[index_variable_to_assign][1]][1] = result
    else:
        return f"{tokens[i][1]} no ha sido declarada "
    return str(i+1)

def operation(total_operators,total_to_assign):
    result = total_to_assign[0]
    index = 1
    if not total_operators == []:
        #falta parentesis
        for operator in total_operators:
            if operator == '+':
                result += total_to_assign[index]
            elif operator == '-':
                result -= total_to_assign[index]
            elif operator == '*':
                result *= total_to_assign[index]
            elif operator == '/':
                result /= total_to_assign[index]
            index += 1
    else:
        return result
    return result