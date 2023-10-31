
def verify_write(self,variables,arrays,matrix,i,tokens):
    i+=2
    text = ""
    while tokens[i][0] != 'PARENTESIS_DER':
        if tokens[i][0] == "IDENTIFICADOR" and tokens[i+1][0] == "INDICE" and tokens[i+2][0] == "INDICE":
            if tokens[i][1] in matrix:
                matrix_to_write = matrix[tokens[i][1]]
                matrix_row_size = matrix_to_write[2]
                matrix_column_size = matrix_to_write[3]
                is_num_index = False
                row:0
                column:0
                if tokens[i+1][1] in variables:
                    row = variables[tokens[i+1][1]]
                    if row[1] <= int(matrix_row_size):
                        i+=1
                    else:
                        return f"Error semantico el indice {tokens[i+1][1]} o {tokens[i+2][1]} es mayor al tamaño de la matriz"
                elif tokens[i+1][1].isdigit():
                    if int(tokens[i+1][1]) <= int(matrix_row_size):
                        row = tokens[i+1][1]
                        is_num_index = True
                        i+=1
                    else:
                        return f"Error semantico el indice {tokens[i+1][1]} o {tokens[i+2][1]} es mayor al tamaño de la matriz"
                if tokens[i+1][1] in variables:
                    column = variables[tokens[i+1][1]]
                    if column[1] <= int(matrix_column_size):
                        i+=2
                    else:
                        return f"Error semantico el indice {tokens[i+1][1]} o {tokens[i+2][1]} es mayor al tamaño de la matriz"
                elif tokens[i+1][1].isdigit():
                    if int(tokens[i+1][1]) <= int(matrix_column_size):
                        column = tokens[i+1][1]
                        is_num_index = True
                        i+=2
                    else:
                        return f"Error semantico el indice {tokens[i+1][1]} o {tokens[i+2][1]} es mayor al tamaño de la matriz"
                if is_num_index:
                    value = matrix_to_write[1][0][0]
                else:
                    value = matrix_to_write[1][0]
                if isinstance(value, (int, float)):
                    text = text + str(value)
                elif value == "VERDADERO":
                    text = text + "VERDADERO"
                elif value == "FALSO":
                    text = text + "FALSO"
                else:
                    text = text + value
            else:
                return f"Error semantico la variable {error_message(tokens, i )} no esta declarada"
        elif tokens[i][0] == "IDENTIFICADOR" and tokens[i+1][0] == "INDICE":
            if tokens[i][1] in arrays:
                array_size = arrays[tokens[i][1]]
                if tokens[i+1][1] in variables:
                    variable_value = variables[tokens[i+1][1]]
                    if variable_value[1] <= int(array_size[2]):
                        value = arrays[tokens[i][1]][1][tokens[i+1][1]]
                        if not value == None:
                            if isinstance(value, (int, float)):
                                text = text + str(value)
                            elif value == "VERDADERO":
                                text = text + "VERDADERO"
                            elif value == "FALSO":
                                text = text + "FALSO"
                            else:
                                text = text + value
                            i+=2
                        else:
                            text = text + "NULO"
                    else:
                        return f"Error semantico el indice {tokens[i+1][1]} es mayor al tamaño del arreglo"
                elif tokens[i+1][1].isdigit():
                    if int(tokens[i+1][1]) <= int(array_size[2]):
                        value = arrays[tokens[i][1]][1][tokens[i+1][1]]
                        if isinstance(value, (int, float)):
                            text = text + str(value)
                        else:
                            text = text + value
                        i+=2
                    else:
                        return f"Error semantico el indice {tokens[i+1][1]} es mayor al tamaño del arreglo"
            else:
                return f"Error semantico la variable {error_message(tokens, i )} no esta declarada"
        elif tokens[i][0] == "IDENTIFICADOR":
            if tokens[i][1] in variables:
                value = variables[tokens[i][1]][1]
                if isinstance(value, (int, float)):
                    text = text + str(value)
                elif value == "VERDADERO":
                    text = text + "VERDADERO"
                elif value == "FALSO":
                    text = text + "FALSO"
                else:
                    text = text + value
                i+=1
            else:
                return f"Error semantico la variable {error_message(tokens, i )} no esta declarada"
        elif tokens[i][0] == "CADENA_LITERAL" or tokens[i][0] == "VALOR_CARACTER" or tokens[i][0] == "NUMERO_ENTERO" or tokens[i][0] == "NUMERO_FLOTANTE" :
            text = text + tokens[i][1]
            i+=1
        elif tokens[i][0] == "VALOR_BOOLEANO":
            if tokens[i][1] == "VERDADERO":
                text = text + "VERDADERO"
                i+=1
            elif tokens[i][1] == "FALSO":
                text = text + "FALSO"
                i+=1
        else:
            return f"Error semantico en {error_message(tokens, i )}"
    self.write_variables(text)
    return str(i+2)