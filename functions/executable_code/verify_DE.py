def verify_DE(self,principal,i,tokens, variables):
    from functions.utils.traverse_structure_principal import traverse_structure_principal
    from functions.utils.utils import  is_declared_variable
    init = 0
    end = 0
    init_value = 0
    if tokens[i][0] == 'NUMERO_ENTERO':
        init_value = int(tokens[i][1])
    elif tokens[i][0] == "IDENTIFICADOR":
        if is_declared_variable(tokens,i,variables):
            init = tokens[i][1]
    i += 2
    if tokens[i][0] == 'NUMERO_ENTERO':
        end = int(tokens[i][1])
    elif tokens[i][0] == "IDENTIFICADOR":
        if is_declared_variable(tokens,i,variables):
            end = tokens[i][1]
    i += 2
    auxi = i
    if init in variables:
        init_value= variables[init][1]
    if end in variables:
        end = variables[end][1]
    while init_value < end:
        i = auxi
        if init in variables:
            init_value= variables[init][1]
        else:
            init_value += 1
        message = traverse_structure_principal(self,principal,i,tokens,variables)
        if not message.isdigit():
            return message
        i = int(message)
    return str(i)