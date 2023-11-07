
def semantic_analysis_PROCEDIMENTO(principal,i,tokens):
    from functions.utils.global_state import Procedimento
    from functions.utils.utils import  error_message, is_parameters_declaration
    from functions.utils.traverse_structure import traverse_structure
    procedimento = Procedimento()
    procedimento.identifier = tokens[i+1][1]
    i = i + 3
    while tokens[i][0] != 'PARENTESIS_DER':
        if is_parameters_declaration(tokens,i):
            procedimento.parameters[tokens[i+1][1]] = [tokens[i][1],None]
            i += 2
        else:
            return f"Error semantico en {error_message(tokens, i )}"
    i += 2
    procedimento.init_function = i
    variables = principal.variables.copy()
    variables.update(procedimento.parameters)
    message = traverse_structure(principal,variables,i,tokens)
    if not message.isdigit():
        return message
    i = int(message)
    end_function = i
    procedimento.end_function = end_function
    principal.procedures[procedimento.identifier] = procedimento
    return str(i)
