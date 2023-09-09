import re


# Definir las expresiones regulares para los tokens
patterns = [
    (r'FUNCION', 'FUNCION'),
    (r'PROCEDIMIENTO', 'PROCEDIMIENTO'),
    (r'INICIO', 'INICIO'),
    (r'DE', 'DE'),
    (r'ESCRIBIR', 'ESCRIBIR'),
    (r'LEER', 'LEER'),
    (r';', 'FIN_DE_INSTRUCCION'),
    (r'CUANDO', 'CUANDO'),
    (r'MIENTRAS', 'MIENTRAS'),
    (r'\$(.*?)\$', 'COMENTARIO'),
    (r'FIN', 'FIN'),
    (r'ENTERO|BOOLEANO |FLOTANTE|CADENA|CARACTER', 'TIPO_DATO'),
    (r'[+\-*/]', 'OPERADOR_ARITMETICO'),
    (r'[=!<>]', 'OPERADOR_COMPARACION'),
    (r'&', 'OPERADOR_LOGICO_AND'),
    (r'#', 'OPERADOR_LOGICO_OR'),
    (r'\(', 'PARENTESIS_IZQ'),
    (r'\)', 'PARENTESIS_DER'),
    (r'\"(.*?)\"', 'CADENA_LITERAL'),  # Cadenas literales
    (r"\'(.)'", 'CARACTER'),
    (r'\:', 'ASIGNACION'),
    (r'[a-zA-Z_]\w*', 'IDENTIFICADOR'),
    (r'\d+\.\d+', 'NUMERO_FLOTANTE'),
    (r'\d+', 'NUMERO_ENTERO'),
]

def syntax_analysis(code):
    print("Syntax analysis")
    tokens = []
    while code:
        for pattern, token_type in patterns:
            match = re.match(pattern, code)
            if match:
                token = match.group()
                if token_type != 'COMENTARIO':
                    tokens.append((token_type, token))
                code = code[len(token):].lstrip()
                break
        else:
            print(tokens)
            print(f"ERROR: {code}")
            raise ValueError(f"No se pudo analizar el token en: {code}")
    return "COMPILACION EXITOSA"