vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
}

# my_car = vehicles['Fiesta']
# print(my_car)

# commuter = vehicles['virago']
# print(commuter)

# learner = vehicles.get("ER5")
# print(learner)

# adding item to the dir
# vehicles['test']='new car'

# remoing item from dir
# del vehicles['test']

# vehicles.pop('fiesta')

# if item is not exists then will throw the error
# del vehicles['f1']
#vehicles.pop('f1')
result=vehicles.pop('f1','**here is message we does not exits**')
print(result)

result1=vehicles.pop('fiesta','** here is key exists **')
print(result1)
print()

#printing element from dir
# for key in vehicles:
#     print(key, vehicles[key], sep=', ')

for key, value in vehicles.items():
    print(key, value, sep=', ')
