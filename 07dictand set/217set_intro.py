#  set are unorder . if we run multiple time report will display diff output

farm_animal={'cow','sheep','hen','goat','horse'}
print(farm_animal)

for animal in farm_animal:
    print(animal)

print()
print("indexing a sequence")
animal_list=['cow','sheep','hen','goat']
goat=animal_list[3]
print(goat)

# print("indexing set is not possible")
# goat=farm_animal[3]

more_animal={'sheep','goat','cow','horse','hen'}

# list compare each item . but for set item are not sorted but it oes not check sequenclly.
if more_animal==farm_animal:
    print(" The set are equal")
else:
    print("The sets are different")