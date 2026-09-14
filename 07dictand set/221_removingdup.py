data=["blue","red","blue", "green","red","blue"]

# suppose we want to data to be unique

unique_data=set(data)
print(unique_data)

# if we want to set the use the sorted function
unique_data1=sorted(set(data))
print(unique_data1)

# create a list of unique colours , keeping the order they appeared
unique_data=list(dict.fromkeys(data))
print(unique_data)

print()
print(dict.fromkeys(data))