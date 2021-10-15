def find_fastest(lst, total):
    trials = [k for k in conns.keys() if k not in lst]
    for k in trials:
        find_fastest(lst + [k], total + conns[lst[-1]][k])
    if not trials and len(lst) == len(conns.keys()):
        routes[tuple(lst)] = total

with open("C:\\Advent\\2015\\day9.txt", 'r') as file:
    data = [[x.split(' ')[y] for y in [0,2,4]] for x in file.read().splitlines()]
    conns, routes = dict({x[0] : {} for x in data}, **{x[1] : {} for x in data}), {}
    for a,b,c in data:
        conns[a][b] = conns[b][a] = int(c)

    for x in conns.keys():
        find_fastest([x], 0)

    print(min(routes.values()))
    print(max(routes.values()))
