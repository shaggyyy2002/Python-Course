# Loop control statements changes a loop execution from its normal sequence.

# break = used to terminate the loop entirely.
# continue = skips to the next iteration.
# pass = does nothing, acts as a placeholder.


while True:
    name = input("What is your name?: ")
    if name != "": # If we input our name it will break the statement
        break

phoneNumber = "998-7724-866" # We have to use string because int object is not iterable
for i in phoneNumber:
    if i =="-":
        continue
    print(i,end="")

for i in range(1,21):
    if i == 13:
        pass 
    else:
        print(i) 