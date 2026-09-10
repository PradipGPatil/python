even=[2,4,6,8]
odd=[1,3,5,7,9]

even.extend(odd) # appended the 2 list 
print(even)

# sort function make the sorting of the existing list does not create a copy 
even.sort()
print(even)

another_even=even
print(another_even)

# reserver the list 

even.sort(reverse=True)
print(even)
print(another_even)
