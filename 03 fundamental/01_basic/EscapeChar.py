splitString="This sring has bee \n slit over \n serveral \n lines";
print(splitString);

tabString="1 \t 2\t 3 \t 4";
print(tabString);


# escape character
print('the pest shop owner say \'no \'not ..');
#or 
print(""" tim said "hello , world ' """);

#we can split sprint multiline in that thirpple quates are helpfule 

print("""
this 
      string 
      as 
      mulitple line

""");


#if we want to print in singe line ,escape end of the line
print(
    """
this \
string \
as \
mulitple line \

"""

);


# scenario where we want to include \ so we will add \\. this method is preparable
print("c:\\User\\tim\\notes.txt");
#or another way put r which tell jave interpriter it row strin
print(r"c:\\User\\tim\\notes.txt")

