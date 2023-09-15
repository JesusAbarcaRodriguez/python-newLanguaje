from functions.semantic_analysis.semantic_objcs import Function, Principal
from functions.semantic_analysis.verify_CUANDO import verify_CUANDO
from functions.semantic_analysis.verify_DE import verify_DE
from functions.semantic_analysis.verify_assignments import verify_assigments
from functions.utils.utils import is_assignment, is_for, is_function_declaration, is_if, is_parameters_declaration, is_variable_declaration, is_while
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
                    message = verify_assigments(principal,i,tokens)
                    if not message.isdigit():
                        return message
                    i = int(message)
                elif is_for(tokens,i):
                    i += 1
                    verify_DE(principal,i,tokens)
                elif is_while(tokens,i):
                    i += 1
                elif is_if(tokens,i):
                    i += 1
                    verify_CUANDO(principal,i,tokens)
                if tokens[i][0] == 'INICIO':
                    countINICIO += 1
                if tokens[i][0] == 'FIN':
                    countFIN += 1
                i += 1


