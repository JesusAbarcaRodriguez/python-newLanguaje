from collections import deque

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
    return top(stack_bool_operations)

def top(pila):
    if not pila:
        return (r' ', ' ')
    return pila[-1]