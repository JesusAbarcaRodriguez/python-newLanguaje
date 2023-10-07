
from functions.executable_code.verify_write import verify_write
from functions.utils.utils import is_write

def traverse_structure_principal(self,principal,i,tokens,variables):
    from functions.semantic_analysis.semantic_call_function_procedure import semantic_call_function_procedure
    from functions.executable_code.verify_DE import verify_DE   
    from functions.executable_code.assignments_variables import verify_assigments
    from functions.utils.utils import is_assignment, is_for, is_if, is_while, is_called_fuction_procedure
    from functions.executable_code.verify_CUANDO import verify_CUANDO
    from functions.executable_code.verify_Mientras import verify_MIENTRAS
    from functions.executable_code.verify_FUNCION import verify_FUNCION
    from functions.executable_code.verify_PROCEDIMIENTO import verify_PROCEDIMIENTO
    from functions.utils.utils import is_declared_variable
    parameters_input = []
    while not tokens[i][0] == 'FIN':
        if is_assignment(tokens,i):
            message = verify_assigments(self,principal,principal.variables,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
        elif is_write(tokens,i):
            message = verify_write(self,principal.variables,i,tokens)
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
            message = verify_MIENTRAS(self,principal,i,tokens)
            if not message.isdigit():
                    return message
            i = int(message)
        elif is_if(tokens,i):
            i += 1
            message = verify_CUANDO(self,principal,i,tokens)
            if not message.isdigit():
                    return message
            i = int(message)
        elif is_called_fuction_procedure(tokens,i):
            function_procedures_name= tokens[i][1]
            i += 2
            while tokens[i][0] != 'PARENTESIS_DER':
                if tokens[i][0] == 'IDENTIFICADOR':
                    if is_declared_variable(tokens,i,principal.variables):
                        parameters_input.append(principal.variables.get(tokens[i][1]))
                    i += 1
                else:
                    parameters_input = tokens[i]

            if  len(parameters_input): 
                message = semantic_call_function_procedure(principal,function_procedures_name,parameters_input)
                if not message == "OK":
                        return message
            keys_functions = principal.functions.keys()
            keys_procedures = principal.procedures.keys()
            if function_procedures_name in keys_functions:
                init_function = principal.functions[function_procedures_name].init_function
                verify_FUNCION(self,principal,init_function,tokens,function_procedures_name)
            if function_procedures_name in keys_procedures:
                init_function = principal.procedure[function_procedures_name].init_function
                verify_PROCEDIMIENTO(self,principal,init_function,tokens,function_procedures_name)
            i += 2
        else:
            return f"Error semantico en {tokens[i][1]}"
    return str(i+1)