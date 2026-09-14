small_int=set(range(21))
print(small_int)

# clearing the set 

# small_int.clear()
# print(small_int)

# to remove item we have discard method and remove method
# discard method- If item does not exits  it will not throw the exception
# remove method- if item does not exits from the set. it will throw the exception

small_int.discard(10)
small_int.remove(11)
print(small_int)

# trying to remove the item which does not exits. 
small_int.discard(99)
print(small_int)