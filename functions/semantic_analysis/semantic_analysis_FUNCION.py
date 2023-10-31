from functions.semantic_analysis.semantic_analysis_write import semantic_analysis_write
from functions.semantic_analysis.sementic_analysis_array_assignments import sementic_analysis_array_assignments
from functions.utils.utils import is_array_assignment, is_return, is_write
def semantic_analysis_FUNCION(principal,i,tokens):
    from functions.semantic_analysis.semantic_analysis_MIENTRAS import semantic_analysis_MIENTRAS
    from functions.utils.global_state import Function
    from functions.semantic_analysis.semantic_analysis_CUANDO import semantic_analysis_CUANDO
    from functions.semantic_analysis.semantic_analysis_DE import semantic_analysis_DE
    from functions.semantic_analysis.semantic_analysis_assignments import semantic_analysis_assigments
    from functions.utils.utils import error_message, is_assignment, is_for, is_if, is_parameters_declaration, is_while
    init_funtion = i
    function = Function(tokens[i][1],tokens[i+2][1])
    i = i + 4
    while tokens[i][0] != 'PARENTESIS_DER':
        if is_parameters_declaration(tokens,i):
            function.parameters[tokens[i+1][1]] = [tokens[i][1],None]
            i += 2
        else:
            return f"Error semantico en {error_message(tokens, i )}"
    i += 2
    function.init_function = i
    variables = principal.variables.copy()
    variables.update(function.parameters)
    while not tokens[i][0] == 'FIN':
        if is_assignment(tokens,i):
            message = semantic_analysis_assigments(principal,variables,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
        if is_array_assignment(tokens,i):
            message = sementic_analysis_array_assignments(principal,principal.arrays,variables,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
        elif is_write(tokens,i):
            message = semantic_analysis_write(variables,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
        elif is_for(tokens,i):
            i += 1
            message = semantic_analysis_DE(principal,variables,i,tokens)
            if not message.isdigit():
                    return message
            i = int(message)
        elif is_while(tokens,i):
            i += 1
            message = semantic_analysis_MIENTRAS(principal,variables,i,tokens)
            if not message.isdigit():
                    return message
            i = int(message)
        elif is_if(tokens,i):
            i += 1
            message = semantic_analysis_CUANDO(principal,variables,i,tokens)
            if not message.isdigit():
                    return message
            i = int(message)
        elif is_return(tokens,i):
            i += 1
            if tokens[i][0] == 'IDENTIFICADOR':
                if tokens[i][1] in variables:
                    if not variables[tokens[i][1]][0] == function.data_type:
                        return f"Error semantico en {error_message(tokens, i )}"
                else:
                    return f"Error semantico en {error_message(tokens, i )}"
            elif tokens[i][0] in ['NUMERO_ENTERO','NUMERO_FLOTANTE','CADENA']:
                if  not tokens[i][0] == 'NUMERO_ENTERO' and function.data_type == 'ENTERO' or function.data_type == 'FLOTANTE':
                    return f"Error semantico en {error_message(tokens, i )}"
                elif not tokens[i][0] == 'NUMERO_FLOTANTE' and function.data_type == 'FLOTANTE':
                    return f"Error semantico en {error_message(tokens, i )}"
                elif not tokens[i][0] == 'VALOR_CARACTER' and function.data_type == 'CARARCTER':
                    return f"Error semantico en {error_message(tokens, i )}"
                elif not tokens[i][0] == 'CADENA_LITERAL' and function.data_type == 'CADENA':
                    return f"Error semantico en {error_message(tokens, i )}"
                elif not tokens[i][0] == 'VALOR_BOOLEANO' and function.data_type == 'BOOLEANO':
                    return f"Error semantico en {error_message(tokens, i )}"
            else:
                return f"Error semantico en {error_message(tokens, i )}"
            i += 2
    end_function = i
    function.end_functio = end_function
    principal.functions[function.identifier] = function
    return str(i+1)
