def histogram(numbers):
    for number in numbers:
        for i in range(0, number):
            print("*", end="")
        print()

string_num = input()
integers = string_num.split()
integers = [int(string_num) for string_num in integers]
print(histogram(integers))