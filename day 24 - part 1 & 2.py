from itertools import combinations
from functools import reduce

def find_matches(data, lst=[], current=0, matches=[]):
    
    for x in data:
        if lst:
            if lst[-1] < x:
                temp = current + x
                if temp < weight_per_group:
                    matches = find_matches(data, lst[:]+[x], temp, matches)
                elif temp == weight_per_group:
                    matches.append(lst[:]+[x])
                else:
                    break
        else:
            find_matches(data, lst[:]+[x], x)
    return matches

    

with open("C:\\Advent\\2015\\day24.txt", 'r') as file:
    data = [int(x) for x in file.read().splitlines()]
    weight_per_group = sum(data)//3
    matches = []
    matches = set(tuple(x) for x in find_matches(data))
    final_matches = set()
    for x in matches:
        if tuple(x) in final_matches:
            continue
        second_matches = set(tuple(e) for e in find_matches([i for i in data if i not in x]))
        for y in second_matches:
            if y in final_matches:
                continue
            third_matches = set(tuple(e) for e in find_matches([i for i in data if i not in x and i not in y]))
            for z in third_matches:
                if z in final_matches:
                    continue
                final_matches.add(tuple(x))
                final_matches.add(y)
                final_matches.add(z)

    sort = sorted(final_matches, key=lambda x: (len(x), reduce(lambda y,z: y*z, x)))
    print(reduce(lambda y,z: y*z, sort[0]))

    weight_per_group = sum(data)//4
    matches = []
    matches = set(tuple(x) for x in find_matches(data))
    final_matches = set()
    for x in matches:
        if tuple(x) in final_matches:
            continue
        second_matches = set(tuple(e) for e in find_matches([i for i in data if i not in x]))
        for y in second_matches:
            if y in final_matches:
                continue
            third_matches = set(tuple(e) for e in find_matches([i for i in data if i not in x and i not in y]))
            for z in third_matches:
                if z in final_matches:
                    continue
                fourth_matches = set(tuple(e) for e in find_matches([i for i in data if i not in x and i not in y and i not in z]))
                for a in fourth_matches:
                    if a in final_matches:
                        continue
                    final_matches.add(tuple(x))
                    final_matches.add(y)
                    final_matches.add(z)
                    final_matches.add(a)
                    

    sort = sorted(final_matches, key=lambda x: (len(x), reduce(lambda y,z: y*z, x)))
    print(reduce(lambda y,z: y*z, sort[0]))
