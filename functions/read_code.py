from functions.syntactic_analysis.syntactic_analysis import syntactic_analysis
from functions.syntax_analysis.syntax_analysis import SyntaxAnalysisObj, syntax_analysis
def read_code(code):
    syntax_analysis_obj =  SyntaxAnalysisObj(False,"")
    syntax_analysis_obj = syntax_analysis(code)
    if syntax_analysis_obj.isError:
        return syntax_analysis_obj.message
    else:
        return syntactic_analysis(code)