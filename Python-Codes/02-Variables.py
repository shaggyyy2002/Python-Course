# Variables are like a container which is used to store the value. 
# Data type is an attribute associated with a piece of data that tells a computer system how to interpret its value.

# ----Strings---- #
firstName = "Nitin"
lastName = "Gouda"
fullName = (firstName +" "+ lastName)
# We can find what is the value. 
print(type(firstName))
print(type(lastName))
# We have combined a str with a str using an arithmethic operator(+).
print("Hello " + fullName +" "+ "Welcome to our Python Learning!")

# ----Int---- #
# An Int Datatype is a datatype which can store numerical values which are whole numbers in genral.
age = 19
age += 1 # we used an increment operator so that when age is print it will add +1 in the age and then it will get executed.
myage ="19" # When we used (" ") it converts int type to a str type.
print(type(age))
print(type(myage))
# We cannot add an int with a str if done so it will give us an TypeEror
print("Your age is: " + str(age)) 

# ----Float---- 
# A float is a numerical value which stores decimal value
height = 159.6
print(type(height))
print("Your height is: "+ str(height))

# ----Boolean---- #
# Boolean value stores true or false values.It is very useful when we get to if statments.
human = True
desk = False
print(type(human))
print(type(desk))
print(human)
print(desk)
