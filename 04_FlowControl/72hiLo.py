low = 1
high = 1000

print("please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")
guesses=1
while True:
    guess = low + (high - low) // 2  # //2 give the integer division
    high_low = input(
        "My guess is {}. Should I guess higher or lower ? Enter h or l, or c if my guess was correct".format(
            guess
        )
    ).casefold()

    if high_low=='h':
        # Guess higher. The low end of the range becomes 1 grater than the guess
        low=guess+1
        #pass -> if we have just code framework and going to add code later pass create correct syntax so we can add code later
    elif high_low=='l':
        high=guess-1
        #Gueess lower.The high end of the rane becomes one less than the guess.
        #pass
    elif high_low=='c':
        print("i got it in {} guesses !".format(guesses))
    else:
        print("Please enter h,l or c")
    guesses+=1
