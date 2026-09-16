filename='D:\\Practice\\Python\\08_Mastering_input_output\\Jabberwocky.txt'

with open(filename) as poem:
    firstline=poem.readline().rstrip()
print(firstline)

chars="'Twaseby"
no_apostrophe=firstline.strip(chars)
print(no_apostrophe)
# chars=" ' Twaseby"

for character in firstline:
    if character in chars:
        print(f" removing {character}")
    else:
        break

print("*"*80)

for character in firstline[::-1]:
    if character in chars:
        print(f" removing {character}")
    else:
        break

