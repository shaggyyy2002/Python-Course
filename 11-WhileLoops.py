# While loop execute the block of code as long as its conditions remain True.
# If we do not provide a stop statement we will be stuck in an infinte loop.

name = ""
# Here if user leave the space blank it will ask user to enter their name again.
while len(name) == 0:
    name = input("Enter your name: ")
    print("Welcome " +name)
