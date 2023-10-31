logic_operations = {"OPERADOR_LOGICO_AND","OPERADOR_LOGICO_OR","OPERADOR_COMPARACION"}
def verify_MIENTRAS(self,principal,i,tokens, variables):
    from functions.utils.traverse_structure_principal import traverse_structure_principal
    from functions.utils.utils import  error_message, is_declared_variable
    from functions.utils.analysis_conditions import evaluate_logic_expression

    logic_operators = []
    logic_variables = []
    while not tokens[i][0] == 'INICIO':
        if tokens[i][0] == 'ENTERO' or tokens[i][0] == 'CADENA_LITERAL' or tokens[i][0] == 'CARACTER':
            logic_variables.append(tokens[i][1])
        if tokens[i][0] == 'IDENTIFICADOR':
            if is_declared_variable(tokens,i,variables):
                logic_variables.append(variables[tokens[i][1]][1])
            else:
                return f"Error semantico en {error_message(tokens, i )}"
        elif tokens[i][0] in logic_operations :
            logic_operators.append(tokens[i][1])
        i += 1
    result = evaluate_logic_expression(logic_variables, logic_operators)
    while result == True:
        message = traverse_structure_principal(self,principal,i,tokens)
        if not message.isdigit():
            return message
        i = int(message)

        result = evaluate_logic_expression(logic_variables, logic_operators)
    while not tokens[i][0] == 'FIN':
        i += 1
    return str(i)