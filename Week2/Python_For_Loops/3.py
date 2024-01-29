#The continue Statement
#With the continue statement we can stop the current iteration of the loop, and continue with the next:
#Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#The range() Function
#To loop through a set of code a specified number of times, we can use the range() function,
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
#Using the range() function:
for x in range(6):
  print(x)

#The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):
#Using the start parameter:
for x in range(2, 6):
  print(x)

#The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
#Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
  print(x)