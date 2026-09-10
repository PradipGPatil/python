available_exits=["north","south","east","west"]

chosen_exit=""

# good when does not know in advance how may time you need to loop
while chosen_exit not in available_exits:
    chosen_exit=input("Please choose a direction ")
print(" are't you glad you got out of there")