jabber=open('D:\\Practice\\Python\\08_Mastering_input_output\\Jabberwocky.txt','r')

#python will take care of closing the file. so we does not need to close file here
with open('D:\\Practice\\Python\\08_Mastering_input_output\\Jabberwocky.txt','r') as jabber:
    for line in jabber:
        print(line.rstrip())