# Slicing = Create a substring by extracting elements from another strings
#                             indexing[] or slice()
#                               [start:stop:step]

name = "Nitin Gouda"

# To slice we have to give a starting index which is default inclusive and ending index which is exclusive.
firstName = name[0:6] # 6 bcoz ending is exclusive we have to mention the next index 
lastname = name[6:] # If we want to select everything after the starting point is mentioned we can leave the stop section blank
print(firstName + lastname)

# Step is option feild we can set our value to. If we use step 2 it will count every second character after first.
step = name[::2] # Normally step is set 1 as default 
print(step) 

# If we want to set string backwards we can set step to -1
reverseName = name[::-1]
print(reverseName)

                                        # ------Slice------

website = "http://google.com" #If we want to slice the name "Google" we have to select the start point an end point
#But not every website will have the same lenth so we will use negative indexing.
# What is negative indexing? 
# The indexing starting from begining counts from 0-1-2.. and negative indexing are counted from the end -1,-2,-3..
# In slice we seprate it using commas.
slice1 = slice(7,-4) 
print(website[slice1])

# Challenge: Slice Wikipedia
website2 ="https://wikipedia.com"
slice2 = slice(8,-4) 
print(website2[slice2])