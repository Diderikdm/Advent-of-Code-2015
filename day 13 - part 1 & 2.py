def find_matches(lst, total):
    trials = [k for k in matches.keys() if k not in lst]
    for k in trials:
        find_matches(lst + [k], total + matches[lst[-1]][k])
    if not trials and len(lst) == len(matches.keys()):
        all_matches[tuple(lst)] = total + matches[lst[0]][lst[-1]]
        

with open("C:\\Advent\\2015\\day13.txt", 'r') as file:
    data = [[x.strip('.').split(' ')[y] for y in [0,2,3,-1]] for x in file.read().splitlines()]
    conns, all_matches = {x[0]:{} for x in data}, {}
    for x in data:
        conns[x[0]][x[-1]] = int(x[2]) * (-1 if x[1] == 'lose' else 1)
    matches = {k:{x:conns[k][x] + conns[x][k] for x in v} for k,v in conns.items()}
    for k in matches.keys():
        find_matches([k], 0)
    print(max(all_matches.values()))

    conns['i'], all_matches = {}, {}
    for k in conns.keys():
        conns[k]['i'] = conns['i'][k] = 0
    matches = {k:{x:conns[k][x] + conns[x][k] for x in v} for k,v in conns.items()}
    for k in matches.keys():
        find_matches([k], 0)
    print(max(all_matches.values()))
