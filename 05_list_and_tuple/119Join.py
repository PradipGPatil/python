menu=[
    ["egg","bacon"],
    ["egg","sausage","bacon"],
    ["egg","spam"],
    ["egg","bacon","spam"],
    ["egg","bacon","sausage","spam"],
    ["spam","bacon","sausage","spam"],
    ["spam","egg","spam","spam","bacon","spam"]
]
for meal in menu:
    for index in range(len(meal)-1,-1,-1): 
        if meal[index]=="spam":
            del meal[index]

    print(",".join(meal))

print("*"*50 +"flowers "+"*"*50)

flowers=[
    "Daffodil",
    "Evening primrose",
    "hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily"
]

# for flower in flowers:
#     print(flower)

separtor=" | "
output=separtor.join(flowers)
print(output)

# all the item must be strin if list contain number it will give error
print(" , ".join(flowers))