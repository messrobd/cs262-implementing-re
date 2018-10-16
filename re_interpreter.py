def edge(ast, current_state):
    re_type = ast[0]
    if re_type == 'character':
        return (current_state, ast[1]), current_state+1

def interpret(ast):
    edges = {}
    current_state = 1
    for ptree in ast:
        key, value = edge(ptree, current_state)
        edges[key] = value
        current_state += 1
    return edges
