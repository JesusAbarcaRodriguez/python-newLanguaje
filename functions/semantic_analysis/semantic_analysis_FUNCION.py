def semantic_analysis_FUNCION(principal,i,tokens):
    from functions.semantic_analysis.semantic_analysis_MIENTRAS import semantic_analysis_MIENTRAS
    from functions.utils.global_state import Function
    from functions.semantic_analysis.semantic_analysis_CUANDO import semantic_analysis_CUANDO
    from functions.semantic_analysis.semantic_analysis_DE import semantic_analysis_DE
    from functions.semantic_analysis.semantic_analysis_assignments import semantic_analysis_assigments
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
            message = semantic_analysis_assigments(variables,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
        elif is_for(tokens,i):
            i += 1
            message = semantic_analysis_DE(principal,i,tokens)
            if not message.isdigit():
                    return message
            i = int(message)
        elif is_while(tokens,i):
            i += 1
            message = semantic_analysis_MIENTRAS(principal,i,tokens)
            if not message.isdigit():
                    return message
            i = int(message)
        elif is_if(tokens,i):
            i += 1
            message = semantic_analysis_CUANDO(principal,i,tokens)
            if not message.isdigit():
                    return message
            i = int(message)
        
    end_function = i
    function.end_function = end_function
    principal.functions[function.identifier] = function
    return str(i+1)
