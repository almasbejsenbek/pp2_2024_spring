def is_palindrome(string):
    string = string.lower().replace(" ", "")
    return string == string[::-1]


input_string = "А роза упала на лапу Азора"
if is_palindrome(input_string):
    print('палиндром') 
else:
    print('не палиндром')