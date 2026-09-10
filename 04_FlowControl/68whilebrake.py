available_exits=["north","south","east","west"]

chosen_exits=""

while chosen_exits not in available_exits: 
    chosen_exits=input(" please chose the exits = ")
    if chosen_exits.casefold()=="quit":
        print(" Game Over")
        break

print(" are not you glad , you get exits ")