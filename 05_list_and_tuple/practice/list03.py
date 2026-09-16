# Practice Problem: Calculate the total sum of all integers in a list and find the arithmetic mean (average).
Numbers= [10, 20, 30, 40, 50]
sumofnumber=sum(Numbers)

print(" sum : {}".format(sumofnumber))
# for number in Numbers:
#     sumofnumber=sumofnumber + number
# print(" sum : {}".format(sumofnumber))

avg_of_number=sumofnumber/len(Numbers)
print(f" avg is : {avg_of_number}")

