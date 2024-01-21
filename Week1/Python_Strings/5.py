#The upper() method returns the string in upper case:
a = "Hello, Almas!"
print(a.upper())

#The lower() method returns the string in lower case:
a = "Hello, World and Almas!"
print(a.lower())

#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World and My Parents! "
print(a.strip()) # returns "Hello, World and My Parents!"

#The replace() method replaces a string with another string:
a = "Hello, World and My Parents. How are you!"
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']