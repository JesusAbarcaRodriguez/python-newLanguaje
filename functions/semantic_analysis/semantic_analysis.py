def semantic_analysis(tokens):
    from functions.utils.utils import is_procedure_decalaration
    from functions.semantic_analysis.semantic_analysis_PRINCIPAL import verify_PRINCIPAL
    from functions.semantic_analysis.semantic_analysis_FUNCION import verify_FUNCION
    from functions.semantic_analysis.semantic_objcs import  Principal
    from functions.semantic_analysis.semantic_analysis_PROCEDIMIENTO import verify_PROCEDIMENTO
    from functions.utils.utils import is_main_procedure, is_function_declaration, is_variable_declaration

    principal = Principal()
    i = 0
    while i < len(tokens):
        if is_variable_declaration(tokens,i):
            if principal.variables.get(tokens[i+1][1]) == None:
                principal.variables[tokens[i+1][1]] = [tokens[i][1],None]
                i += 3
            else:
                return f"Error semantico la variable {tokens[i+1][1]} ya esta declarada"
        elif is_function_declaration(tokens,i):
            message = verify_FUNCION(principal,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
        elif is_procedure_decalaration(tokens,i):
            message = verify_PROCEDIMENTO(principal,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
        elif is_main_procedure(tokens,i):
            message = verify_PRINCIPAL(principal,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
            
    return "Analisis semantico exitoso"




