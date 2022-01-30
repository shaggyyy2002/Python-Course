# In nested Loop the "inner loop" will finish all of its iteration before finishing one iteration of "outer loop".

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("what is the symbol you want to use?: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="") # We used end so that after it takes 5 rows and 5 columns and slso end after 5 rows
    print() # Make sure you have the right amount of space everywhere otherwise code will not run proper
    
       