# Practice Problem: Multiply every number in a list together to find the total product.
factor=[2,3,5,7]

accu_sum=1

for f in factor:
   accu_sum*= f 
print(accu_sum)