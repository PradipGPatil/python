# function to remove the tab and space

def palindrone_sentence(sentence):
    clean_text=""
    for char in sentence:
        if char.isalnum():
            clean_text+=char
    return sentence[::-1].casefold()==sentence.casefold()

print(" enter the text which we want to check ")

world=input()

if palindrone_sentence(world):
    print(" the enter text is palindrone")
else:
    print(" the entered test is not palindrone")