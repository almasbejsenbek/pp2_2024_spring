#Looping Through a String
#Even strings are iterable objects, they contain a sequence of characters:
#Loop through the letters in the word "banana":
for x in "banana":
  print(x)

#The break Statement
#With the break statement we can stop the loop before it has looped through all the items:
#Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#Exit the loop when x is "banana", but this time the break comes before the print:
#fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)