import re


def verify_DE(principal,i,tokens):
    from functions.semantic_analysis.verify_CUANDO import verify_CUANDO
    from functions.semantic_analysis.verify_assignments import verify_assigments
    from functions.utils.utils import is_assignment, is_declared_variable, is_for, is_if
    init = 0
    end = 0
    if tokens[i][0] == 'NUMERO_ENTERO':
        init = int(tokens[i][1])
    elif tokens[i][0] == "IDENTIFICADOR":
        if is_declared_variable(tokens,i,principal):
            init = principal.variables[tokens[i][1]][1]
    i += 2
    if tokens[i][0] == 'NUMERO_ENTERO':
        end = int(tokens[i][1])
    elif tokens[i][0] == "IDENTIFICADOR":
        if is_declared_variable(tokens,i,principal):
            end = principal.variables[tokens[i][1]][1]
    i += 2
    auxi = i
    while init < end:
        i = auxi
        init += 1
        while not tokens[i][0] == 'FIN':
            if is_assignment(tokens,i):
                message = verify_assigments(principal,i,tokens)
                if not message.isdigit():
                    return message
                i = int(message)
            if is_for(tokens,i):
                i += 1
                message = verify_DE(principal,i,tokens)
                if not message.isdigit():
                        return message
                i = int(message)
            if is_if(tokens,i):
                i += 1
                message = verify_CUANDO(principal,i,tokens)

    return str(i+1)