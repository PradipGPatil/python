from contents import recipes, pantry
"""
    here we are showing option to user to choce the recepy
"""
display_dic={}

# enumerate can be used on any iterable like list, tuple, dict
for index, key in enumerate(recipes):
    # print("{} : {}".format(index ,key))
    # print(f"{index} : {key}")
    #  print(index,key, sep=" : ")
    display_dic[str(index+1)]=key

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
        for food_item in ingredients: 
            if food_item in pantry:
                print(f"\t {food_item} OK")
            else:
                print(f"\t {food_item} : you do not have necessary ingerdient")

           