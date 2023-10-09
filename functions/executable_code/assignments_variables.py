
from numbers import Number
from PyQt5.QtCore import QEventLoop

def verify_assigments(self,principal,variables,i,tokens):
    from functions.utils.utils import is_read
    from functions.executable_code.verify_FUNCION import verify_FUNCION
    from functions.semantic_analysis.semantic_call_function_procedure import semantic_call_function_procedure
    from functions.utils.utils import is_called_fuction_procedure, is_declared_variable, is_same_type
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
                        variables[tokens[index_variable_to_assign][1]][1] = principal.functions[function_name].return_data
                        i += 1
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
                    if result.isdigit():
                        result = int(result)
                        variables[tokens[index_variable_to_assign][1]][1] = result
                    else:
                        return f"Error: La variable: '{variable_to_assign[1]}' de tipo '{variable_to_assign[0]}' no coincide con {result} "
                elif variable_to_assign[0] == 'FLOTANTE':
                    if result.isdigit():
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

            elif tokens[i][0] == 'IDENTIFICADOR':
                if tokens[i][1] in variables and not variables[tokens[i][1]][1] == None  and (is_same_type(variable_to_assign,tokens,i,variables) or variable_to_assign[0] == 'FLOTANTE' and  variables[tokens[i][1]][0] == 'ENTERO'):
                    if variable_to_assign[0] == 'ENTERO' or variable_to_assign[0] == 'FLOTANTE':
                        total_nums_to_assign.append(variables[tokens[i][1]][1])
                        is_int_assignments = True
                    else:
                        variable_to_assign[1] = tokens[i][1]
                    i += 1
                else:
                    return f"Error semantico en {tokens[i][1]}"
            elif tokens[i][0] == 'NUMERO_ENTERO':
                if variable_to_assign[0] == 'ENTERO' or variable_to_assign[0] == 'FLOTANTE':
                    total_nums_to_assign.append(int(tokens[i][1]))
                    is_int_assignments = True
                    i += 1
            elif tokens[i][0] == 'NUMERO_FLOTANTE':
                if variable_to_assign[0] == 'FLOTANTE' :
                    total_nums_to_assign.append(int(tokens[i][1]))
                    is_int_assignments = True
                    i += 1
            elif tokens[i][0] == 'VALOR_BOOLEANO':
                if variable_to_assign[0] == 'BOOLEANO':
                    variables[tokens[index_variable_to_assign][1]][1] = tokens[i][1]
            elif tokens[i][0] == "OPERADOR_ARITMETICO" or tokens[i][0] == "PARENTESIS_IZQ" or tokens[i][0] == "PARENTESIS_DER":
                total_operators.append(tokens[i][1])
                i += 1
            elif tokens[i][0] == "CARACTER":
                if variable_to_assign[0] == 'CARACTER':
                    variables[tokens[index_variable_to_assign][1]][1] = tokens[i][1]
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