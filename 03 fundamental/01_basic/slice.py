     #            1
    #   012345678901234
parrot="Norwegial Blue"

#colon will tell python we need to slice
#start with index 0 upto index 6 but not including 6
print(parrot[0:6])
print(parrot[3:5])
print(parrot[0:9])

#default start index will be zero
print(parrot[:9])

print(parrot[10:])
print(parrot[:])



#negative slice
# we can not slice in backwork direction
print(parrot[-4:2])
print(parrot[-4:12])
print(parrot[-14:-8])
