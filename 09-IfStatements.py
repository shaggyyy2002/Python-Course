# A block of code which will execute if the code is true

age = int(input("What is your age?: "))
if age >= 100:
    print("You are a century old!!")
elif age >= 18:
    print("You are an Adult") 
elif age <= 0:
    print("You are not even born yet")    
else:
    print("You are a child")       

# Make a Grade system

grade = str(input("What is your garde?: "))
if grade =="A":
    print("Awesome, Keep It Up!!")
elif grade =="B":
    print("Goood") 
elif grade =="C":
    print("Need Improvement!")
elif grade =="D":
    print("Failing in one Subject!")
elif grade =="E":
    print("Failing in two Subject!")
elif grade =="F":
    print("Failing in three Subject!")    
else:
    print("Please give Proper Input!!")    
