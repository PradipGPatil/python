answer=5

print("please guess number between 1 and 10 :")
guess=int(input())

if guess!=answer:
    if guess<answer:
        print("please guess higher")
    else:
        print("please guess lower")
    guess=int(input())
    if guess==answer:
        print("well done !, you gussed it ")
    else:
        print("Sorry , you have not guessed correctly")
else:
    print(" you got it first time")