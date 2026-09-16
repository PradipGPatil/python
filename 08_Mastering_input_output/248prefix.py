filename='D:\\Practice\\Python\\08_Mastering_input_output\\Jabberwocky.txt'

with open(filename) as poem:
    firstline=poem.readline().rstrip()
print(firstline)

# this method are suppporesed in python 3.9 version
twas_removed=firstline.removeprefix("'Twas")
print(twas_removed)

toves_removed=firstline.removesuffix("toves")
print(toves_removed)
