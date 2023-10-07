logic_operations = {"OPERADOR_LOGICO_AND","OPERADOR_LOGICO_OR","OPERADOR_COMPARACION"}
def verify_CUANDO(self,principal,i,tokens, variables):
    from functions.utils.traverse_structure_principal import traverse_structure_principal
    from functions.utils.analysis_conditions import evaluate_logic_expression
    from functions.utils.utils import  is_declared_variable
    logic_operators = []
    logic_variables = []
    while not tokens[i][0] == 'INICIO':
        if tokens[i][0] == 'NUMERO_ENTERO' or tokens[i][0] == 'NUMERO_FLOTANTE'  or tokens[i][0] == 'VALOR_CARACTER' or tokens[i][0] == 'CADENA_LITERAL':
            logic_variables.append(tokens[i][1])
        if tokens[i][0] == 'IDENTIFICADOR':
            if is_declared_variable(tokens,i,variables):
                logic_variables.append(variables[tokens[i][1]][1])
            else:
                return f"Error semantico en {tokens[i][1]}"
        elif tokens[i][0] in logic_operations :
            logic_operators.append(tokens[i][1])
        i += 1
    result = evaluate_logic_expression(logic_variables, logic_operators)
    if  result == True:
        i += 1
        message = traverse_structure_principal(self,principal,i,tokens,variables)
        if not message.isdigit():
            return message
        i = int(message)
    else:
        while not tokens[i][0] == 'FIN':
            i=i+1
        i=i+1
        if tokens[i][0] == 'SINO':
            i +=2
            if not message.isdigit():
                return message
            i = int(message)
    return str(i)
