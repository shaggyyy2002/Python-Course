# A statement that will apply a block of code for a limited amount of time.
# while loop = unlimited time.
# for loop = limited time.

for i in range(10):
    print(i)

for n in range(50,100):
    print(n)

for a in "Nitin":
    print(a)

# Challenge :- Make a stopwatch.

import time

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1) # Waits for 1 sec before executing the next number.
    