empty_list=[]
even=[2,4,6,8]
odd=[1,3,5,7,9,]

# we can add 2 list by concadinating

numbers=even + odd
print(numbers)

# 2nd way to create list , it will create another list
sorted_number=sorted(numbers)
print(sorted_number)
# here original list will be their


digit=sorted('4375909')
# here list is created of character
print(digit)

#more_numbers=list(numbers)
#more_numbers=numbers[:]
more_numbers=numbers.copy()
print(more_numbers)
print(numbers)
print(numbers is more_numbers)
# list is equal becuase both contain the same items
print(numbers == more_numbers)