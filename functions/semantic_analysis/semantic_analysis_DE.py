def semantic_analysis_DE(principal,variables,i,tokens):
    from functions.utils.traverse_structure import traverse_structure
    from functions.utils.utils import  error_message,is_same_expression_type, is_declared_variable
    variable_init = 0
    variable_fin = 0
    if tokens[i][0] == 'IDENTIFICADOR':
        if is_declared_variable(tokens,i,variables):
            variable_init = variables[tokens[i][1]][0]
    elif tokens[i][0] == 'NUMERO_ENTERO':
        variable_init = tokens[i][0]
    else:
        return f"Error semantico en {error_message(tokens, i )} No se puede recorrer un rango con un tipo de dato {tokens[i][0]}"
    i += 2
    if tokens[i][0] == 'IDENTIFICADOR':
        if is_declared_variable(tokens,i,variables):
            variable_fin = variables[tokens[i][1]][0]
    elif tokens[i][0] == 'NUMERO_ENTERO':
        variable_fin = tokens[i][0]
    else:
        return f"Error semantico en {error_message(tokens, i )} No se puede recorrer un rango con un tipo de dato {tokens[i][0]}"
    if is_same_expression_type(variable_init, variable_fin) or variable_init == 'NUMERO_ENTERO' or variable_fin == 'ENTERO' or variable_init == 'ENTERO' or variable_fin == 'NUMERO_ENTERO' :
        i+=2
        message = traverse_structure(principal,variables,i,tokens)
        if not message.isdigit():
            return message
        i = int(message)
    else:
        return f"Error semantico en {error_message(tokens, i )} No se puede recorrer un rango con un tipo de dato {tokens[i][0]}"
    return str(i)