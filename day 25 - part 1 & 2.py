row = 2947
column = 3029
ans = 20151125

a = column
for x in range(1,(row + column-1)):
    a += x

for x in range(a-1):
    ans = (ans * 252533) % 33554393

print(ans)
