from collections import deque

def evaluate_logic_expression(logic_variables, logic_operators):
    index = 0
    stack_bool_operations = deque()
    stack_and_or = deque()
    if len(logic_variables) == 1 and logic_variables[0] == 'VERDADERO' or logic_variables[0] == 'FALSO':
        if logic_variables[0] == 'VERDADERO':
            return True
        elif logic_variables[0] == 'FALSO':
            return False
    else:
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
                if  logic_variables[index] == "VERDADERO" or logic_variables[index] == "FALSO" and logic_variables[index+1] == "VERDADERO" or logic_variables[index+1] == "FALSO":
                    return f"Error semantico en {logic_variables[index]} no se puede comparar con <"
                else:
                    if logic_variables[index] < logic_variables[index+1]:
                        stack_bool_operations.append(True)
                        index += 1
                    else:
                        stack_bool_operations.append(False)
                        index += 1
            elif operator == '>':
                if  logic_variables[index] == "VERDADERO" or logic_variables[index] == "FALSO" or logic_variables[index+1] == "VERDADERO" or logic_variables[index+1] == "FALSO":
                    return f"Error semantico en {logic_variables[index]} no se puede comparar con <"
                else:
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
    return top(stack_bool_operations)

def evaluate_type_expression(logic_variables, logic_operators):
    index = 0
    stack_bool_operations = deque()
    stack_and_or = deque()
    while index < len(logic_operators) :
        operator = logic_operators[index]
        if operator == '=' or operator == '<' or operator == '>' or operator == '!':
            variable1 = logic_variables.pop()
            variable2 = logic_variables.pop()
            if variable1 == variable2 or ( variable1 == 'NUMERO_ENTERO' and variable2 == 'ENTERO')or (variable2 == 'NUMERO_ENTERO' and variable1 == 'ENTERO'):
                index += 1
            else:
                if operator == '='or operator == '!':
                    index += 1
                else:
                    return f"Error semantico en {variable1} y {variable2}"

        elif operator == '&' or operator == '#':
            index += 1
    return 'OK'

def top(pila):
    if not pila:
        return (r' ', ' ')
    return pila[-1]
