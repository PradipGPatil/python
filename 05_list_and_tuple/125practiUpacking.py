for t in enumerate("abcdefgh"):
    index,character=t
    print(index,character)

index,character=(0,'a')
print(index)
print(character)

# so in below loop , we are unpacking tupple and sort hand to 
# unpack the tupple
for index,character in  enumerate("abcefgh"):
    print(index,character)