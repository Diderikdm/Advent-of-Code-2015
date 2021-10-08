from hashlib import md5

puzzle_input = 'ckczppom'
x, part1, part2 = 0, 0, 0

while True:
    trial = md5((puzzle_input + str(x)).encode()).hexdigest()
    if not part1 and trial.startswith('00000'):
        part1 = x
    elif not part2 and trial.startswith('000000'):
        part2 = x
    elif part1 and part2:
        print(part1, part2)
        break
    x+=1
