def semantic_call_function_procedure(principal,function_name, parameters_input):
    iterator = 0
    keys_functions = principal.functions.keys()
    keys_procedures = principal.procedures.keys()
    if function_name in keys_functions:
        obj = principal.functions[function_name]
    elif function_name in keys_procedures:
        obj = principal.procedures[function_name]
    else:
        return f"Error: El metodo {function_name} no ha sido definida"
    expected_parameters = obj.parameters
    if len(parameters_input) == len(expected_parameters):
        for param_name, param_data  in expected_parameters.items():
            if param_data[0] == parameters_input[iterator][0]:
                obj.parameters[param_name][1] = parameters_input[iterator][1]
                iterator += 1
            elif param_data[0] == 'ENTERO' and parameters_input[iterator][0] == 'NUMERO_ENTERO':
                obj.parameters[param_name][1] = parameters_input[iterator][1]
                iterator += 1
            elif param_data[0] == 'FLOTANTE' and (parameters_input[iterator][0] == 'NUMERO_FLOTANTE' or parameters_input[iterator][0] == 'NUMERO_ENTERO'):
                obj.parameters[param_name][1] = parameters_input[iterator][1]
                iterator += 1
            elif param_data[0] == 'CADENA' and parameters_input[iterator][0] == 'CADENA_LITERAL':
                obj.parameters[param_name][1] = parameters_input[iterator][1]
                iterator += 1
            elif param_data[0] == 'CARACTER' and parameters_input[iterator][0] == 'VALOR_CARACTER':
                obj.parameters[param_name][1] = parameters_input[iterator][1]
                iterator
            elif param_data[0] == 'BOOLEANO' and parameters_input[iterator][0] == 'VALOR_BOOLEANO':
                obj.parameters[param_name][1] = parameters_input[iterator][1]
                iterator += 1
            else:
                return f'Error: El parámetro {param_name} no coincide en tipo con la definición de la función {function_name}'
    else:
        return f'Error: Número incorrecto de parámetros en la llamada a la función {function_name}'

    return 'OK'