from collections import deque
tokens_to_verify_identificador = {"RETORNO","TIPO_DATO", "FUNCION", "CUANDO", "MIENTRAS", "DE","OPERADOR_COMPARACION","RANGO","OPERADOR_LOGICO_AND","OPERADOR_LOGICO_OR","OPERADOR_ARITMETICO","INICIO","ASIGNACION","FIN_DE_INSTRUCCION", "PARENTESIS_IZQ", "IDENTIFICADOR"}
tokens_inicio_final ={"INICIO","FIN"}
tokens_to_verify_num = {'ASIGNACION','NUMERO_ENTERO', "PARENTESIS_IZQ", 'RANGO' , 'DE' , 'CUANDO','MIENTRAS','OPERADOR_LOGICO_AND','OPERADOR_LOGICO_OR','OPERADOR_ARITMETICO','OPERADOR_COMPARACION'}
tokens_num_entero_flotante ={"NUMERO_ENTERO","NUMERO_FLOTANTE","IDENTIFICADOR"}
tokens_cadena_caracter = {"CADENA_LITERAL","VALOR_CARACTER"}
tokens_data = {"NUMERO_ENTERO","NUMERO_FLOTANTE","CADENA_LITERAL","VALOR_CARACTER","VALOR_BOOLEANO"}
def syntactic_analysis(tokens):
    pila_data_type= deque()
    pila_block= deque()
    pila_if_else= deque()
    pila_verify_inicio_fin = deque()
    flag = False
    for token in tokens:
        if token[0] == 'TIPO_DATO':
            pila_data_type.append(token)
        elif token[0] == 'IDENTIFICADOR':
            if top(pila_data_type)[0] in tokens_to_verify_identificador:
                pila_data_type.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        elif token[0] == 'LEER':
            if top(pila_data_type)[0] == 'FIN_DE_INSTRUCCION' or top(pila_data_type)[0] == 'INICIO' or top(pila_data_type)[0] == 'FIN':
                pila_data_type.append(token)
        elif token[0] == 'ESCRIBIR':
            if top(pila_data_type)[0] == 'FIN_DE_INSTRUCCION' or top(pila_data_type)[0] == 'INICIO' or top(pila_data_type)[0] == 'FIN':
                pila_data_type.append(token)
        elif token[0] == 'RETORNO':
            if top(pila_data_type)[0] == 'FIN_DE_INSTRUCCION' or top(pila_data_type)[0] == 'FIN' or top(pila_data_type)[0] == 'INICIO':
                pila_data_type.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        elif token[0] == 'FIN_DE_INSTRUCCION':
            if top(pila_data_type)[0] in tokens_num_entero_flotante or top(pila_data_type)[0] in tokens_cadena_caracter or top(pila_data_type)[0] == 'PARENTESIS_DER':
                pila_data_type.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        elif token[0] == 'FUNCION':
            if top(pila_data_type)[0] == 'TIPO_DATO':
                pila_data_type.append(token)
                pila_verify_inicio_fin.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        elif token[0] == 'PARENTESIS_IZQ':
            if top(pila_data_type)[0] == 'IDENTIFICADOR' or top(pila_data_type)[0] == 'ESCRIBIR' or top(pila_data_type)[0] == 'LEER':
                pila_data_type.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        elif token[0] == 'PARENTESIS_DER':
            if top(pila_data_type)[0] in tokens_data or top(pila_data_type)[0] == 'PARENTESIS_IZQ' or top(pila_data_type)[0] == 'IDENTIFICADOR':
                pila_data_type.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        elif token[0] == 'INICIO':
            if top(pila_data_type)[0] == 'PARENTESIS_DER' or top(pila_data_type)[0] in tokens_num_entero_flotante or top(pila_data_type)[0] == 'SINO' or top(pila_data_type)[0] == 'PRINCIPAL' :
                pila_block.append(token)
                pila_data_type.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        elif token[0] == 'FIN':
            if  top(pila_block)[0] == 'RETORNO' or  top(pila_block)[0] == 'FIN' or top(pila_data_type)[0] == 'FIN_DE_INSTRUCCION':
                    pila_block.append(token)
                    pila_data_type.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        elif token[0] == 'CUANDO':
            if top(pila_block)[0] in tokens_inicio_final or top(pila_data_type)[0] or top(pila_block)[0] =='FIN_DE_INSTRUCCION':
                pila_if_else.append(token)
                pila_data_type.append(token)
                pila_verify_inicio_fin.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        elif token[0] == 'OPERADOR_COMPARACION':
            if top(pila_data_type)[0] in tokens_num_entero_flotante:
                pila_data_type.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        elif token[0] == 'SINO':
            if top(pila_data_type)[0] == 'FIN':
                pila_data_type.append(token)
                pila_verify_inicio_fin.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        elif token[0] == 'MIENTRAS':
            if top(pila_block)[0] in tokens_inicio_final or top(pila_data_type)[0] == 'FIN_DE_INSTRUCCION':
                pila_data_type.append(token)
                pila_verify_inicio_fin.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        elif token[0] == 'RANGO':
            if top(pila_data_type)[0] in tokens_num_entero_flotante:
                pila_data_type.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        elif token[0] == 'DE':
            if top(pila_block)[0] in tokens_inicio_final or top(pila_data_type)[0] == 'FIN_DE_INSTRUCCION':
                pila_data_type.append(token)
                pila_verify_inicio_fin.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        elif token[0] == 'OPERADOR_LOGICO_AND':
            if(top(pila_data_type)[0] in tokens_num_entero_flotante or top(pila_data_type)[0] in tokens_cadena_caracter):
                pila_data_type.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        elif token[0] == 'OPERADOR_LOGICO_OR':
            if(top(pila_data_type)[0] in tokens_num_entero_flotante or top(pila_data_type)[0] in tokens_cadena_caracter):
                pila_data_type.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        elif token[0] == 'OPERADOR_ARITMETICO':
            if(top(pila_data_type)[0] in tokens_num_entero_flotante or top(pila_data_type)[0] == "CADENA_LITERAL"):
                pila_data_type.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        elif token[0] == 'CADENA_LITERAL':
            if(top(pila_data_type)[0] == 'ASIGNACION') or top(pila_data_type)[0] == 'RETORNO' or top(pila_data_type)[0] == 'OPERADOR_ARITMETICO' or top(pila_data_type)[0] == "PARENTESIS_IZQ":
                pila_data_type.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        elif token[0] == 'VALOR_CARACTER':
            if(top(pila_data_type)[0] == 'ASIGNACION') or top(pila_data_type)[0] == 'RETORNO':
                pila_data_type.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        elif token[0] == 'VALOR_BOOLEANO':
            if(top(pila_data_type)[0] == 'ASIGNACION') or top(pila_data_type)[0] == 'RETORNO':
                pila_data_type.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        elif token[0] == 'ASIGNACION':
            if(top(pila_data_type)[0] == 'IDENTIFICADOR'):
                pila_data_type.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        elif token[0] == 'PROCEDIMIENTO':
                pila_data_type.append(token)
                pila_verify_inicio_fin.append(token)
        elif token[0] == 'TIPO_DATO_VECTOR':
                pila_data_type.append(token)
        elif token[0] == 'TIPO_DATO_MATRIZ':
            pila_data_type.append(token)
        elif token[0] == 'NUMERO_ENTERO':
            if(top(pila_data_type)[0]  in tokens_to_verify_num) or top(pila_data_type)[0] == 'RETORNO':
                pila_data_type.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        elif token[0] == 'PRINCIPAL':
            if(top(pila_data_type)[0] == 'PROCEDIMIENTO'):
                flag = True
                pila_data_type.append(token)
        elif token[0] == 'NUMERO_FLOTANTE':
            if(top(pila_data_type)[0] in tokens_to_verify_num) or top(pila_data_type)[0] == 'RETORNO':
                pila_data_type.append(token)
            else:
                return f"Error sintactico en {token[1]}"
        else:
            return "Error sintactico"
    pila_size_block = len(pila_block)//2
    pila_verify_inicio_fin_size = len(pila_verify_inicio_fin)
    if flag == False:
        return "Error sintactico, no se encontro el procedimiento principal"
    if pila_size_block != pila_verify_inicio_fin_size:
        return "Error sintactico en el inicio o final del bloque"
    count_inicio = pila_block.count(('INICIO', 'INICIO'))
    count_final = pila_block.count(('FIN', 'FIN'))
    count_de = pila_data_type.count(('DE', 'DE'))
    count_rango = pila_data_type.count(('RANGO', '...'))
    if count_de != count_rango:
        return "Error sintactico en la declaracion de DE y Rango"
    if count_inicio != count_final:
        return "Error sintactico en el inicio o final del bloque"
    return "Analisis sintactico correcto"
def top(pila):
    if not pila:
        return (r' ', ' ')  # Devuelve None si la pila está vacía
    return pila[-1]  # Devuelve el último elemento de la pila
