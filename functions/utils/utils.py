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
def is_for(tokens,i):
    if tokens[i][0] == 'DE':
        return True
    else:
        return False
def is_variable_declaration(tokens,i):
    if tokens[i][0] == 'TIPO_DATO' and tokens[i+1][0] == 'IDENTIFICADOR':
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
def is_assignment(tokens,i):
    if tokens[i][0] == 'IDENTIFICADOR' and tokens[i+1][0] == 'ASIGNACION':
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