choice = "-"  # initialise choice to something invalid
while choice != "0":
    # if choice in "12345":  the probleam with this code if we pass 123 it print 
    #if choice in list('12345'):   # here list function create a list like ['1','2','3','4','5']
    if choice in set('12345'): # it is best choice here becuase for the list . need to go by each value but in set uses hashmap to find the item
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input()