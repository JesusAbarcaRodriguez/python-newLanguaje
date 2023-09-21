import re
class LexicalAnalysisObj:
    def __init__(self, isError, message,tokens):
        self.isError = isError
        self.message = message
        self.tokens = tokens if tokens is not None else []
patterns = [
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
    (r'ENTERO|BOOLEANO |FLOTANTE|CADENA|CARACTER', 'TIPO_DATO'),
    (r'VERDADERO|FALSO','VALOR_BOOLEANO'),
    (r'[+\-*/]', 'OPERADOR_ARITMETICO'),
    (r'[=!<>]', 'OPERADOR_COMPARACION'),
    (r'&', 'OPERADOR_LOGICO_AND'),
    (r'#', 'OPERADOR_LOGICO_OR'),
    (r'\(', 'PARENTESIS_IZQ'),
    (r'\)', 'PARENTESIS_DER'),
    (r'\"(.*?)\"', 'CADENA_LITERAL'),
    (r"\'(.)'", 'VALOR_CARACTER'),
    (r'\:', 'ASIGNACION'),
    (r'[a-zA-Z_]\w*', 'IDENTIFICADOR'),
    (r'\d+\.\d+', 'NUMERO_FLOTANTE'),
    (r'\d+', 'NUMERO_ENTERO'),
    (r'\.\.\.', 'RANGO'),
]

def lexical_analysis(code):
    syntax_analysis_obj = LexicalAnalysisObj(False,"",[])
    while code:
        for pattern, token_type in patterns:
            match = re.match(pattern, code)
            if match:
                token = match.group()
                if token_type != 'COMENTARIO':
                    syntax_analysis_obj.tokens.append((token_type, token))
                code = code[len(token):].lstrip()
                break
        else:
            syntax_analysis_obj.isError = True
            syntax_analysis_obj.message += (f"No se pudo analizar el token en: {code}")
            break
    return syntax_analysis_obj