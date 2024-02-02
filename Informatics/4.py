i = 1
y = 1
x = 0
while i <= 5:
    x = x + 4/y - 4/(y+2)
    y = y + 4
    i += 1

print(x)