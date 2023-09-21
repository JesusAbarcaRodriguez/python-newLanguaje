

from functions.utils.utils import is_declared_variable


def traverse_structure_principal(principal,i,tokens):
    from functions.semantic_analysis.semantic_analysis_call_function import semantic_analysis_call_function
    from functions.executable_code.verify_DE import verify_DE   
    from functions.executable_code.assignments_variables import verify_assigments
    from functions.utils.utils import is_assignment, is_for, is_if, is_while, is_called_fuction
    from functions.executable_code.verify_CUANDO import verify_CUANDO
    from functions.executable_code.verify_Mientras import verify_MIENTRAS
    parameters_input = []
    while not tokens[i][0] == 'FIN':
        if is_assignment(tokens,i):
            message = verify_assigments(principal.variables,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
        elif is_for(tokens,i):
            i += 1
            message = verify_DE(principal,i,tokens)
            if not message.isdigit():
                    return message
            i = int(message)
        elif is_while(tokens,i):
            i += 1
            message = verify_MIENTRAS(principal,i,tokens)
            if not message.isdigit():
                    return message
            i = int(message)
        elif is_if(tokens,i):
            i += 1
            message = verify_CUANDO(principal,i,tokens)
            if not message.isdigit():
                    return message
            i = int(message)
        elif is_called_fuction(tokens,i):
            function_name= tokens[i][1]
            i += 2
            while tokens[i][0] != 'PARENTESIS_DER':
                if tokens[i][0] == 'IDENTIFICADOR':
                    if is_declared_variable(tokens,i,principal.variables):
                        parameters_input.append(principal.variables.get(tokens[i][1]))
                    i += 1
                else:
                    parameters_input = tokens[i]
            message = semantic_analysis_call_function(principal,function_name,parameters_input)
            if not message == "OK":
                    return message
            i += 2
        else:
            return f"Error sintactico en {tokens[i][1]}"
    return str(i+1)