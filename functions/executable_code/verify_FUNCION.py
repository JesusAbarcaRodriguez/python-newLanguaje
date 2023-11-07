from functions.executable_code.verify_write import verify_write
from functions.utils.utils import is_read, is_return, is_write
def verify_FUNCION(self,principal,init_function,tokens,function_name):
    from functions.executable_code.verify_PROCEDIMIENTO import verify_PROCEDIMIENTO
    from functions.semantic_analysis.semantic_call_function_procedure import semantic_call_function_procedure
    from functions.utils.utils import is_called_fuction_procedure, is_declared_variable
    from functions.executable_code.assignments_variables import verify_assigments
    from functions.executable_code.verify_CUANDO import verify_CUANDO
    from functions.executable_code.verify_DE import verify_DE
    from functions.executable_code.verify_Mientras import verify_MIENTRAS
    from functions.utils.utils import error_message, is_assignment, is_for, is_if, is_while

    function = principal.functions[function_name]
    i = init_function
    variablesAux = function.parameters.copy()
    variables = principal.variables.copy()
    variables.update(variablesAux)
    while not tokens[i][0] == 'FIN':
        if is_assignment(tokens,i):
            message = verify_assigments(self,principal,variables,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
        elif is_read(tokens,i):
            i += 4
        elif is_write(tokens,i):
            message = verify_write(self,variables,principal.arrays,principal.matrix,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
        elif is_for(tokens,i):
            i += 1
            message = verify_DE(self,principal,i,tokens,variables)
            if not message.isdigit():
                    return message
            i = int(message)
        elif is_while(tokens,i):
            i += 1
            message = verify_MIENTRAS(self,principal,i,tokens,variables)
            if not message.isdigit():
                    return message
            i = int(message)
        elif is_if(tokens,i):
            i += 1
            message = verify_CUANDO(self,principal,i,tokens, variables)
            if not message.isdigit():
                    return message
            i = int(message)
        elif tokens[i][0] == 'SINO':
            while not tokens[i][0] == 'FIN':
                i=i+1
            i=i+1
        elif is_return(tokens,i):
            i += 1
            if tokens[i][0] == 'IDENTIFICADOR':
                if tokens[i][1] in variables:
                    function.return_data = variables[tokens[i][1]][1]
                else:
                    return f"Error semantico en {error_message(tokens, i )}"
            elif tokens[i][0] in ['NUMERO_ENTERO','NUMERO_FLOTANTE','VALOR_CADENA','VALOR_CARACTER','VALOR_BOOLEANO']:
                function.return_data = tokens[i][1]
            else:
                return f"Error semantico en {error_message(tokens, i )}"
            i += 2
            break
        elif is_called_fuction_procedure(tokens,i):
            function_name2= tokens[i][1]
            i += 2
            while tokens[i][0] != 'PARENTESIS_DER':
                if tokens[i][0] == 'IDENTIFICADOR':
                    if is_declared_variable(tokens,i,principal.variables):
                        parameters_input.append(principal.variables.get(tokens[i][1]))
                    i += 1
                else:
                    parameters_input = tokens[i]

            if  len(parameters_input):
                message = semantic_call_function_procedure(principal,function_name2,parameters_input)
                if not message == "OK":
                        return message
            keys_functions = principal.functions.keys()
            keys_procedures = principal.procedures.keys()
            if function_name2 in keys_functions:
                init_function = principal.functions[function_name2].init_function
                verify_FUNCION(self,principal,init_function,tokens,function_name2)
            if function_name2 in keys_procedures:
                init_function = principal.functions[function_name2].init_function
                verify_PROCEDIMIENTO(self,principal,init_function,tokens,function_name2)
            i += 2

    return str(i+1)
