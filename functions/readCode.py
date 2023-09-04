from functions.verifyVariables import verify_variables
def verify_syntax(code):
    lines = code.split(';')
    return verify_variables(lines)