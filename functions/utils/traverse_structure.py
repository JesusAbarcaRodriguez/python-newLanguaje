def traverse_structure(principal,i,tokens):
    from functions.semantic_analysis.semantic_analysis_CUANDO import semantic_analysis_CUANDO
    from functions.semantic_analysis.semantic_analysis_DE import semantic_analysis_DE
    from functions.semantic_analysis.semantic_analysis_MIENTRAS import semantic_analysis_MIENTRAS
    from functions.semantic_analysis.semantic_analysis_assignments import semantic_analysis_assigments
    from functions.utils.utils import is_assignment, is_for, is_if, is_while
    while not tokens[i][0] == 'FIN':
        if is_assignment(tokens,i):
            message = semantic_analysis_assigments(principal,principal.variables,i,tokens)
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
    return str(i+1)