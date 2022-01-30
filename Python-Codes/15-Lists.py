# Lists are used to store multiple items in a single variable.
food = ["pizza", "momos", "Paneer", "Sandwhich"]
print(food)

# If we want an specific item we have to enter their index value.
print(food[0])
print(food[1])
print(food[2])
print(food[3])

# We can update an index or add by mentioning the index
food[0] = "Sushi"
print(food)

                                     # THERE ARE SOME FUNCTIONS WE CAN USE IN LIST.
# If we want to add something
food.append("ice cream")
print(food)

# If we want to remove the function we can use 
food.remove("momos")
print(food)

# If we want to remove the last element
food.pop()
print(food)

# If we want to insert an element 
food.insert(0,"momo") # Specify the index to add and the element
print(food)

# If we want to sort list alphabetically
food.sort()
print(food)

# If we want to clear all the elements in the list 
food.clear()
print(food)