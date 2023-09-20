def verify_PRINCIPAL(principal,i,tokens):
    from functions.semantic_analysis.traverse_structure.traverse_structure import traverse_structure

    i += 3
    message = traverse_structure(principal,i,tokens)
    if not message.isdigit():
        return message
    i = int(message)

    return str(i)
