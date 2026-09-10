parrot="Norwegian Blue"

letter=input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter,parrot))
else:
    print("i do not need that letter")

activity=input("What would you like to do today ?")

#CASEFOLD() to caseless matching
if "cinema" not in activity.casefold():
    print("But i want to go to the cinema")

