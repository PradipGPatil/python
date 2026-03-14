# # generally while reading file we open it so same will goes for python
# jabber=open('Jabberwocky.txt','r')

# for line in jabber:
#     # this output will print space because /n print pyton on new line but in text editor it take to new line
#    # print(line,end='')
#    print(line.strip())
#     #close the file after reading.
# jabber.close()

# with open("Jabberwocky.txt",'r') as jabber:
#     # for line in jabber:
#     #     print(line.rstrip())
#     #realines return the list 
#     lines=jabber.readlines()
# print(lines)
# #if we want to print last line 
# print(lines[-1:])

# with open("Jabberwocky.txt",'r') as jabber:
#     #this return strin rather than list
#     text=jabber.read()
# #print(text)
# for character in reversed(text):
#     print(character,end='')

with open('Jabberwocky.txt') as jabber:
    while True:
        # readline read the single line upto newline character(\n) or eof
        line=jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break
print('*'*80)

# if did not specific r the default mode will be read
with open('Jabberwocky.txt') as jabber:
    for line in jabber:
        print(line.rstrip())
        if "jubjub" in line.casefold():
            break