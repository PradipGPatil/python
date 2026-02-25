parrot="Norwegian Blue"

letter=input(" enter a character : ")

if letter in parrot:
    print("{} is in {}".format(letter,parrot))
else:
    print("i do not need that letter")