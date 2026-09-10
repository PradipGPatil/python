shoping_list=["milk", "pasta", "eggs","spam","brad","rice"]

# for item in shoping_list:
#     if item != 'spam':
#         print("Buy "+item)

for item in shoping_list: 
    if item=="spam":
        continue    # we code search to continue , then it will skip all code below and move to next for loop
    print(" Buy "+ item)