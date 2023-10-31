import re
class LexicalAnalysisObj:
    def __init__(self, isError, message,tokens):
        self.isError = isError
        self.message = message
        self.tokens = tokens if tokens is not None else []
patterns = [
    (r'\n', 'SALTO_DE_LINEA'),  
    (r'FUNCION', 'FUNCION'),
    (r'PROCEDIMIENTO', 'PROCEDIMIENTO'),
    (r'INICIO', 'INICIO'),
    (r'PRINCIPAL', 'PRINCIPAL'),
    (r'DE', 'DE'),
    (r'ESCRIBIR', 'ESCRIBIR'),
    (r'LEER', 'LEER'),
    (r';', 'FIN_DE_INSTRUCCION'),
    (r'CUANDO', 'CUANDO'),
    (r'SINO', 'SINO'),
    (r'MIENTRAS', 'MIENTRAS'),
    (r'\$(.*?)\$', 'COMENTARIO'),
    (r'RETORNO', 'RETORNO'),
    (r'FIN', 'FIN'),
    (r'(ENTERO|BOOLEANO|FLOTANTE|CADENA|CARACTER)\[(\d+)\]\[(\d+)\]', 'TIPO_DATO_MATRIZ'),
    (r'(ENTERO|BOOLEANO|FLOTANTE|CADENA|CARACTER)\[(\d+)\]', 'TIPO_DATO_VECTOR'),
    (r'\[(\d+)\]', lambda match: ('INDICE', int(match.group(1)) if int(match.group(1)) > 0 else handle_error(match.group(1)))),
    (r'ENTERO|BOOLEANO|FLOTANTE|CADENA|CARACTER', 'TIPO_DATO'),
    (r'VERDADERO|FALSO','VALOR_BOOLEANO'),
    (r'[=!<>]', 'OPERADOR_COMPARACION'),
    (r'&', 'OPERADOR_LOGICO_AND'),
    (r'#', 'OPERADOR_LOGICO_OR'),
    (r'\(', 'PARENTESIS_IZQ'),
    (r'\)', 'PARENTESIS_DER'),
    (r'\"(.*?)\"', lambda match: ('CADENA_LITERAL', match.group(1))),
    (r"\'(.)'", 'VALOR_CARACTER'),
    (r'\:', 'ASIGNACION'),
    (r'[a-zA-Z_]\w*', 'IDENTIFICADOR'),
    (r'\d+\.\d+', 'NUMERO_FLOTANTE'),
    (r'\d+', 'NUMERO_ENTERO'),
    (r'[+\-*/]', 'OPERADOR_ARITMETICO'),
    (r'\.\.\.', 'RANGO'),
]

def lexical_analysis(code):
    while code:
        for pattern, token_type in patterns:
            match = re.match(pattern, code ,re.DOTALL)
            if match:
                if callable(token_type):
                    syntax_analysis_obj.tokens.append(token_type(match))
                else:
                    token = match.group()
                    if token_type == 'NUMERO_ENTERO':
                        token = int(token)  # Convertir a entero
                    elif token_type == 'NUMERO_FLOTANTE':
                        token = float(token)
                    
                    elif token_type == 'SALTO_DE_LINEA':
                        code = code[len(match.group()):].lstrip()
                        break
                syntax_analysis_obj.tokens.append((token_type, token))
                code = code[len(match.group()):].lstrip()
                break
        else:
            syntax_analysis_obj.isError = True
            syntax_analysis_obj.message += (f"No se pudo analizar el token en: {code[:10]}")
            break
    return syntax_analysis_obj
def handle_error(index_value):
    syntax_analysis_obj.isError = True
    syntax_analysis_obj.message += f"No se puede acceder a un índice 0 o menor:  {index_value} \n"
    return 'ERROR_INDICE'

syntax_analysis_obj = LexicalAnalysisObj(False, "", [])