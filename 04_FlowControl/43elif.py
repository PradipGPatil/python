name=input("enter your name ")
age=int(input("how old are you , {0}".format(name)))
print(age)

if age<18:
    print("please come back {0} year later ".format(18-age))
elif age==100:
    print("please enter correct age")
else:
    print("you are old enought to vote")
    print(" please put 'x' in box ")