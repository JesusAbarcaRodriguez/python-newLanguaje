def verify_DE(self,principal,i,tokens, variables):
    from functions.utils.traverse_structure_principal import traverse_structure_principal
    from functions.utils.utils import  is_declared_variable
    init = 0
    end = 0
    if tokens[i][0] == 'NUMERO_ENTERO':
        init = int(tokens[i][1])
    elif tokens[i][0] == "IDENTIFICADOR":
        if is_declared_variable(tokens,i,variables):
            init = variables[tokens[i][1]][1]
    i += 2
    if tokens[i][0] == 'NUMERO_ENTERO':
        end = int(tokens[i][1])
    elif tokens[i][0] == "IDENTIFICADOR":
        if is_declared_variable(tokens,i,variables):
            end = variables[tokens[i][1]][1]
    i += 2
    auxi = i
    while init < end:
        i = auxi
        init += 1
        message = traverse_structure_principal(self,principal,i,tokens,variables)
        if not message.isdigit():
            return message
        i = int(message)
    return str(i)