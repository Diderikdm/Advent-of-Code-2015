import json

def calculate(data, param = lambda x: False):
    if type(data) == list:
        return sum(x if type(x) == int else calculate(x, param) for x in data if type(x) in [int, list, dict])
    else:
        return sum(v if type(v) == int else calculate(v, param) for k,v in data.items() if type(v) in [int, list, dict]) \
               if not any(param(x) for x in data.values()) else 0


with open("C:\\Advent\\2015\\day 12.txt", 'r') as file:
    data = json.loads(file.read())
    result = calculate(data)
    print(result)
    result = calculate(data, lambda x: x == "red")
    print(result)
