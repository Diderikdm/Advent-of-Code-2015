with open('C:\\Users\\dider\\AppData\\Local\\Programs\\Python\\Python39\\AoC 2015\\input\\day1.txt', 'r') as file:
    data = file.read()
    print('Part 1: {}'.format(data.count('(') - data.count(')')))
    for index in range(len(data)):
        if data[:index+1].count('(') - data[:index+1].count(')') < 0:
            print('Part 2: {}'.format(index+1))
            break
