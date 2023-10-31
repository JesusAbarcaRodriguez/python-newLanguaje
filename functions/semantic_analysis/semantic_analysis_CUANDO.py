logic_operations = {"OPERADOR_LOGICO_AND","OPERADOR_LOGICO_OR","OPERADOR_COMPARACION"}
def semantic_analysis_CUANDO(principal,variables,i,tokens):
    from functions.utils.traverse_structure import traverse_structure
    from functions.utils.analysis_conditions import evaluate_type_expression
    from functions.utils.utils import error_message,  is_declared_variable
    logic_operators = []
    logic_variables = []
    while not tokens[i][0] == 'INICIO':
        if tokens[i][0] == 'NUMERO_ENTERO' or tokens[i][0] == 'NUMERO_FLOTANTE' or tokens[i][0] == 'CADENA_LITERAL' or tokens[i][0] == 'VALOR_CARACTER' :
            logic_variables.append(tokens[i][0])
        if tokens[i][0] == 'IDENTIFICADOR':
            if is_declared_variable(tokens,i,variables):
                logic_variables.append(variables[tokens[i][1]][0])
            else:
                return f"Error semantico en {error_message(tokens, i )}"
        elif tokens[i][0] in logic_operations :
            logic_operators.append(tokens[i][1])
        i += 1
    i += 1
    result = evaluate_type_expression(logic_variables, logic_operators)
    if not result == "OK":
        return result
    else:
        message = traverse_structure(principal,variables,i,tokens)
        if not message.isdigit():
            return message
        i = int(message)
        if tokens[i][0] == 'SINO':
            i +=2
            message = traverse_structure(principal,variables,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
    return str(i)
