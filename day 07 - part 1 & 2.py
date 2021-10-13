import operator

operators = {
    'AND'       : lambda source: int(source[0]) & int(source[1]),
    'OR'        : lambda source: int(source[0]) | int(source[1]),
    'LSHIFT'    : lambda source: int(source[0]) << int(source[1]),
    'RSHIFT'    : lambda source: int(source[0]) >> int(source[1]),
    'NOT'       : lambda source: ~int(source[0])
            }

def find_value(wire):
    if wire not in results:
        source = connections[wire]
        operator = next(iter(x for x in source if type(x) == str and x.isupper()), None)
        if operator:
            source.remove(operator)

        for e,x in enumerate(source):
            if type(x) == str and x.isalpha():
                source[e] = find_value(x)

        result = operators[operator](source) if operator else (find_value(source[0]) if type(source[0]) == str and source[0].isalpha() else source[0])
        results[wire] = result
    return results[wire]
        

with open("C:\\Advent\\2015\\day7.txt", 'r') as file:
    data = file.read().splitlines()
    connections, results = {}, {}

    for line in data:
        source, wire = line.split(' -> ')
        connections[wire] = source.split(' ')

    result = find_value('a')

    print(result)

    connections, results = {}, {}
    
    for line in data:
        source, wire = line.split(' -> ')
        connections[wire] = source.split(' ')

    connections['b'] = [str(result)]

    result = find_value('a')
    
    print(result)
