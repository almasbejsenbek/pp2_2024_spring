#Short Hand If
#If you have only one statement to execute, you can put it on the same line as the if statement.
#One line if statement
a = 200
b = 11
if a > b: print("a is greater than b")

#Short Hand If ... Else
#If you have only one statement to execute, one for if, and one for else, you can put it all on the same line:
#One line if else statement:
a = 2
b = 330
print("A") if a > b else print("B")

#You can also have multiple else statements on the same line:
#One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#And
#The and keyword is a logical operator, and is used to combine conditional statements:
#Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")