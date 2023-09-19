def verify_FUNCION(principal,i,tokens):
    from functions.semantic_analysis.semantic_objcs import Function
    from functions.semantic_analysis.verify_CUANDO import verify_CUANDO
    from functions.semantic_analysis.verify_DE import verify_DE
    from functions.semantic_analysis.verify_MIENTRAS import verify_MIENTRAS
    from functions.semantic_analysis.verify_assignments import verify_assigments
    from functions.utils.utils import is_assignment, is_for, is_if, is_parameters_declaration, is_while

    init_funtion = i
    function = Function(tokens[i][1],tokens[i+2][1])
    function.init_function = init_funtion
    i = i + 4
    while tokens[i][0] != 'PARENTESIS_DER':
        if is_parameters_declaration(tokens,i):
            function.parameters[tokens[i+1][1]] = [tokens[i][1],None]
            i += 2
        else:
            return f"Error semantico en {tokens[i][1]}"
    i += 2
    variables = principal.variables.copy()
    variables.update(function.parameters)
    while not tokens[i][0] == 'FIN':
        if is_assignment(tokens,i):
            message = verify_assigments(variables,i,tokens)
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
        
    end_function = i
    function.end_function = end_function
    principal.functions[function.identifier] = function
    return str(i+1)
