class Principal:
    functions = {}
    variables = {}
    procedures = {}
    arrays = {}
    matrix = {}
    init_principal = 0 
    print_data = []
    read_data = []
    def clear_all_data(self):
        self.functions = {}
        self.variables = {}
        self.arrays = {}
        self.matrix = {}
        self.procedures = {}
        self.print_data = []
        self.read_data ={}
class Function:
    parameters = {}
    data_type = ""
    identifier = ""
    init_function = 0
    end_function = 0
    return_data = None
    def __init__(self):
        self.parameters = {}
        self.data_type = ""
        self.identifier = ""
        self.init_function = 0
        self.end_function = 0
        self.return_data = None
class Procedimento:
    parameters = []
    identifier = ""
    init_function = 0
    end_function = 0
    return_data = None
    def __init__(self,parameters,identifier):
        self.parameters = parameters
        self.identifier = identifier