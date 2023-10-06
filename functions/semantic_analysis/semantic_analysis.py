def semantic_analysis(self,tokens):
    from functions.utils.utils import is_procedure_decalaration
    from functions.semantic_analysis.semantic_analysis_PRINCIPAL import semantic_analysis_PRINCIPAL
    from functions.semantic_analysis.semantic_analysis_FUNCION import semantic_analysis_FUNCION
    from functions.utils.global_state import  Principal
    from functions.semantic_analysis.semantic_analysis_PROCEDIMIENTO import semantic_analysis_PROCEDIMENTO
    from functions.utils.utils import is_main_procedure, is_function_declaration, is_variable_declaration
    principal = Principal()
    principal.clear_all_data()
    i = 0
    while i < len(tokens):
        if is_variable_declaration(tokens,i):
            if principal.variables.get(tokens[i+1][1]) == None:
                principal.variables[tokens[i+1][1]] = [tokens[i][1],None]
                i += 3
            else:
                return f"Error semantico la variable {tokens[i+1][1]} ya esta declarada"
        elif is_function_declaration(tokens,i):
            message = semantic_analysis_FUNCION(principal,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
        elif is_procedure_decalaration(tokens,i):
            message = semantic_analysis_PROCEDIMENTO(principal,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
        elif is_main_procedure(tokens,i):
            message = semantic_analysis_PRINCIPAL(self,principal,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
    return "Analisis semantico exitoso"




