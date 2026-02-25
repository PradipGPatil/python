shoping_list=["rice","oil","colgate"]
another_list=shoping_list
print(id(shoping_list))
print(id(another_list))

shoping_list+=["body spary"]
print(shoping_list)
print(id(shoping_list))