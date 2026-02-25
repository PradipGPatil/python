shoppinglist=["milk","egg","spam","rice"]

for item in shoppinglist:
    if item=="spam":
        continue
    print("buy "+item)
print("----")
for item in shoppinglist:
    if item=="spam":
        break
    print("buy "+item)