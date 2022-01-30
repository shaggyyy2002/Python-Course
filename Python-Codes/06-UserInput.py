# In user input we wait for the user to type the input we will save that input in variables.
# While using VsCode if youre not able to write something. 
# -> Click on Settings --> Search --> Run in terminal --> CheckBox on CodeRunner

name = input("Enter your name: ")
age = int(input("Enter your age: ")) #we changed our string to int using typecasting to do mathemathical functions
age = age + 1

print("Hello " + name)
print("You are " + str(age) + " years old") # Since we cannot add int to string we have to change our "age" to "str" again