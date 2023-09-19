


def verify_PRINCIPAL(principal,i,tokens):
    from functions.semantic_analysis.semantic_objcs import Procedimento
    from functions.semantic_analysis.verify_CUANDO import verify_CUANDO
    from functions.semantic_analysis.verify_DE import verify_DE
    from functions.semantic_analysis.verify_MIENTRAS import verify_MIENTRAS
    from functions.semantic_analysis.verify_assignments import verify_assigments
    from functions.utils.utils import is_assignment, is_for, is_if, is_while
    i += 3
    countINICIO =0
    countFIN =0
    countINICIO += 1
    while not countFIN == countINICIO:
        if is_assignment(tokens,i):
            message = verify_assigments(principal.variables,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
        elif is_for(tokens,i):
            i += 1
            message = verify_DE(principal,i,tokens)
            if not message.isdigit():
                    return message
            i = int(message)
        elif is_while(tokens,i):
            i += 1
            message = verify_MIENTRAS(principal,i,tokens)
            if not message.isdigit():
                    return message
            i = int(message)
        elif is_if(tokens,i):
            i += 1
            message = verify_CUANDO(principal,i,tokens)
            if not message.isdigit():
                    return message
            i = int(message)
        if tokens[i][0] == 'FIN':
            countFIN += 1
    end_function = i
    return str(i+1)
