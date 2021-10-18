def alter_data(data, index):
    if data[index] == 'z':
        if index == 0:
            return ''.join(['a' for x in len(data)])
        return alter_data(data, index-1)
    return data[:index] + chr(ord(data[index]) + 1) + ''.join(['a' for x in range(index+1, len(data))])


def run(data):
    while True:
        for ex in excluded:
            if ex in data:
                data = alter_data(data, data.index(ex))
        if not len(list(set(sum([[x,x+1] for x in range(0, len(data)-1) if data[x] == data[x+1]], [])))) > 3:
            data = alter_data(data, len(data)-1)
        elif not any(ord(data[x+2]) - ord(data[x+1]) == 1 and ord(data[x+1]) - ord(data[x]) == 1 for x in range(0, len(data)-2)):
            data = alter_data(data, len(data)-1)
        else:
            return data

data = "vzbxkghb"
excluded = ['i', 'o', 'l']

data = run(data)
print(data)

data = run(alter_data(data, len(data)-1))
print(data)
