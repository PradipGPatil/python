answer=5

print("please guess number between 1 and 10 : ")
guess=int(input())

if guess< answer:
    print("please guess higher")
elif guess>answer:
    print("please guess lowere")
else:
    print(" your guess is correct")