def verify_DE(principal,i,tokens):
    from functions.utils.traverse_structure import traverse_structure
    from functions.utils.utils import  is_declared_variable
    init = 0
    end = 0
    if tokens[i][0] == 'NUMERO_ENTERO':
        init = int(tokens[i][1])
    elif tokens[i][0] == "IDENTIFICADOR":
        if is_declared_variable(tokens,i,principal.variables):
            init = principal.variables[tokens[i][1]][1]
    i += 2
    if tokens[i][0] == 'NUMERO_ENTERO':
        end = int(tokens[i][1])
    elif tokens[i][0] == "IDENTIFICADOR":
        if is_declared_variable(tokens,i,principal.variables):
            end = principal.variables[tokens[i][1]][1]
    i += 2
    auxi = i
    while init < end:
        i = auxi
        init += 1
        message = traverse_structure(principal,i,tokens)
        if not message.isdigit():
            return message
        i = int(message)
    return str(i)