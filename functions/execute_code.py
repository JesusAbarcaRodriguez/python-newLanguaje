from functions.executable_code.verify_PRINCIPAL import verify_PRINCIPAL
from functions.lexical_analysis.lexical_analysis import LexicalAnalysisObj, lexical_analysis
from functions.semantic_analysis.semantic_analysis import semantic_analysis
from functions.syntactic_analysis.syntactic_analysis import syntactic_analysis
from functions.utils.global_state import Principal
from functions.utils.utils import is_main_procedure

def execute_code(self,code):
    syntax_analysis_obj =  LexicalAnalysisObj(False,"",[])
    syntax_analysis_obj = lexical_analysis(code)
    message = ""
    principal = Principal()
    principal.clear_all_data()
    if syntax_analysis_obj.isError:
        return syntax_analysis_obj.message
    else:
        message = syntactic_analysis(syntax_analysis_obj.tokens)
    if message == "Analisis sintactico correcto":
        message = semantic_analysis(syntax_analysis_obj.tokens,principal)
    if message == "Analisis semantico exitoso":
        tokens = syntax_analysis_obj.tokens 
        i = principal.init_principal
        if is_main_procedure(tokens,i):
            message = verify_PRINCIPAL(self,principal,i,tokens)
            if not message.isdigit():
                return message
            i = int(message)
    
    return message