
missing_letter=sorted('The quick fox jump over the lazy Dogs',key=str.casefold)
print(missing_letter)

name=['Test', 'Jon', 'patric']
name.sort()
print(name)

name.sort(key=str.casefold)
print(name)