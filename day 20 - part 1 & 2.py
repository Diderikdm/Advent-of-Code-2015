def calculate(max_val, presents, func):
    houses = {}
    for x in range(1, data):
        for y in range(x, func(x, max_val), x):
            
            if y not in houses:
                houses[y] = 0
            houses[y] += x * presents
            
        if houses[x] >= data:
            return x

data = 36000000

print(calculate(data//20, 10, lambda x,y: y))
print(calculate(data//20, 11, lambda x,y: min(x*50+1, y)))

