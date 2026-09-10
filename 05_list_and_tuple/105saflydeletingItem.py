data=[1,5, 105, 109, 111, 350, 370]

# del data[0:2]
# print(data)

# this will not delete the item since we already removed 1 item from the list
# del data[5:]
# print(data)

min_valid=100
max_valid=200

for index, value in enumerate(data):
    if (value<min_valid) or (value>max_valid):
        del data[index] # here we are deleting the value, due to which index position of the list is getting changed
print(data)