# # using tuple 
tuple1=("geeks","for","geeks")
print("Length of tuple",len(tuple1))
for i in tuple1: #for(i=0;i<len(tuple);i++)
    print(i)


 # list illustration
list1=["2nd","Lab","of","AI"]
for index,values in enumerate(list1):
   print(f"Here the {index} index : {values}")
print(f"Complete list is: {list1}")
print("Another one List")
listt=[1,4,9,25,36,49,64,81,100]
for i in listt:
    print(i)


# String illustration
string_1="Synatx of loops"

for i in range(len(string_1)):
    print(f"Here {i} is {string_1[i]}")
# printing index by using a function enumerates
for i,values in enumerate(string_1):
    print(f"Here {i} in the string is: {values}")


# Here printing the index of list
for  i in range(len(list1)):
    print (f"Here {i} is {list1[i]}")

x=int(input("Enter a number you want to search: "))
i=0
listt=(1,4,9,25,36,49,64,81,100)
for i,Values in enumerate(listt):
    if(x==Values):
        print(f"Element found at index: {i}")
        break
    i+=1
else:
    print("Element not found")
    
#LINEAR SEARCHING
x=int(input("Enter a number you want to search: "))
i=0
idx=0
listt=(1,4,9,25,36,49,64,81,100)
for i in listt:
    if(x==i):
        print(f"Element found at index: {idx}")
        break
    idx +=1
else:
        print("Element not found")


