from functions.semantic_analysis.sementic_analysis_matrix_assignments import sementic_analysis_matrix_assignments
from functions.utils.utils import is_matrix_assignment


def traverse_structure(principal,variables,i,tokens):
    from functions.semantic_analysis.sementic_analysis_array_assignments import sementic_analysis_array_assignments
    from functions.utils.utils import is_array_assignment, is_return
    from functions.semantic_analysis.semantic_analysis_write import semantic_analysis_write
    from functions.utils.utils import is_write
    from functions.semantic_analysis.semantic_analysis_CUANDO import semantic_analysis_CUANDO
    from functions.semantic_analysis.semantic_analysis_DE import semantic_analysis_DE
    from functions.semantic_analysis.semantic_analysis_MIENTRAS import semantic_analysis_MIENTRAS
    from functions.semantic_analysis.semantic_analysis_assignments import semantic_analysis_assigments
    from functions.utils.utils import is_assignment, is_for, is_if, is_while
    while not tokens[i][0] == 'FIN':
        if is_assignment(tokens,i):
            message = semantic_analysis_assigments(principal,variables,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
        elif is_array_assignment(tokens,i):
            message = sementic_analysis_array_assignments(principal,principal.arrays,variables,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
        elif is_matrix_assignment(tokens,i):
            message = sementic_analysis_matrix_assignments(principal,principal.matrix,variables,i,tokens)
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
        elif is_write(tokens,i):
            message = semantic_analysis_write(variables,principal.arrays,principal.matrix,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
        elif is_return(tokens,i):
            i += 3
    return str(i+1)