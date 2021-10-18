with open("C:\\Advent\\2015\\day14.txt", 'r') as file:
    data = [[x.split(' ')[y] for y in [0,3,6,-2]] for x in file.read().splitlines()]
    end = 2503
    reindeer, second_race = {}, {}
    for who, speed, time, rest in data:
        schema = [int(speed) for x in range(int(time))] + [0 for x in range(int(rest))]
        reindeer[who] = (schema * (end // len(schema) + 1))[:end]
    print(max(sum(v) for v in reindeer.values()))

    second_race_distance = {k:0 for k in reindeer.keys()}
    second_race_points = {k:0 for k in reindeer.keys()}
    for x in range(end):
        for rd, move in reindeer.items():
            second_race_distance[rd] += move[x]
            
        leading = max(v for v in second_race_distance.values())
        for k,v in second_race_distance.items():
            if v == leading:
                second_race_points[k] += 1

    print(max(second_race_points.values()))
        
        
        
        
