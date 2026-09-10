def is_palindrome(string):
    return string[::-1].casefold()==string.casefold()


# function to remove the tab and space

def palindrone_sentence(sentence):
    clean_text=""
    for char in sentence:
        if char.isalnum():
            clean_text+=char
    return is_palindrome(clean_text)

print(" enter the text which we want to check ")

world=input()

if palindrone_sentence(world):
    print(" the enter text is palindrone")
else:
    print(" the entered test is not palindrone")