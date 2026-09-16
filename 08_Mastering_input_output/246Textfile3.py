
#the open function return the object  which has 3 method we can easily read the file
# as readlines return the list . the file size shoudl be such a way that it should be fit in memory
# with open('D:\\Practice\\Python\\08_Mastering_input_output\\Jabberwocky.txt','r') as jabber:
#     lines=jabber.readlines()        # readline return list of string
# print(lines)
# print(lines[-1:])

# # suppose if we want to read file in reversed oreder

# for line in reversed(lines):
#     print(line,end="")

# read function return string 
# with open('D:\\Practice\\Python\\08_Mastering_input_output\\Jabberwocky.txt','r') as jabber:
#     text=jabber.read()

# print(text)

# for character in reversed(text):
#     print(character,end="")

# readline()
with open('D:\\Practice\\Python\\08_Mastering_input_output\\Jabberwocky.txt','r') as jabber:
    while True:
        line=jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break