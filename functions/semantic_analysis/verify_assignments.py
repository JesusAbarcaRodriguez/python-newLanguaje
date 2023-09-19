from functions.utils.utils import is_declared_variable, is_same_type
def verify_assigments(variables,i,tokens):
    if is_declared_variable(tokens,i,variables):
        variable_to_assign = variables[tokens[i][1]]
        index_variable_to_assign = i
        total_to_assign = []
        total_operators = []
        i += 2
        while tokens[i][0] != 'FIN_DE_INSTRUCCION':
            if tokens[i][0] == 'IDENTIFICADOR':
                if tokens[i][1] in variables and not variables[tokens[i][1]][1] == None  and (is_same_type(variable_to_assign,tokens,i,variables) or variable_to_assign[0] == 'FLOTANTE' and  variables[tokens[i][1]][0] == 'ENTERO'):
                    if variable_to_assign[0] == 'ENTERO' or variable_to_assign[0] == 'FLOTANTE':
                        total_to_assign.append(variables[tokens[i][1]][1])
                    else:
                        variable_to_assign[1] = tokens[i][1]
                    i += 1
                else:
                    return f"Error semantico en {tokens[i][1]}"
            elif tokens[i][0] == 'NUMERO_ENTERO':
                if variable_to_assign[0] == 'ENTERO' or variable_to_assign[0] == 'FLOTANTE':
                    total_to_assign.append(int(tokens[i][1]))
                    i += 1
            elif tokens[i][0] == 'NUMERO_FLOTANTE':
                if variable_to_assign[0] == 'FLOTANTE' :
                    total_to_assign[0].append(int(tokens[i][1]))
                    i += 1
            elif tokens[i][0] == 'VALOR_BOOLEANO':
                if variable_to_assign[0] == 'BOOLEANO':
                    variables[tokens[index_variable_to_assign][1]][1] = tokens[i][1]
            elif tokens[i][0] == "OPERADOR_ARITMETICO":
                total_operators.append(tokens[i][1])
                i += 1
            elif tokens[i][0] == "CARACTER":
                if variable_to_assign[0] == 'CARACTER':
                    variables[tokens[index_variable_to_assign][1]][1] = tokens[i][1]
            elif tokens[i][0] == "CADENA_LITERAL":
                if variable_to_assign[0] == 'CADENA':
                    variables[tokens[index_variable_to_assign][1]][1] = tokens[i][1]
        result = operation(total_operators,total_to_assign)
        variables[tokens[index_variable_to_assign][1]][1] = result
    else:
        return f"{tokens[i][1]} no ha sido declarada "
    return str(i+1)

def operation(total_operators,total_to_assign):
    result = total_to_assign[0]
    index = 1
    if not total_operators == []:
        #falta parentesis
        for operator in total_operators:
            if operator == '+':
                result += total_to_assign[index]
            elif operator == '-':
                result -= total_to_assign[index]
            elif operator == '*':
                result *= total_to_assign[index]
            elif operator == '/':
                result /= total_to_assign[index]
            index += 1
    else:
        return result
    return result