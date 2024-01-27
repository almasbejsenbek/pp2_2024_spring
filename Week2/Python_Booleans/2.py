#Print a message based on whether the condition is True or False:
a = 221
b = 3312
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#The bool() function allows you to evaluate any value, and give you True or False in return,
#Evaluate a string and a number:
print(bool("Almas"))
print(bool(1501))

#Evaluate two variables:
x = "Almas"
y = 15112
print(bool(x))
print(bool(y))

#Almost any value is evaluated to True if it has some sort of content.
#Any string is True, except empty strings.
#Any number is True, except 0.
#Any list, tuple, set, and dictionary are True, except empty ones.
bool("abc")
bool(123)
bool(["almas", "dias", "daulet"])
