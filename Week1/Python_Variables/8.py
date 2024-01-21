x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
# If you use the global keyword, the variable belongs to the global scope:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#Also, use the global keyword if you want to change a global variable inside a function.