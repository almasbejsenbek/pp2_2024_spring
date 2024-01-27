#In fact, there are not many values that evaluate to False, 
#except empty values, such as (), [], {}, "", the number 0, and the value None.
#And of course the value False evaluates to False.
#The following will return False:
x = bool(False)
print(x)
x = bool(None)
print(x)
x = bool(0)
print(x)
x = bool("")
print(x)
x = bool(())
print(x)
x = bool([])
print(x)
x = bool({})

# One more value, or object in this case, evaluates to False, 
# and that is if you have an object that is made from 
# a class with a __len__ function that returns 0 or False:
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))

#You can create functions that returns a Boolean Value:
#Print the answer of a function:
def myFunction() :
  return True
print(myFunction())

#Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return False
if myFunction():
  print("YES!")
else:
  print("NO!")

# Python also has many built-in functions that return a boolean value, like the isinstance() function, 
# which can be used to determine if an object is of a certain data type:
#Check if an object is an integer or not:
x = 200
print(isinstance(x, int))