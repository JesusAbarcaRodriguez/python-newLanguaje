logic_operations = {"OPERADOR_LOGICO_AND","OPERADOR_LOGICO_OR","OPERADOR_COMPARACION"}
def semantic_analysis_CUANDO(principal,i,tokens):
    from functions.semantic_analysis.traverse_structure.traverse_structure import traverse_structure
    from functions.utils.analysis_conditions import evaluate_type_expression
    from functions.utils.utils import  is_declared_variable
    logic_operators = []
    logic_variables = []
    while not tokens[i][0] == 'INICIO':
        if tokens[i][0] == 'ENTERO' or tokens[i][0] == 'FLOTANTE' or tokens[i][0] == 'CADENA_LITERAL' or tokens[i][0] == 'CARACTER' :
            logic_variables.append(tokens[i][1])
        if tokens[i][0] == 'IDENTIFICADOR':
            if is_declared_variable(tokens,i,principal.variables):
                logic_variables.append(principal.variables[tokens[i][1]][1])
            else:
                return f"Error semantico en {tokens[i][1]}"
        elif tokens[i][0] in logic_operations :
            logic_operators.append(tokens[i][1])
        i += 1
    result = evaluate_type_expression(logic_variables, logic_operators)
    if not result == "OK":
        return result
    else:    
        message = traverse_structure(principal,i,tokens)
        if not message.isdigit():
            return message
        i = int(message)
    while not tokens[i][0] == 'FIN':
            i=i+1
    i=i+1
    if tokens[i][0] == 'SINO':                          
        i +=2
        message = traverse_structure(principal,i,tokens)
        if not message.isdigit():
            return message
        i = int(message)
    return str(i)
