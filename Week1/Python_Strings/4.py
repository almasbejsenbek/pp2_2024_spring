#You can return a range of characters by using the slice syntax.
#Specify the start index and the end in dex, separated by a colon, to return a part of the string.
b = "Hello, World!"
print(b[2:5])
#Get the characters from position 2 to position 5 (not included):

#By leaving out the start index, the range will start at the first character:
b = "Almas, Student!"
print(b[:5])

#Get the characters from position 2, and all the way to the end:
b = "I am Student!"
print(b[2:])

#Use negative indexes to start the slice from the end of the string:
#Get the characters:
#From: "o" in "World!" (position -5)
#To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])