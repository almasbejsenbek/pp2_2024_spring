def unique(mylist):
    list_unique = []
    for num in mylist:
        if num not in list_unique:
            list_unique.append(num)
    return list_unique

number = input()
numbers = number.split()
numbers = [int(number) for number in numbers]
print("Unique List:", unique(numbers))