jabber=open('D:\\Practice\\Python\\08_Mastering_input_output\\Jabberwocky.txt','r')

for line in jabber:
    # print(line,end="")
    print(line.rstrip())

jabber.close()