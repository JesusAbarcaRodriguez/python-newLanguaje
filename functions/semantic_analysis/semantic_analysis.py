from functions.semantic_analysis.semantic_objcs import Function, Principal
def semantic_analysis(tokens):
    principal = Principal()
    countINICIO = 0
    countFIN = 0
    i = 0
    while i < len(tokens):
        if is_variable_declaration(tokens,i):
            principal.variables[tokens[i+1][1]] = [tokens[i][1],None]
            i += 3
        elif is_function_declaration(tokens,i):
            function = Function([],tokens[i][1],tokens[i+2][1])
            i = i + 4
            while tokens[i][0] != 'PARENTESIS_DER':
                if is_parameters_declaration(tokens,i):
                    function.parameters.append([tokens[i+1][1],tokens[i][1]])
                    i += 2
                else:
                    return f"Error semantico en {tokens[i][1]}"
            i += 2
            countINICIO += 1
            while not countFIN == countINICIO:
                if is_assignment(tokens,i):
                    if is_declared_variable(tokens,i,principal):
                        variable_to_assign = principal.variables[tokens[i][1]]
                        variable_to_assigni += 2
                        while tokens[i][0] != 'FIN_DE_INSTRUCCION':
                            if tokens[i][0] == 'IDENTIFICADOR':
                                if tokens[i][1] in principal.variables and not principal.variables[tokens[i][1]][1] == None  and is_same_type(variable_to_assign,tokens,i,principal):
                                    tokenAuxType = principal.variables[tokens[i][1]][0]
                                    i += 1
                                else:
                                    return f"Error semantico en {tokens[i][1]}"
                            elif tokens[i][0] == 'NUMERO_ENTERO':
                                variable_to_assign[1]
                                if variable_to_assign[0] == 'ENTERO':
                                    principal.variables[tokens[i-2][1]][1] = tokens[i][1]
                                    i += 1
                    else:
                        return f"Error semantico en {tokens[i][1]}"
                if tokens[i][0] == 'INICIO':
                    countINICIO += 1
                if tokens[i][0] == 'FIN':
                    countFIN += 1
                i += 1
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
def is_declared_variable(tokens,i,principal):
    if tokens[i][1] in principal.variables:
        return True
    else:
        return False
def is_same_type(tokenAuxType,tokens,i,principal):
    if tokenAuxType == principal.variables[tokens[i][1]][0]:
        return True
    else:
        return False
