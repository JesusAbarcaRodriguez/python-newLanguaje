import re
from functions.lexical_analysis.lexical_analysis import LexicalAnalysisObj, lexical_analysis
from functions.semantic_analysis.semantic_analysis import semantic_analysis
from functions.syntactic_analysis.syntactic_analysis import syntactic_analysis
from collections import deque
def compile_code(code):
    syntax_analysis_obj =  LexicalAnalysisObj(False,"",[])
    syntax_analysis_obj = lexical_analysis(code)
    if syntax_analysis_obj.isError:
        return syntax_analysis_obj.message
    else:
        message = syntactic_analysis(syntax_analysis_obj.tokens)
    if message == "Analisis sintactico correcto":
        return semantic_analysis(syntax_analysis_obj.tokens)
    else:
        return message