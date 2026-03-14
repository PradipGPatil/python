availabe_parts=["computor","monitor","keyboard","mouse","mouse mat"]
current_choice="-"
computor_parts=[]

while current_choice!='0':
    if current_choice in "12345":
        print("adding {}".format(current_choice))
        if current_choice=='1':
            computor_parts.append("computor")
        elif current_choice=='2':
            computor_parts.append("monitor")
        elif current_choice=='3':
            computor_parts.append("keyboard")
        elif current_choice=='4':
            computor_parts.append("mouse")
        elif current_choice=='5':
            computor_parts.append("mouse mat")
    else:
        print("please add options from the list below ")
        #instead of this we can list iterator 
        # print("1:computor")
        # print("2:monitor")
        # print("3:keyboard")
        # print("4:mouse")
        # print("5:mouse mat")
        # print("0:to finish")
        for number,part in enumerate(availabe_parts):
            print("{0}:{1}".format(number+1,part))
    current_choice=input()

print(computor_parts)