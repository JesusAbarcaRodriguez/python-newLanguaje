def verify_write(variables,i,tokens):
    from main import write_variables
    i+=2
    text = ""

    while tokens[i][0] != 'PARENTESIS_DER':
        if tokens[i][0] == "IDENTIFICADOR":
            if tokens[i][0] in variables:
                text = text + variables[tokens[i][1]][0]
                i+=1
        elif tokens[i][0] == "CADENA_LITERAL" or tokens[i][0] == "VALOR_CARACTER" or tokens[i][0] == "NUMERO_ENTERO" or tokens[i][0] == "NUMERO_FLOTANTE" :
            text = text + tokens[i][1]
            i+=1
        else:
            return f"Error semantico en {tokens[i][1]}"
    write_variables(text)
    return i+2