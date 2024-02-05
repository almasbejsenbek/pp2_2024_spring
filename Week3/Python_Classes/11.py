def palindrome(word):
    new_word = ''.join(word.lower().split())
    if new_word == new_word[::-1]:
        print(f"{word} is palindrome")
    else:
        print("Is not palindrome")

myword = input()
print(palindrome(myword))

