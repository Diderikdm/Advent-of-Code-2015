def alter_grid(grid, excluded = []):
    new_grid = {}
    for loc, light in grid.items():
        if loc in excluded:
            new_grid[loc] = '#'
            continue
        adjescents = sum(1 for x in adj if calc(loc, x) in grid and grid[calc(loc, x)] == '#') 
        if (grid[loc] == '#' and adjescents in [2,3]) or (grid[loc] == '.' and adjescents == 3):
            new_grid[loc] = '#'
        else:
            new_grid[loc] = '.'
    return new_grid

with open("C:\\Advent\\2015\\day18.txt", 'r') as file:
    data = [[x for x in y] for y in file.read().splitlines()]
    grid = {}
    adj = sum([[(x,y) for y in range(-1,2) if (x,y) != (0,0)] for x in range(-1,2)], [])
    calc = lambda x, a: (x[0] + a[0], x[1] + a[1])
    for y, row in enumerate(data):
        for x, light in enumerate(row):
            grid[(x,y)] = light

    excluded = [(0,0),(0,len(data)-1),(len(data)-1,0),(len(data)-1,len(data)-1)]
    corner_grid = {k : v if k not in excluded else '#' for k,v in grid.items()}

    for x in range(100):
        grid = alter_grid(grid)
        corner_grid = alter_grid(corner_grid, excluded)
        
    print(sum(1 for x in grid.values() if x == '#'))
    print(sum(1 for x in corner_grid.values() if x == '#'))
