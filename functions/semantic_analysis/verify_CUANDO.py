from functions.utils.utils import is_declared_variable
logic_operations = {"OPERADOR_LOGICO_AND","OPERADOR_LOGICO_OR","OPERADOR_COMPARACION"}
def verify_CUANDO(principal,i,tokens):
    logic_operators = []
    logic_variables = []
    while not tokens[i][0] == 'INICIO':
        if tokens[i][0] == 'ENTERO' or tokens[i][0] == 'CADENA_LITERAL' or tokens[i][0] == 'CARACTER':
            logic_variables.append(tokens[i][1])
        if tokens[i][0] == 'IDENTIFICADOR':
            if is_declared_variable(tokens,i,principal):
                logic_variables.append(principal.variables[tokens[i][1]][1])
            else:
                return f"Error semantico en {tokens[i][1]}"
        elif tokens[i][0] in logic_operations :
            logic_operators.append(tokens[i][1])
        i += 1
    result = evaluate_logic_expression(logic_variables, logic_operators)
    return result
def evaluate_logic_expression(logic_variables, logic_operators):
    index = 0
    bool_operations = []
    isAnd = False
    isOr = False
    while index < len(logic_operators) + len(logic_variables):
        if index < len(logic_operators):
            operator = logic_operators[index]
        elif operator == '=':
            if logic_variables[index] == logic_variables[index+1]:
                bool_operations.append(True)
                index += 1
            else:
                bool_operations.append(False)
                index += 1
        elif operator == '<':
            if logic_variables[index] < logic_variables[index+1]:
                bool_operations.append(True)
                index += 1
            else:
                bool_operations.append(False)
                index += 1
        elif operator == '>':
            if logic_variables[index] > logic_variables[index+1]:
                bool_operations.append(True)
                index += 1
            else:
                bool_operations.append(False)
                index += 1
        elif operator == '!':
            if logic_variables[index] != logic_variables[index+1]:
                bool_operations.append(True)
                index += 1
            else:
                bool_operations.append(False)
                index += 1
        elif operator == '&':
            isAnd=True
            index += 1
        elif operator == '#':
            isOr=True
            index += 1
    return bool_operations[index]
