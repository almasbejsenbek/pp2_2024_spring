def is_prime(integer):
    if integer < 2:
        return False
    for i in range(2, integer):
        if integer % i == 0:
            return False
    return True

def filter_prime(integers):
    return[integer for integer in integers if is_prime(integer)]

integer = input()
integers = integer.split() 
integers = [int(integer) for integer in integers]

prime_numbers = filter_prime(integers)
print(prime_numbers)
