
# def is short form of define
def multiply(x,y):
    result=x*y
    return result


answer=multiply(10.5,4)
print(answer)

for val in range(1,5):
    two_times=multiply(2,val)
    print(two_times)

# default argument call
def myfun(x,y=50):
    print('x ', x);
    print('y ' , y )
myfun(10)
myfun(10,33)