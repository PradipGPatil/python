available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }

current_choice = None
computer_parts={}  # create an empty dictionary

while current_choice != "0":
    #current_choice is going to be key only . if we enter value 'mouse ' it will not give the output
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            #its alread in , so remove it
            print(f'Removing {chosen_part}')
            del computer_parts[current_choice]
        else:
            print(f"Adding {chosen_part}")
            computer_parts[current_choice]=chosen_part
        print(f'Your dictionary now contain {computer_parts}')
    else:
        print('chose options from below')
        for key, value in available_parts.items():
            print(f'{key} : {value}')
        print("0 : to finish")

    current_choice = input("> ")
