with open("C:\\Advent\\2015\\day16.txt", 'r') as file:
    data = [x.split(': ') for x in file.read().replace(',',':').splitlines()]
    sues = {x[0].strip('Sue ') : {x[y] : int(x[y+1]) for y in range(1, len(x), 2)} for x in data}
    real_sue = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3,'akitas': 0,\
                'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
    for x,y in sues.items():
        if all(real_sue[k] == sues[x][k] for k in y.keys()):
            print(1, x) 
        elif all(real_sue[k] == sues[x][k] for k in y.keys() if k not in ['cats', 'trees', 'pomeranians', 'goldfish']):
            if all(sues[x][k] > real_sue[k] for k in ['cats', 'trees'] if k in sues[x]):
                if all(sues[x][k] < real_sue[k] for k in ['pomeranians', 'goldfish'] if k in sues[x]):
                    print (2, x)
