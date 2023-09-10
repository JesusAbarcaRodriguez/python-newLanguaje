from collections import deque
tokens_to_verify_identificador = {"TIPO_DATO", "FUNCION", "CUANDO", "MIENTRAS", "DE","OPERADOR_COMPARACION","RANGO","OPERADOR_LOGICO_AND","OPERADOR_LOGICO_OR","OPERADOR_ARITMETICO"}
tokens_inicio_final ={"INCIO","FINAL"}
tokens_num_entero_flotante ={"NUMERO_ENTERO","NUMERO_FLOTANTE","IDENTIFICADOR"}
tokens_cadena_caracter = {"CADENA_LITERAL","CARACTER"}
def syntactic_analysis(tokens):
    pila_data_type= deque()
    pila_block= deque()
    pila_if_else= deque()
    for token in tokens:
        if token[0] == 'TIPO_DATO':
            pila_data_type.append(token)
        elif token[0] == 'IDENTIFICADOR':
            if top(pila_data_type)[0] in tokens_to_verify_identificador:
                pila_data_type.pop()
                pila_data_type.append(token)
        elif token[0] == 'FIN_DE_INSTRUCCION':
            if top(pila_data_type)[0] in tokens_num_entero_flotante or top(pila_data_type)[0] in tokens_cadena_caracter:
                pila_data_type.pop()
        elif token[0] == 'FUNCION':
            if top(pila_data_type)[0] == 'TIPO_DATO':
                pila_data_type.pop()
                pila_data_type.append(token)
        elif token[0] == 'PARENTESIS_IZQ':
            if top(pila_data_type)[0] == 'IDENTIFICADOR':
                pila_data_type.pop()
                pila_data_type.append(token)
        elif token[0] == 'PARENTESIS_DER':
            if top(pila_data_type)[0] == 'PARENTESIS_IZQ' or top(pila_data_type)[0] == 'IDENTIFICADOR':
                pila_data_type.pop()
                pila_data_type.append(token)
        elif token[0] == 'INICIO':
            if top(pila_data_type)[0] == 'PARENTESIS_DER' or top(pila_data_type)[0] in tokens_num_entero_flotante:
                pila_block.append(token)
                pila_data_type.pop()
        elif token[0] == 'FIN':
            top_block = top(pila_block)
            if top_block and top_block[0] == 'INICIO' or top(pila_data_type)[0] == 'FIN_DE_INSTRUCCION':
                if pila_data_type:
                    pila_data_type.pop()
                pila_block.append(token)
            else:
                pila_block.append(token)
        elif token[0] == 'CUANDO':
            if top(pila_block)[0] in tokens_inicio_final or top(pila_data_type)[0]:
                pila_if_else.append(token)
                pila_data_type.append(token)
        elif token[0] == 'OPERADOR_COMPARACION':
            if top(pila_data_type)[0] in tokens_num_entero_flotante:
                pila_data_type.pop()
                pila_data_type.append(token)
        elif token[0] == 'SINO':
            if top(pila_if_else)[0] == 'CUANDO':
                pila_if_else.pop()
                
        elif token[0] == 'MIENTRAS':
            if top(pila_block)[0] in tokens_inicio_final or top(pila_data_type)[0] == 'FIN_DE_INSTRUCCION':
                pila_data_type.clear()
                pila_data_type.append(token)
        
        elif token[0] == 'RANGO':
            if top(pila_data_type)[0] in tokens_num_entero_flotante:
                pila_data_type.pop()
                pila_data_type.append(token)
        elif token[0] == 'DE':
            if top(pila_block)[0] in tokens_inicio_final or top(pila_data_type)[0] == 'FIN_DE_INSTRUCCION':
                pila_data_type.clear()
                pila_data_type.append(token)        
        else:
            return "Error sintactico"
    return "Codigo correcto"    
    
def top(pila):
    if not pila:
        return (r' ', ' ')  # Devuelve None si la pila está vacía
    return pila[-1]  # Devuelve el último elemento de la pila
