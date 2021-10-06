with open("C:\\Advent\\2015\\day6.txt", "r") as file:
    data = file.read().splitlines()
    a,b,c = 'turn on ', 'turn off ', 'toggle '
    refined_data = [{'operator' :   0 if x.startswith(a) else \
                                    1 if x.startswith(b) else \
                                    2,
                     'start'    :   [int(y) for y in x.strip(a).strip(b).strip(c).split(' through ')[0].split(',')],    
                     'end'      :   [int(y) for y in x.strip(a).strip(b).strip(c).split(' through ')[1].split(',')]}
                    for x in data]
    grid = [[-1 for x in range(1000)] for y in range(1000)]
    for command in refined_data:
        for y in range(command['start'][0], command['end'][0]+1):
            for x in range(command['start'][1], command['end'][1]+1):
                if command['operator'] == 0:
                    grid[y][x] = 1
                elif command['operator'] == 1:
                    grid[y][x] = -1
                else:
                    grid[y][x] *= -1

    count = 0
    for y in grid:
        for x in y:
            if x == 1:
                count += 1

    print(count)

    grid = [[0 for x in range(1000)] for y in range(1000)]
    for command in refined_data:
        for y in range(command['start'][0], command['end'][0]+1):
            for x in range(command['start'][1], command['end'][1]+1):
                if command['operator'] == 0:
                    grid[y][x] += 1
                elif command['operator'] == 1 and grid[y][x] > 0:
                    grid[y][x] -= 1
                elif command['operator'] == 2:
                    grid[y][x] += 2

    count = 0
    for y in grid:
        for x in y:
            count += x

    print(count)
