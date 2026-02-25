name=input("Please enter your name ")
age=int(input("how old are you , {0} ".format(name)))
print(age)

# if age>=18:
#     print("you are old engought to vote")
#     print("please put x in the box")
# else:
#     print("Please come back in {0} years".format(18-age))

if age<18:
    print("Please come back in {0} years".format(18-age))
elif age==900:
    print(" make sure you have entered correct age")

else:
    print("you are old engought to vote")
    print("please put x in the box")