
from numbers import Number
from PyQt5.QtCore import QEventLoop
from functions.executable_code.assignments_matrix import filtrar_por_fila_columna

from functions.utils.utils import is_array_call, is_matrix_call

def verify_assigments(self,principal,variables,arrays,i,tokens):
    from functions.utils.utils import is_read
    from functions.executable_code.verify_FUNCION import verify_FUNCION
    from functions.semantic_analysis.semantic_call_function_procedure import semantic_call_function_procedure
    from functions.utils.utils import error_message,is_called_fuction_procedure, is_declared_variable, is_same_type, error_message
    if is_declared_variable(tokens,i,variables):
        variable_to_assign = variables[tokens[i][1]]
        index_variable_to_assign = i
        total_nums_to_assign = []
        total_strings_to_assign = []
        total_operators = []
        parameters_input = []
        is_int_assignments = False
        is_string_assignments = False
        i += 2
        while tokens[i][0] != 'FIN_DE_INSTRUCCION':
            if is_called_fuction_procedure(tokens,i):
                function_name= tokens[i][1]
                keys_functions = principal.functions.keys()
                if function_name in keys_functions:
                    if principal.functions[function_name].data_type == variable_to_assign[0]:
                        i += 2
                        while tokens[i][0] != 'PARENTESIS_DER':
                            if tokens[i][0] == 'IDENTIFICADOR':
                                if is_declared_variable(tokens,i,variables):
                                    parameters_input.append(variables.get(tokens[i][1]))
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
                        variables[tokens[index_variable_to_assign][1]][1] = principal.functions[function_name].return_data
                        i += 1
                        parameters_input = []
                    else:
                        return f"Error: La variable: '{variable_to_assign[1]}' no es del mismo tipo que la funcion {function_name} "
            elif is_read(tokens,i):
                self.on_comand_line()
                event_loop = QEventLoop()
                self.command_line.returnPressed.connect(event_loop.quit)
                event_loop.exec_()
                result = self.comand_text
                self.off_comand_line()
                if variable_to_assign[0] == 'ENTERO':
                    if result.isdigit() or (result[0]== '-' and result[1:].isdigit()):
                        result = int(result)
                        variables[tokens[index_variable_to_assign][1]][1] = result
                    else:
                        return f"Error: La variable: '{variable_to_assign[1]}' de tipo '{variable_to_assign[0]}' no coincide con {result} "
                elif variable_to_assign[0] == 'FLOTANTE':
                    if result.isdigit() or (result[0]== '-' and result[1:].isdigit()):
                        result = float(result)
                        variables[tokens[index_variable_to_assign][1]][1] = result
                    else:
                        return f"Error: La variable: '{variable_to_assign[1]}' de tipo '{variable_to_assign[0]}' no coincide con {result} "
                elif variable_to_assign[0] == "CADENA":
                    variables[tokens[index_variable_to_assign][1]][1] = result
                elif variable_to_assign[0] == "CARACTER":
                    if result.len()==1:
                        variables[tokens[index_variable_to_assign][1]][1] = result
                    else:
                        return f"Error: La variable: '{variable_to_assign[1]}' de tipo '{variable_to_assign[0]}' solo permite un caracter "
                else:
                    return f"Error: La variable: '{variable_to_assign[1]}' no es del mismo tipo que la funcion que {result} "
                i += 1
            elif is_matrix_call(tokens,i):
                if tokens[i][1] in principal.matrix:
                    matrix_to_write = principal.matrix[tokens[i][1]]
                    matrix_list = matrix_to_write[1]
                    matrix_row_size = matrix_to_write[2]
                    matrix_column_size = matrix_to_write[3]
                    row:0
                    column:0
                    if tokens[i+1][1] in variables:
                        row = variables[tokens[i+1][1]][1]
                        if row <= int(matrix_row_size):
                            i+=1
                        else:
                            return f"Error semantico el indice {tokens[i+1][1]} o {tokens[i+2][1]} es mayor al tamaño de la matriz"
                    elif tokens[i+1][1].isdigit():
                        if int(tokens[i+1][1]) <= int(matrix_row_size):
                            row = int(tokens[i+1][1])
                            i+=1
                        else:
                            return f"Error semantico el indice {tokens[i+1][1]} o {tokens[i+2][1]} es mayor al tamaño de la matriz"
                    if tokens[i+1][1] in variables:
                        column = variables[tokens[i+1][1]][1]
                        if column <= int(matrix_column_size):
                            i+=1
                        else:
                            return f"Error semantico el indice {tokens[i+1][1]} o {tokens[i+2][1]} es mayor al tamaño de la matriz"
                    elif tokens[i+1][1].isdigit():
                        if int(tokens[i+1][1]) <= int(matrix_column_size):
                            column = int(tokens[i+1][1])
                            i+=1
                        else:
                            return f"Error semantico el indice {tokens[i+1][1]} o {tokens[i+2][1]} es mayor al tamaño de la matriz"
                    value = filtrar_por_fila_columna(matrix_list,row,column)
                    i+=1
                    if variable_to_assign[0] == 'ENTERO' or variable_to_assign[0] == 'FLOTANTE':
                        total_nums_to_assign.append(value)
                        is_int_assignments = True
                    elif variable_to_assign[0] == 'CADENA':
                        total_strings_to_assign.append(value)
                        is_string_assignments = True
                    else:
                        variable_to_assign[1] = value
            elif is_array_call(tokens,i):
                if tokens[i][1] in arrays:
                    array_size = arrays[tokens[i][1]]
                    if tokens[i+1][1] in variables:
                        variable_value = variables[tokens[i+1][1]]
                        if variable_value[1] <= int(array_size[2]):
                            if tokens[i+1][1].isdigit():
                                value = arrays[tokens[i][1]][1][tokens[i+1][1]]
                            else:
                                value = arrays[tokens[i][1]][1][variables[tokens[i+1][1]][1]]
                        else:
                            return f"Error semantico el indice {tokens[i+1][1]} es mayor al tamaño del arreglo"
                    elif tokens[i+1][1].isdigit():
                        if int(tokens[i+1][1]) <= int(array_size[2]):
                            value = arrays[tokens[i][1]][1][tokens[i+1][1]]
                        else:
                            return f"Error semantico el indice {tokens[i+1][1]} es mayor al tamaño del arreglo"
                if variable_to_assign[0] == 'ENTERO' or variable_to_assign[0] == 'FLOTANTE':
                    total_nums_to_assign.append(value)
                    is_int_assignments = True
                elif variable_to_assign[0] == 'CADENA':
                    total_strings_to_assign.append(value)
                    is_string_assignments = True
                else:
                    variable_to_assign[1] = value
                i+=2
            elif tokens[i][0] == 'IDENTIFICADOR':
                if tokens[i][1] in variables and not variables[tokens[i][1]][1] == None  and (is_same_type(variable_to_assign,tokens,i,variables) or variable_to_assign[0] == 'FLOTANTE' and  variables[tokens[i][1]][0] == 'ENTERO'):
                    if variable_to_assign[0] == 'ENTERO' or variable_to_assign[0] == 'FLOTANTE':
                        total_nums_to_assign.append(variables[tokens[i][1]][1])
                        is_int_assignments = True
                    else:
                        variable_to_assign[1] = tokens[i][1]
                    i += 1
                else:
                    return f"Error semantico en {error_message(tokens, i )}"
            elif tokens[i][0] == 'NUMERO_ENTERO':
                if variable_to_assign[0] == 'ENTERO' or variable_to_assign[0] == 'FLOTANTE':
                    total_nums_to_assign.append(tokens[i][1])
                    is_int_assignments = True
                    i += 1
            elif tokens[i][0] == 'NUMERO_FLOTANTE':
                if variable_to_assign[0] == 'FLOTANTE' :
                    total_nums_to_assign.append(tokens[i][1])
                    is_int_assignments = True
                    i += 1
            elif tokens[i][0] == 'VALOR_BOOLEANO':
                if variable_to_assign[0] == 'BOOLEANO':
                    variables[tokens[index_variable_to_assign][1]][1] = tokens[i][1]
                    i += 1
            elif tokens[i][0] == "OPERADOR_ARITMETICO" or tokens[i][0] == "PARENTESIS_IZQ" or tokens[i][0] == "PARENTESIS_DER":
                total_operators.append(tokens[i][1])
                i += 1
            elif tokens[i][0] == "VALOR_CARACTER":
                if variable_to_assign[0] == 'CARACTER':
                    variables[tokens[index_variable_to_assign][1]][1] = tokens[i][1]
                    i += 1
            elif tokens[i][0] == "CADENA_LITERAL":
                if variable_to_assign[0] == 'CADENA':
                    total_strings_to_assign.append(tokens[i][1])
                    is_string_assignments = True
                    i += 1
        if is_int_assignments:
            result = assign_nums_operation(total_operators,total_nums_to_assign)
            variables[tokens[index_variable_to_assign][1]][1] = result
        if is_string_assignments:
            result = assign_string_operation(total_operators,total_strings_to_assign)
            variables[tokens[index_variable_to_assign][1]][1] = result
    else:
        return f"{error_message(tokens, i )} no ha sido declarada "
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


def assign_nums_operation(total_operators, total_nums_to_assign):
    if not total_operators:
        return total_nums_to_assign[0] if total_nums_to_assign else 0

    # Realizar primero las multiplicaciones y divisiones
    i = 0
    while i < len(total_operators):
        if total_operators[i] == '*':
            total_nums_to_assign[i] *= total_nums_to_assign[i + 1]
            del total_operators[i]
            del total_nums_to_assign[i + 1]
        elif total_operators[i] == '/':
            total_nums_to_assign[i] /= total_nums_to_assign[i + 1]
            del total_operators[i]
            del total_nums_to_assign[i + 1]
        else:
            i += 1

    # Realizar luego las sumas y restas
    if not total_operators:  # Solo hay multiplicaciones y divisiones
        return total_nums_to_assign[0]

    if len(total_nums_to_assign) == 1 and total_operators[0] == '-':
        return -total_nums_to_assign[0]

    result = total_nums_to_assign[0]
    for i in range(len(total_operators)):
        if total_operators[i] == '+':
            result += total_nums_to_assign[i + 1]
        elif total_operators[i] == '-':
            result -= total_nums_to_assign[i + 1]

    return result
