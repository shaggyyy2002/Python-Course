name = "Nitin Gouda"
name1 = "nitin"

# We can check the lenth of the name
print(len(name))

# We can also find on what index no our letter is 
print(name.find("G"))

# We can capitalize the first letter
print(name1.capitalize())

# We can make our string uppercase or lowercase
print(name1.upper())
print(name1.lower())

# Check wether the string entered is digits
print(name.isdigit())

# Check wether the name is alphabets. If used space gives false
print(name1.isalpha())

# Checks how many same letters are there
print(name.count("n"))

# We can replace a letter with our desired letter
print(name1.replace("n","0")) 

# It is not a string function but we can print anything for a desired time 
print(name1*3)