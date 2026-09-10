answer=5

print("please guess number between 1 and 10 : ")
guess=int(input())

if guess< answer:
    print("please guess higher")
    guess=int(input())
    if guess==answer:
        print("well done , you guessed it ")
    else:
        print("sorry , you have not guessed correctly ")
elif guess>answer:
    print("please guess lowere")
    guess=input(input())
    if guess==answer:
        print("well done !, you guess it correctly ")
    else:
        print("sorry , you have not guessed correctly ")
else:
    print(" your guess is correct")