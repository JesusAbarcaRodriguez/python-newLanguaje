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

def is_same_type(variable_to_assign,tokens,i,principal):
    if variable_to_assign[0]  == principal.variables[tokens[i][1]][0]:
        return True
    else:
        return False
def is_declared_variable(tokens,i,principal):
    if tokens[i][1] in principal.variables:
        return True
    else:
        return False