with open("C:\\Advent\\2015\\day23.txt", 'r') as file:
    data = [x.split(', ') for x in file.read().splitlines()]
    instructions = {
        'hlf' : lambda x        : registers[x] // 2,
        'tpl' : lambda x        : registers[x] * 3,
        'inc' : lambda x        : registers[x] + 1,
        'jmp' : lambda x,y      : x + int(y),
        'jie' : lambda x,y,z    : (x + int(y)) if registers[z]%2 == 0 else x+1,
        'jio' : lambda x,y,z    : (x + int(y)) if registers[z] == 1 else x+1
        }

    for registers in [{'a' : 0, 'b' : 0}, {'a' : 1, 'b' : 0}]:
        i = 0
        while i in range(len(data)):
            instruction = data[i]
            ins, reg = instruction[0].split(' ')
            if ins in ['jmp', 'jie', 'jio']:
                if ins == 'jmp':
                    i = instructions[ins](i, reg)
                else:
                    i = instructions[ins](i, instruction[1], reg)
                continue

            registers[reg] = instructions[ins](reg)
            i += 1

        print(registers)
