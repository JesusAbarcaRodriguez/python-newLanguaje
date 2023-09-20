def semantic_analysis_DE(principal,i,tokens):
    from functions.utils.traverse_structure import traverse_structure
    from functions.utils.utils import  is_declared_variable
    from functions.utils.utils import is_same_expression_type
    variable_init = 0
    variable_fin = 0
    if tokens[i][0] == 'IDENTIFICADOR':
        if is_declared_variable(tokens,i,principal.variables):
            variable_init = principal.variables[tokens[i][1]][0]
    elif tokens[i][0] == 'NUMERO_ENTERO':
        variable_init = tokens[i][0]
    else:
        return f"Error semantico en {tokens[i][1]} No se puede recorrer un rango con un tipo de dato {tokens[i][0]}"
    i += 2
    if tokens[i][0] == 'IDENTIFICADOR':
        if is_declared_variable(tokens,i+2,principal.variables):
            variable_fin = principal.variables[tokens[i+2][1]][0]
    elif tokens[i][0] == 'NUMERO_ENTERO':
        variable_fin = tokens[i][0]
    else:
        return f"Error semantico en {tokens[i][1]} No se puede recorrer un rango con un tipo de dato {tokens[i][0]}"

    if is_same_expression_type(variable_init, variable_fin):
        message = traverse_structure(principal,i,tokens)
        if not message.isdigit():
            return message
        i = int(message)
    return str(i)