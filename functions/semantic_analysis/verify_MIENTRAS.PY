
logic_operations = {"OPERADOR_LOGICO_AND","OPERADOR_LOGICO_OR","OPERADOR_COMPARACION"}

def verify_MIENTRAS(principal,i,tokens):

    from functions.semantic_analysis.verify_assignments import verify_assigments
    from functions.utils.utils import is_assignment, is_declared_variable, is_for, is_if, is_while
    from functions.semantic_analysis.verify_DE import verify_DE
    from functions.utils.analysis_conditions import evaluate_logic_expression
    from functions.semantic_analysis.verify_CUANDO import verify_CUANDO
    countINICIO = 0
    countFIN = 0
    logic_operators = []
    logic_variables = []
    while not tokens[i][0] == 'INICIO':
        if tokens[i][0] == 'ENTERO' or tokens[i][0] == 'CADENA_LITERAL' or tokens[i][0] == 'CARACTER':
            logic_variables.append(tokens[i][1])
        if tokens[i][0] == 'IDENTIFICADOR':
            if is_declared_variable(tokens,i,principal.variables):
                logic_variables.append(principal.variables[tokens[i][1]][1])
            else:
                return f"Error semantico en {tokens[i][1]}"
        elif tokens[i][0] in logic_operations :
            logic_operators.append(tokens[i][1])
        i += 1
    result = evaluate_logic_expression(logic_variables, logic_operators)
    while result == True:
        while not tokens[i][0] == 'FIN':
            if is_assignment(tokens,i):
                message = verify_assigments(principal,i,tokens)
                if not message.isdigit():
                    return message
                i = int(message)
            elif is_for(tokens,i):
                i += 1
                message = verify_DE(principal,i,tokens)
                if not message.isdigit():
                        return message
                i = int(message)
            elif is_while(tokens,i):
                i += 1
                message = verify_MIENTRAS(principal,i,tokens)
                if not message.isdigit():
                        return message
                i = int(message)
            elif is_if(tokens,i):
                i += 1
                message = verify_CUANDO(principal,i,tokens)
                if not message.isdigit():
                        return message
                i = int(message)

        result = evaluate_logic_expression(logic_variables, logic_operators)
    while not tokens[i][0] == 'FIN':
        i += 1
    return str(i+1)