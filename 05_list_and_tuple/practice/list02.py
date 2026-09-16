# Exercise 2. Perform List Manipulation
# Practice Problem: Take a given list and modify it through five specific actions:

# Change Element: Change the second element of a list to 200 and print the updated list.
# Append Element: Add 600 o the end of a list and print the new list.
# Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
# Remove Element (by value): Remove 600 from the list and print the list.
# Remove Element (by index): Remove the element at index 0 from the list print the list.
# Exercise Purpose: Python lists are mutable, meaning they can be changed after they are created. This exercise demonstrates the various ways to “reshape” your data dynamically during execution.

# Given Input: Initial List: [100, 50, 400, 500]

input=[100,50,400,500]

input[1]=200
print(input)

print("appending element in list")
input.append(600)
print(input)

# inserting element 
input.insert(2,300)
print(input)

# removing 600 from the list
input.remove(600)
print(input)

#removing element by using index
input.pop(4)
print(input)