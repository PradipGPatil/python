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
