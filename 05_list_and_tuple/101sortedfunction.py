pangram="The quick brown fox  jump over the lazy dog "
letters=sorted(pangram)
print(letters)

numbers=[2.3,4.5,8.7,3.1,9.2,1.6]

sorted_number=sorted(numbers)
print(sorted_number)
print(numbers)

# sort method does not return any value , it modifity the existing list
another_sorted_number=numbers.sort()
print(another_sorted_number)