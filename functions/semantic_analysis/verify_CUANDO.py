from collections import deque
logic_operations = {"OPERADOR_LOGICO_AND","OPERADOR_LOGICO_OR","OPERADOR_COMPARACION"}
def verify_CUANDO(principal,i,tokens):
    from functions.semantic_analysis.verify_DE import verify_DE
    from functions.semantic_analysis.verify_assignments import verify_assigments
    from functions.utils.utils import is_assignment, is_declared_variable, is_for, is_if, is_while
    logic_operators = []
    logic_variables = []
    countINICIO = 0
    countFIN = 0
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
    if  result == True:
        countINICIO += 1
        while not countFIN == countINICIO:
            if is_assignment(tokens,i):
                message = verify_assigments(principal,i,tokens)
            if not message.isdigit():
                return message
                i = int(message)
            elif is_for(tokens,i):
                i += 1
                verify_DE(principal,i,tokens)
            elif is_while(tokens,i):
                i += 1
            elif is_if(tokens,i):
                i += 1
                verify_CUANDO(principal,i,tokens)
            if tokens[i][0] == 'INICIO':
                    countINICIO += 1
            if tokens[i][0] == 'FIN':
                    countFIN += 1
    else:
        while not tokens[i][0] == 'SINO':
            i +=1
        countINICIO += 1
        i +=2
        while not countFIN == countINICIO:
            if is_assignment(tokens,i):
                message = verify_assigments(principal,i,tokens)
                if not message.isdigit():
                    return message
                i = int(message)
            elif is_for(tokens,i):
                i += 1
                message = verify_DE(principal,i,tokens)
            elif is_while(tokens,i):
                i += 1
            elif is_if(tokens,i):
                i += 1
                message = verify_CUANDO(principal,i,tokens)
            if tokens[i][0] == 'INICIO':
                    countINICIO += 1
            if tokens[i][0] == 'FIN':
                    countFIN += 1
    return message
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
