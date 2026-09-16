file_name='D:\\Practice\\Python\\08_Mastering_input_output\\Jabberwocky.txt'

# the we did not specifiy the encoding. it will depend upon 'platform dependent'
with open(file_name, encoding='UTF-8') as jabber:
    for line in jabber:
        print(line.rstrip())