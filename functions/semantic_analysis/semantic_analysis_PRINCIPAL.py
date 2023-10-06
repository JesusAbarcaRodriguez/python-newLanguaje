def semantic_analysis_PRINCIPAL(self,principal,i,tokens):
    from functions.utils.traverse_structure_principal import traverse_structure_principal

    i += 3
    message = traverse_structure_principal(self,principal,i,tokens,principal.variables)
    if not message.isdigit():
        return message
    i = int(message)

    return str(i)
