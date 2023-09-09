from functions.sintax_analysis.sintax_analysis import syntax_analysis
def read_code(code):
    #lines = code.split('FIN')
    return  syntax_analysis(code)