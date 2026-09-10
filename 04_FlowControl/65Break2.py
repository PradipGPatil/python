# shoping_list=["milk", "pasta", "eggs","spam","brad","rice"]

# # for item in shoping_list:
# #     if item != 'spam':
# #         print("Buy "+item)

# for item in shoping_list: 
#     if item=="spam":
#         break    # if find the this we needed break the loop
#     print(" Buy "+ item)

shoping_list=["milk", "pasta", "eggs","spam","brad","rice"]
item_to_find="Test"
found_at=None

# for index in range(len(shoping_list)):
#     if shoping_list[index]==item_to_find:
#         found_at=index
#         break

if item_to_find in shoping_list: 
    found_at=shoping_list.index(item_to_find)

# if we does not have item is list . then message printed is not correct 
if found_at is not None:
    print(" Item found at position {} ".format(found_at))
else: 
    print(" item not found")

