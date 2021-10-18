from itertools import combinations

with open("C:\\Advent\\2015\\day17.txt", 'r') as file:
    data = [int(x) for x in file.read().splitlines()]
    comb = sum([[x for x in combinations(data, i) if sum(x) == 150] for i in range(1, len(data)+1)], [])
    print(len(comb))
    min_comb = [x for x in combinations(data, len(comb[0])) if sum(x) == 150]
    print(len(min_comb))
