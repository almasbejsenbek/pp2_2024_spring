def Myfunc(Numbers):
    a = 0
    b = 0
    for num in Numbers:
        if num > 0:
            a = a + num

        if num < 0:
            b = b + num
    return a, b

string_num = input()
numbers = string_num.split()
numbers = [int(string_num) for string_num in numbers]
print(Myfunc(numbers))