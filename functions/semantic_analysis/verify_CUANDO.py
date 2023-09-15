from functions.utils.utils import is_declared_variable
from collections import deque
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
    return result#AQUI HACER ALGO MAS CON EL RESULT, NO RETORNARLO
def evaluate_logic_expression(logic_variables, logic_operators):
    index = 0
    stack_bool_operations = deque()
    stack_and_or = deque()
    while index < len(logic_operators) :
        operator = logic_operators[index]
        if operator == '=':
            if logic_variables[index] == logic_variables[index+1]:
                stack_bool_operations.append(True)
                index += 1
            else:
                stack_bool_operations.append(False)
                index += 1
        elif operator == '<':
            if logic_variables[index] < logic_variables[index+1]:
                stack_bool_operations.append(True)
                index += 1
            else:
                stack_bool_operations.append(False)
                index += 1
        elif operator == '>':
            if logic_variables[index] > logic_variables[index+1]:
                stack_bool_operations.append(True)
                index += 1
            else:
                stack_bool_operations.append(False)
                index += 1
        elif operator == '!':
            if logic_variables[index] != logic_variables[index+1]:
                stack_bool_operations.append(True)
                index += 1
            else:
                stack_bool_operations.append(False)
                index += 1
        elif operator == '&':
            stack_and_or.append('&')
            index += 1
        elif operator == '#':
            stack_and_or.append('#')
            index += 1
    for operator in stack_and_or:
        if operator == '&':
            aux = stack_bool_operations.pop()
            aux2 = stack_bool_operations.pop()
            stack_bool_operations.append(aux and aux2)
        if operator == '#':
            aux = stack_bool_operations.pop()
            aux2 = stack_bool_operations.pop()
            stack_bool_operations.append(aux or aux2)
    return top(stack_and_or)
def top(pila):
    if not pila:
        return (r' ', ' ')  # Devuelve None si la pila está vacía
    return pila[-1]  # Devuelve el último elemento de la pila
