def semantic_analysis_write(variables,i,tokens):
    i+=2
    text = ""
    while tokens[i][0] != 'PARENTESIS_DER':
        if tokens[i][0] == "IDENTIFICADOR":
            if not tokens[i][1] in variables:
                return f"Error semantico en {tokens[i][1] + ' no declarado'}"
            i+=1
        elif tokens[i][0] == "CADENA_LITERAL" or tokens[i][0] == "VALOR_CARACTER" or tokens[i][0] == "NUMERO_ENTERO" or tokens[i][0] == "NUMERO_FLOTANTE" :
            text = text + tokens[i][1]
            i+=1
        else:
            return f"Error semantico en {tokens[i][1]} + 'no se puede imprimir'"
    return i+2

