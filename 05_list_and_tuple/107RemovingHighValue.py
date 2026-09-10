data=[1,5, 105, 109, 111, 350, 370]

min_valid=100
max_valid=200

#process the low values in the list
# notice here we have order list data
stop=0
for index, value in enumerate(data):
    if value>=min_valid:
        stop=index
        break
print(stop)

del data[:stop]

print(data)

# process the higher value

start=0
for index in range(len(data)-1,-1,-1):
    if data[index]<=max_valid:
        # we have to keep index of the last item
        # set start to position of the first item to delete which is '1' after index
        start=index+1
        break
print(start)
del data[start:]
print(data)
