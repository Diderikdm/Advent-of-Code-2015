def follow_instructions(data, compass, x=0, y=0):
    houses = [(x,y)]
    for instruction in data:
        x = x + compass[instruction] if instruction in ['<','>'] else x
        y = y + compass[instruction] if instruction in ['^','v'] else y
        houses.append((x,y))
    return houses

with open('C:\\Users\\dider\\AppData\\Local\\Programs\\Python\\Python39\\AoC 2015\\input\\day3.txt', 'r') as file:
    data = file.read()
    compass = {'^' : 1, 'v' : -1, '>' : 1, '<' : -1}      
    print('Part 1: {}'.format(len(set(follow_instructions(data, compass)))))
    print('Part 2: {}'.format(len(set(follow_instructions(data[0:][::2], compass) + follow_instructions(data[1:][::2], compass)))))
