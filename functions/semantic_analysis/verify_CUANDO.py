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
    result = None
    all_true = True  # Bandera para la operación AND
    while index < len(logic_operators):
        operator = logic_operators[index]

        if operator == '=':
            result = logic_variables[index] == logic_variables[index + 1]
        elif operator == '<':
            result = logic_variables[index] < logic_variables[index + 1]
        elif operator == '>':
            result = logic_variables[index] > logic_variables[index + 1]
        elif operator == '!':
            result = logic_variables[index] != logic_variables[index + 1]
        elif operator == '&':
            result = logic_variables[index] and logic_variables[index + 1]
            all_true = all_true and result  # Actualizar la bandera
        elif operator == '#':
            result = logic_variables[index] or logic_variables[index + 1]

        index += 2  # Avanzar al siguiente par de valores

        if result is False and operator == '#':
            return False  # Si encontramos un OR verdadero, no es necesario seguir evaluando

    return all_true  # Si llega aquí, todas las expresiones AND son verdaderas