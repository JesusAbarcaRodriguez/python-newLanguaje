


def verify_PROCEDIMENTO(principal,i,tokens):
    from functions.semantic_analysis.semantic_objcs import Procedimento
    from functions.utils.utils import  is_parameters_declaration
    from functions.semantic_analysis.traverse_structure.traverse_structure import traverse_structure
    init_funtion = i
    procedimento = Procedimento([],tokens[i+2][1])
    procedimento.init_function = init_funtion
    i = i + 3
    while tokens[i][0] != 'PARENTESIS_DER':
        if is_parameters_declaration(tokens,i):
            procedimento.parameters[tokens[i+1][1]]([tokens[i+1][1],tokens[i][1]])
            i += 2
        else:
            return f"Error semantico en {tokens[i][1]}"
    i += 2
    countINICIO += 1
    message = traverse_structure(principal,i,tokens)
    if not message.isdigit():
        return message
    i = int(message)
    end_function = i
    procedimento.end_function = end_function
    principal.procedimiento[procedimento.name] = procedimento
    return str(i)
