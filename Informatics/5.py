import math
i = 1
x = 0
y = 1
while i <= 10:
    x = x + 1/(y**2)
    y+=1
    i+=1

a = math.sqrt(6 * x)
print(a)