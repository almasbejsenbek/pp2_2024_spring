#Remove Specified Item
#The remove() method removes the specified item.
#Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#Remove the first occurance of "banana":
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

#Remove Specified Index
#The pop() method removes the specified index.
#Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

#The del keyword also removes the specified index:
#Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#The del keyword can also delete the list completely.
#Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist

#Clear the List
#The clear() method empties the list.
#The list still remains, but it has no content.
#Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)