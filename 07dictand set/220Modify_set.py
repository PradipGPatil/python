# here python will create empty dictionlay 
# number={}

# print(number, type(number))

# to create empty set , use set function
number=set();
print(number, type(number))

#if we enter duplicate value , set does not include duplicate value
while len(number) < 4:
    next_value=int(input("please enter next value : "))
    number.add(next_value)
print(number)