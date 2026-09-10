availabe_parts=["computor","monitor","keyboard","mouse","mouse mat", 'test']
current_choice="-"
computor_parts=[]

valid_choice=[]
for i in range(1,len(availabe_parts)+1):
    valid_choice.append(str(i)) # converted into string becuase user entered value is string
print(valid_choice)

while current_choice!='0':
   # if current_choice in "12345":
    if current_choice in valid_choice:
        index=int(current_choice)-1
        chosen_parts=availabe_parts[index]

        # consider if part is already exists in list then we need to remove the part
        if chosen_parts in computor_parts: 
            print("Removing {}".format(current_choice))
            #.remove method to remove the item from the list
            computor_parts.remove(chosen_parts)
        else:
            print("Adding {}".format(current_choice))
            #.append method to add the item in the list
            computor_parts.append(chosen_parts)
        print('your list now contains {}'.format(computor_parts))


        # if current_choice=='1':
        #     computor_parts.append("computor")
        # elif current_choice=='2':
        #     computor_parts.append("monitor")
        # elif current_choice=='3':
        #     computor_parts.append("keyboard")
        # elif current_choice=='4':
        #     computor_parts.append("mouse")
        # elif current_choice=='5':
        #     computor_parts.append("mouse mat")
    else:
        print("please add options from the list below ")
        #instead of this we can list iterator 
        # print("1:computor")
        # print("2:monitor")
        # print("3:keyboard")
        # print("4:mouse")
        # print("5:mouse mat")
        # print("0:to finish")

        # for parts in availabe_parts:
        #     print('{0} : {1}'.format(availabe_parts.index(parts)+1, parts))


        for number,part in enumerate(availabe_parts):
            print("{0}:{1}".format(number+1,part))
    current_choice=input()

print(computor_parts)

# simple example of enumerate , enumerate return index postion of the character and the character

# for index, character in enumerate("abcdefghijk"):
    # print(index,character)