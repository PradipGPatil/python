# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}
 
# Text string
text = "aaLater in the course, you'll see how to use the collections Counter class."
 
# Your code goes here ...
newText=text.casefold()


for value in newText:
    if value.isalnum():
        word_count.setdefault(value,0)
        word_count[value]+=1
        
    

 
# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)