import random


def get_integer(prompt):
    # setting-> search for 'docstring'
    """
    Gets integer from standard input(stdin)

    The function will contious looping and prompting user, unti valid `int` is entered
    
    :param prompt: The String user will see , when they prompted to enter the value

    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("{0} is not a valid number".format(temp))

help(get_integer)
print("*"*80)
print(input.__doc__)
print("*"*80)
print()
print("*"*80)

highest = 1000
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing
guess = 0 # initialise to any number that doesn't equal the answer
print("Please guess number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:   # guess must be greater than answer
            print("Please guess lower")
        # guess = int(input())
        # if guess == answer:
        #     print("Well done, you guessed it")
        # else:
        #     print("Sorry, you have not guessed correctly")
