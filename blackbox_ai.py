# Blackbox AI test script

# Start query with '//' and be sure to state language
# Not perfect. For example, the print statements forgot to include '()'. But very cool.

// How do I create a for loop in python?

mylist = [1,2,3]
for item in mylist:
    print(item)
    # print item

mydict  = {1:'one', 2:'two', 3:'three'}
for key in mydict:
    print(key, mydict[key])
    # print key, mydict[key]


for i, item in enumerate(mylist):
    mylist[i] = item**2


