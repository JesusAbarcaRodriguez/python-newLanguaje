
def verify_write(self,variables,arrays,i,tokens):
    i+=2
    text = ""
    while tokens[i][0] != 'PARENTESIS_DER':
        if tokens[i][0] == "IDENTIFICADOR" and tokens[i+1][0] == "INDICE":
            if tokens[i][1] in arrays:
                value = arrays[tokens[i][1]][1][tokens[i+1][1]]
                if isinstance(value, (int, float)):
                    text = text + str(value)
                else:
                    text = text + value
                i+=2
            else:
                return f"Error semantico la variable {tokens[i][1]} no esta declarada"
        elif tokens[i][0] == "IDENTIFICADOR":
            if tokens[i][1] in variables:
                value = variables[tokens[i][1]][1]
                if isinstance(value, (int, float)):
                    text = text + str(value)
                else:
                    text = text + value
                i+=1
            else:
                return f"Error semantico la variable {tokens[i][1]} no esta declarada"
        elif tokens[i][0] == "CADENA_LITERAL" or tokens[i][0] == "VALOR_CARACTER" or tokens[i][0] == "NUMERO_ENTERO" or tokens[i][0] == "NUMERO_FLOTANTE" :
            text = text + tokens[i][1]
            i+=1
        else:
            return f"Error semantico en {tokens[i][1]}"
    self.write_variables(text)
    return str(i+2)