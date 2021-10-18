with open("C:\\Advent\\2015\\day19.txt", 'r') as file:
    data = [x for x in file.read().splitlines() if x]
    molecule = data[-1]
    solutions, reversed_solutions = {}, {}
    for x in data[:-1]:
        what, to = x.split(' => ')
        if what not in solutions:
            solutions[what] = []
        solutions[what].append(to)
        reversed_solutions[to] = what

    total = set()
    max_len = max(len(x) for x in solutions.keys())

    for e, x in enumerate(molecule):
        if x in solutions.keys():
            for y in solutions[x]:
                total.add('{}{}{}'.format(molecule[:e], y, molecule[e+1:]))
        elif e < len(molecule)-1 and x + molecule[e+1] in solutions.keys():
            for y in solutions[x + molecule[e+1]]:
                total.add('{}{}{}'.format(molecule[:e], y, molecule[e+2:]))

    print(len(total))

    print(sum(molecule.count(x) for x in solutions.keys()) - molecule.count('Y') - 1)
