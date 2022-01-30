# Logical Operators(and, or, not) check if two or more conditional statements are true.
# In "and" conditioon both the condition given should be true.
# In "or" condition anyone condition should be true.

temp = int(input("What is the temperature outside?: "))

if temp >= 15 and temp <= 30:
    print("The temperature is good outside")
    print("GO OUTSIDE!!")
elif temp < 15 or temp > 30:
    print("The temperature is not good outside.")
    print("STAY INSIDE!!")
else:
    print("Please inpu proper temperature.")    

# "Not" opoerator is kinda weird operator.
#  In not operator if the statement is true it changes to false and if false it chnages to True.
