def filter_values_2(line):
    if any([line[x:].count(line[x:][:2]) >= 2 and line[x+2:].count(line[x:][:2]) >= 1 for x in range(len(line)-2)]):
        if any([line[x] == line[x+2] for x in range(len(line)-2)]):
            return True
    
def filter_values(line):
    if sum([line.count(x) for x in ['a','e','i','o','u']]) >= 3:
        if any([x*2 in line for x in line]):
            if not any([x in line for x in ['ab', 'cd', 'pq', 'xy']]):
                return True

with open('C:\\Users\\dider\\AppData\\Local\\Programs\\Python\\Python39\\AoC 2015\\input\\day5.txt', 'r') as file:
    data = file.read().splitlines()
    print('Part 1: {}'.format(len(list(filter(lambda line: filter_values(line), data)))))
    print('Part 2: {}'.format(len(list(filter(lambda line: filter_values_2(line), data)))))
