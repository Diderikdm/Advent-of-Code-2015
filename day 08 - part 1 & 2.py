with open("C:\\Advent\\2015\\day8.txt", 'r') as file:
    data = file.read().splitlines()
    print(sum(len(x) - len(x[1:-1].encode('utf-8').decode('string-escape')) for x in data))
    print(sum(len('"{}"'.format(x.replace('\\','\\\\').replace('"','\\"'))) - len(x) for x in data))
