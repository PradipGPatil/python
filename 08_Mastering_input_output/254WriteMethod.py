data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

# plants_filename='flowers_write.txt'

# with open(plants_filename,'w') as plants:
#     for plant in data:
#         plants.write(plant)

# print(data)
# string_representation=data.__str__()
# print(type(string_representation))

# try entering numberical value to the text file

file_name="test_number.txt"
with open(file_name,'w') as test:
    for i in range(10):
        print(i,file=test)

with open(file_name,'w') as test:
    for i in range(10):
        # test.write(i) # we are writing to the text file so we can write only text
        test.write(str(i)+"\n")

