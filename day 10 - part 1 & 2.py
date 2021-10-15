from itertools import groupby

def solve(data):
    return ''.join(str(len([x for x in v])) + k for k, v in groupby(data))

data = '1113122113' 
for x in range(50):
    if x == 40:
        print(len(data))
    data = solve(data)

print(len(data))
