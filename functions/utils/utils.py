def is_while(tokens,i):
    if tokens[i][0] == 'MIENTRAS':
        return True
    else:
        return False
def is_if(tokens,i):
    if tokens[i][0] == 'CUANDO':
        return True
    else:
        return False
def is_called_fuction_procedure(tokens,i):
    if tokens[i][0] == 'IDENTIFICADOR' and tokens[i+1][0] == 'PARENTESIS_IZQ':
        return True
    return False
def is_for(tokens,i):
    if tokens[i][0] == 'DE':
        return True
    return False
def is_variable_declaration(tokens,i):
    if tokens[i][0] == 'TIPO_DATO' and tokens[i+1][0] == 'IDENTIFICADOR':
        return True
    else:
        return False
def is_array_declaration(tokens,i):
    if tokens[i][0] == 'TIPO_DATO_VECTOR' and tokens[i+1][0] == 'IDENTIFICADOR':
        return True
    else:
        return False
def is_matrix_declaration(tokens,i):
    if tokens[i][0] == 'TIPO_DATO_MATRIZ' and tokens[i+1][0] == 'IDENTIFICADOR':
        return True
    else:
        return False
def is_function_declaration(tokens,i):
    if tokens[i][0] == 'TIPO_DATO' and tokens[i+1][0] == 'FUNCION':
        return True
    else:
        return False
def is_procedure_decalaration(tokens,i):
    if tokens[i][0] == 'PROCEDIMIENTO' and tokens[i+1][0] == 'IDENTIFICADOR':
        return True
    else:
        return False
def is_main_procedure(tokens,i):
    if tokens[i][0] == 'PROCEDIMIENTO' and tokens[i+1][0] == 'PRINCIPAL':
        return True
    else:
        return False
def is_parameters_declaration(tokens,i):
    if tokens[i][0] == 'TIPO_DATO' and tokens[i+1][0] == 'IDENTIFICADOR':
        return True
    else:
        return False
def is_return(tokens,i):
    if tokens[i][0] == 'RETORNO':
        return True
    else:
        return False
def is_assignment(tokens,i):
    if tokens[i][0] == 'IDENTIFICADOR' and tokens[i+1][0] == 'ASIGNACION':
        return True
    else:
        return False
def is_array_assignment(tokens,i):
    if tokens[i][0] == 'IDENTIFICADOR' and tokens[i+1][0] =='INDICE' and tokens[i+2][0] == 'ASIGNACION':
        return True
    else:
        return False
def is_matrix_assignment(tokens,i):
    if tokens[i][0] == 'IDENTIFICADOR' and tokens[i+1][0] =='INDICE' and tokens[i+2][0] == 'INDICE' and tokens[i+3][0] == 'ASIGNACION':
        return True
    else:
        return False
def is_read(tokens,i):
    if tokens[i][0] == 'LEER' and tokens[i+1][0] == 'FIN_DE_INSTRUCCION':
        return True
    else:
        return False
def is_write(tokens,i):
    if tokens[i][0] == 'ESCRIBIR' and tokens[i+1][0] == 'PARENTESIS_IZQ':
        return True
    else:
        return False
def is_same_type(variable_to_assign,tokens,i,variables):
    if variable_to_assign[0]  == variables[tokens[i][1]][0]:
        return True
    else:
        return False
def is_same_expression_type(token1,token2):
    if token1[0] == token2[0]:
        return True
    else:
        return False
def is_declared_variable(tokens,i,variables):
    if tokens[i][1] in variables:
        return True
    else:
        return False
def is_declarate_array(tokens,i,arrays):
    if tokens[i][1] in arrays:
        return True
    else:
        return False
def is_declarate_matrix(tokens,i,matrix):
    if tokens[i][1] in matrix:
        return True
    else:
        return False