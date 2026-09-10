import random

Higher=10
answer=random.randint(1,Higher)
print(answer)       #TODO: to be removed after testin
print("Please guess the number between 1 to {}".format(Higher))
guess=int(input())

flag=True
exist_game="Quit"

if guess== answer: 
    print(" you guess is correctly ")
else: 
    while flag:
        if guess > answer: 
            print(" Please guess the lowere")
        else:
            print("Print guess the Higher")
        guess=int(input())
        if guess==0:
            print(" exiting the game")
            break
        
        elif guess==answer:
            print(" well done ! you guessed it correct !")
            flag=False

            


    