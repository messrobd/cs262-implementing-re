def interpret(ast, current_state=1):
    edges = {}
    for ptree in ast:
        re_type = ptree[0]
        if re_type == 'character':
            edge = (current_state, ptree[1])
            destination = current_state + 1
            edges[edge] = destination
            current_state = destination
        elif re_type == 'multiplier':
            new_edges = []
            new_edges = None
    return edges
