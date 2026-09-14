from contents import recipes, pantry
"""
    here we are showing option to user to choce the recepy
"""

def add_shoping_item(data:list, item:str, amount:int)->None:
    """Add a tupple containg `item` and `amount` to the `data` list."""
    data.append((item,amount))



display_dic={}

# enumerate can be used on any iterable like list, tuple, dict
for index, key in enumerate(recipes):
    # print("{} : {}".format(index ,key))
    # print(f"{index} : {key}")
    #  print(index,key, sep=" : ")
    display_dic[str(index+1)]=key

shopping_list=[]

while True:
    # display the menu of the receipy we know how to cook
    print("please chose the recipy")
    print("-"*50)

    for key, val in display_dic.items():
        print(f"{key} : {val}")

    choice=input(": ")
    if choice=="0": # compare with "0" since user input will be string 
        break
    elif choice in display_dic:
        selected_item=display_dic[choice]
        print(" You have selected the item : {}".format(selected_item))
        print("checking ingerdient .....")
        ingredients=recipes[selected_item]
        print(ingredients)
        print("--checking the stock ")
        for food_item, required_qty in ingredients.items(): 
            quantity_in_pantry=pantry.get(food_item,0)
            if required_qty <= quantity_in_pantry:
                print(f"\t {food_item} OK")
            else:
                quantity_to_buy=required_qty-quantity_in_pantry
                print(f"\t You need to buy the qty {quantity_to_buy} for the {food_item}")
                add_shoping_item(shopping_list,food_item,quantity_to_buy)

for things in shopping_list:
    print(things)

# the probleam with this code , we can get same shoping item multiple time
           