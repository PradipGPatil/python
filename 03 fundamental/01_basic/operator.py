a=12
b=3
print(a+b)  #15
print(a-b)  #9
print(a*b)  #36
print(a/b)  #4.0 return result upto decimal places
print(a//b) #integer divison , rounded down to minus infinity 
print(a%b)  # 0 module reminder after integer division

print(a+b/3-4*12)# PEMDAS - Parentheses, Exponents, Mulitplication/division, Addition/substraction
                # 12+3/3-4*12 -> 12+1.0-4*12 -> 12+1.0-48.0-> 13-48

print(a+(b/3)-(4*12)); # 12 +(3/3)-(4*12)=12+1.0-48.0=-35

print((((a+b)/3)-4)*12) # (15/3-4)*12->(5-4)*12->1*12

c=a+b
d=c/3
e=d-4
print(e*12);