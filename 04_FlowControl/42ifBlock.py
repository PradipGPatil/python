name=input("please enter your name")
#user input will be string so converted into int
age=int(input("how old are you ,{0} ".format(name)))
print(age)

if age>18:
    print("you are old enoguth to vote")
else:
    print("please come back in {0} year".format(18-age))