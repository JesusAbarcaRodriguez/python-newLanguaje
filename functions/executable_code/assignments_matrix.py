from functions.utils.utils import is_read


def assignments_matrix(self,principal,matrix,variables,i,tokens):
    from pprint import isreadable
    from functions.executable_code.verify_FUNCION import verify_FUNCION
    from functions.semantic_analysis.semantic_call_function_procedure import semantic_call_function_procedure
    from functions.utils.utils import is_called_fuction_procedure, is_declarate_matrix, is_declared_variable, is_same_type
    from PyQt5.QtCore import QEventLoop
    if is_declarate_matrix(tokens,i,matrix):
        matrix_to_assign = matrix[tokens[i][1]]
        variable_name = tokens[i][1]
        index_matrix_to_assign = i
        total_nums_to_assign = []
        total_strings_to_assign = []
        total_operators = []
        parameters_input = []
        is_int_assignments = False
        is_string_assignments = False
        i+=1
        row = tokens[i][1]
        if  tokens[i][1] in variables:
            valor = variables[tokens[i][1]]
            if not valor[0] == 'ENTERO':
                return f"Error semantico en {valor} no es un indice valido"
        elif tokens[i][1].isdigit():
            if int(tokens[i][1]) >= int(matrix_to_assign[2]):
                return f"Error semantico en {valor} no es un indice valido"
        else:
            return f"Error semantico en {tokens[i][1]} no es un indice valido"
        i+=1
        column = tokens[i][1]
        if  tokens[i][1] in variables:
            valor = variables[tokens[i][1]]
            if not valor[0] == 'ENTERO':
                return f"Error semantico en {valor} no es un indice valido"
        elif tokens[i][1].isdigit():
            if int(tokens[i][1]) >= int(matrix_to_assign[3]):
                return f"Error semantico en {valor} no es un indice valido"
        else:
            return f"Error semantico en {tokens[i][1]} no es un indice valido"
        i += 2
        while tokens[i][0] != 'FIN_DE_INSTRUCCION':
            if is_called_fuction_procedure(tokens,i):
                function_name= tokens[i][1]
                keys_functions = principal.functions.keys()
                if function_name in keys_functions:
                    if principal.functions[function_name].data_type == matrix_to_assign[0]:
                        i += 2
                        while tokens[i][0] != 'PARENTESIS_DER':
                            if tokens[i][0] == 'IDENTIFICADOR':
                                if is_declared_variable(tokens,i,principal.variables):
                                    parameters_input.append(principal.variables.get(tokens[i][1]))
                                i += 1
                            else:
                                parameters_input.append(tokens[i])
                                i += 1
                        if  len(parameters_input):
                            message = semantic_call_function_procedure(principal,function_name,parameters_input)
                            if not message == "OK":
                                    return message
                        init_function = principal.functions[function_name].init_function
                        verify_FUNCION(self,principal,init_function,tokens,function_name)
                        matrix[tokens[index_matrix_to_assign][1]][1] = [principal.functions[function_name].return_data,row,column]
                        i += 1
                    else:
                        return f"Error: La variable: '{matrix_to_assign[1]}' no es del mismo tipo que la funcion {function_name} "
            elif is_read(tokens,i):
                self.on_comand_line()
                event_loop = QEventLoop()
                self.command_line.returnPressed.connect(event_loop.quit)
                event_loop.exec_()
                result = self.comand_text
                self.off_comand_line()
                if matrix_to_assign[0] == 'ENTERO':
                    if result.isdigit():
                        result = int(result)
                        matrix[tokens[index_matrix_to_assign][1]][1]  = [(result, row, column)]
                    else:
                        return f"Error: La variable: '{matrix_to_assign[1]}' de tipo '{matrix_to_assign[0]}' no coincide con {result} "
                elif matrix_to_assign[0] == 'FLOTANTE':
                    if result.isdigit():
                        result = float(result)
                        matrix[tokens[index_matrix_to_assign][1]][1]  = [(result, row, column)]
                    else:
                        return f"Error: La variable: '{matrix_to_assign[1]}' de tipo '{matrix_to_assign[0]}' no coincide con {result} "
                elif matrix_to_assign[0] == "CADENA":
                    matrix[tokens[index_matrix_to_assign][1]][1]  = [(result, row, column)]
                elif matrix_to_assign[0] == "CARACTER":
                    if result.len()==1:
                        matrix[tokens[index_matrix_to_assign][1]][1]  = [(result, row, column)]
                    else:
                        return f"Error: La variable: '{matrix_to_assign[1]}' de tipo '{matrix_to_assign[0]}' solo permite un caracter "
                else:
                    return f"Error: La variable: '{matrix_to_assign[1]}' no es del mismo tipo que la funcion que {result} "
                i += 1

            elif tokens[i][0] == 'IDENTIFICADOR':
                if tokens[i][1] in variables and not variables[tokens[i][1]][1] == None  and (is_same_type(matrix_to_assign,tokens,i,variables) or matrix_to_assign[0] == 'FLOTANTE' and  variables[tokens[i][1]][0] == 'ENTERO'):
                    if matrix_to_assign[0] == 'ENTERO' or matrix_to_assign[0] == 'FLOTANTE':
                        total_nums_to_assign.append(variables[tokens[i][1]][1])
                        is_int_assignments = True
                    else:
                        matrix[tokens[index_matrix_to_assign][1]][1] = [(result, row, column)]
                    i += 1
                else:
                    return f"Error semantico en {tokens[i][1]}"
            elif tokens[i][0] == 'NUMERO_ENTERO':
                if matrix_to_assign[0] == 'ENTERO' or matrix_to_assign[0] == 'FLOTANTE':
                    total_nums_to_assign.append(int(tokens[i][1]))
                    is_int_assignments = True
                    i += 1
            elif tokens[i][0] == 'NUMERO_FLOTANTE':
                if matrix_to_assign[0] == 'FLOTANTE' :
                    total_nums_to_assign.append(int(tokens[i][1]))
                    is_int_assignments = True
                    i += 1
            elif tokens[i][0] == 'VALOR_BOOLEANO':
                if matrix_to_assign[0] == 'BOOLEANO':
                    matrix[tokens[index_matrix_to_assign][1]][1] = [(result, row, column)]
            elif tokens[i][0] == "OPERADOR_ARITMETICO" or tokens[i][0] == "PARENTESIS_IZQ" or tokens[i][0] == "PARENTESIS_DER":
                total_operators.append(tokens[i][1])
                i += 1
            elif tokens[i][0] == "CARACTER":
                if matrix_to_assign[0] == 'CARACTER':
                    matrix[tokens[index_matrix_to_assign][1]][1] = [(result, row, column)]
            elif tokens[i][0] == "CADENA_LITERAL":
                if matrix_to_assign[0] == 'CADENA':
                    total_strings_to_assign.append(tokens[i][1])
                    is_string_assignments = True
                    i += 1
        if is_int_assignments:
            result = assign_nums_operation(total_operators,total_nums_to_assign)
            matrix[tokens[index_matrix_to_assign][1]][1]  = [(result, row, column)]
        if is_string_assignments:
            result = assign_string_operation(total_operators,total_strings_to_assign)
            matrix[tokens[index_matrix_to_assign][1]][1]  = [(result, row, column)]
    else:
        return f"{tokens[i][1]} no ha sido declarada "
    return str(i+1)
def assign_string_operation(total_operators,total_strings_to_assign):
    result = total_strings_to_assign[0]
    index = 1
    if not total_operators == []:
        for operator in total_operators:
            if operator == '+':
                result += total_strings_to_assign[index]
            index += 1
    else:
        return result
    return result
def assign_nums_operation(total_operators,total_nums_to_assign):
    result = total_nums_to_assign[0]
    index = 1
    if not total_operators == []:
        for operator in total_operators:
            if operator == '+':
                result += total_nums_to_assign[index]
            elif operator == '-':
                result -= total_nums_to_assign[index]
            elif operator == '*':
                result *= total_nums_to_assign[index]
            elif operator == '/':
                result /= total_nums_to_assign[index]
            index += 1
    else:
        return result
    return result