from contents import pantry

chiken_quantity=pantry.setdefault("chicken",0)
print(chiken_quantity)

beans_qty=pantry.setdefault("beans",0)
print(beans_qty)

ketchup_qty=pantry.get("ketchup",0)
print(ketchup_qty)

print()
print("pantry now contain ...")

for key,value in sorted(pantry.items()):
    print(key,value)
# if we see the output beans get added  for the get does not added 'ketchup'