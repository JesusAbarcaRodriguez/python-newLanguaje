from functions.utils.utils import is_declared_variable, is_same_type
def verify_assigments(variables,i,tokens):
    if is_declared_variable(tokens,i,variables):
        variable_to_assign = variables[tokens[i][1]]
        i += 2
        while tokens[i][0] != 'FIN_DE_INSTRUCCION':
            if tokens[i][0] == 'IDENTIFICADOR':
                if not (tokens[i][1] in variables  and (is_same_type(variable_to_assign,tokens,i,variables) or variable_to_assign[0] == 'FLOTANTE' and  variables[tokens[i][1]][0] == 'ENTERO')):
                    return f"Error semantico en {tokens[i][1]}"
                    
            elif tokens[i][0] == 'NUMERO_ENTERO':
                if not variable_to_assign[0] == 'ENTERO' or variable_to_assign[0] == 'FLOTANTE':
                    return f"Error la asignacion es de tipos diferentes {variables[tokens[i][1]]} no es de tipo {tokens[i][0]}"
                i += 1
            elif tokens[i][0] == 'NUMERO_FLOTANTE':
                if not (variable_to_assign[0] == 'FLOTANTE' ):
                    return f"Error la asignacion es de tipos diferentes {variables[tokens[i][1]]} no es de tipo {tokens[i][0]}"
                i += 1
            elif tokens[i][0] == 'VALOR_BOOLEANO':
                if not (variable_to_assign[0] == 'BOOLEANO'):
                    return f"Error la asignacion es de tipos diferentes {variables[tokens[i][1]]} no es de tipo {tokens[i][0]}"
                i += 1
            elif tokens[i][0] == "OPERADOR_ARITMETICO":
                i += 1
            elif tokens[i][0] == "VALOR_CARACTER":
                if not variable_to_assign[0] == 'CARACTER':
                    return f"Error la asignacion es de tipos diferentes {variables[tokens[i][1]]} no es de tipo {tokens[i][0]}"
                i +=1
            elif tokens[i][0] == "CADENA_LITERAL":
                if not variable_to_assign[0] == 'CADENA':
                    return f"Error la asignacion es de tipos diferentes {variables[tokens[i][1]]} no es de tipo {tokens[i][0]}"
                i +=1
            else:
                return f"Error semantico en {tokens[i][1]} no es una asignacion valida"
    else:
        return f"{tokens[i][1]} no ha sido declarada "
    return str(i+1)