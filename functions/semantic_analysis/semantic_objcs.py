class Principal:
    functions = {}
    variables = {}
    data_int_matrix = {}
    data_char_matrix = {}
    data_float_matrix = {}
    data_string_matrix = {}
    data_bool_matrix = {}
    data_int_vector = {}
    data_char_vector = {}
    data_float_vector = {}
    data_string_vector = {}
    data_bool_vector = {}
    procedimiento = {}

class Function:
    parameters = {}
    data_type = ""
    identifier = ""
    init_function = 0
    end_function = 0
    return_data = None
    def __init__(self,data_type,identifier):
        self.data_type = data_type
        self.identifier = identifier

class Procedimento:
    parameters = []
    identifier = ""
    init_function = 0
    end_function = 0
    return_data = None
    def __init__(self,parameters,identifier):
        self.parameters = parameters
        self.identifier = identifier