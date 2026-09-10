def is_palindrome(string):
    backword=string[::-1]
    return backword.casefold()==string.casefold()

world=input(" Please enter a world to check ")

if is_palindrome(world):
    print("{} is a palindrome".format(world))
else:
    print("{} is not a palindrome".format(world))
