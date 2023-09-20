def traverse_structure(principal,i,tokens):
    from functions.semantic_analysis.semantic_analysis_CUANDO import verify_CUANDO
    from functions.semantic_analysis.semantic_analysis_DE import verify_DE
    from functions.semantic_analysis.verify_MIENTRAS import verify_MIENTRAS
    from functions.semantic_analysis.semantic_analysis_assignments import verify_assigments
    from functions.utils.utils import is_assignment, is_for, is_if, is_while
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
    return str(i+1)