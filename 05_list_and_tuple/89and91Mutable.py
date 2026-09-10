shoping_list=["rice","oil","colgate"]
another_list=shoping_list
print(id(shoping_list))
print(id(another_list))

shoping_list+=["body spary"]
print(shoping_list)
print(id(shoping_list))

# if we print another_list it will display the same list like shoping list
print(another_list)
print(id(another_list))