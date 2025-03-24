#BASIC SYNTAX OF WHILE LOOP
count=0
while count<5:
    print("hello Pyhton!")
    count=count+1

#PRINTING NUMBERS FROM 1 TO 100
i=1
while i<=100:
    print(i)
    i+=1

#PRINTING NUMBERS FROM 100 TO 1 IN reverse ORDER
i=100
while i>=1:
    print(i)
    i-=1

#PRINTING a TABLE OF USER ENTERED NUMBER
n=int(input("Enter a number:"))
i=1
print(f"Table of {n} is")
while i<=10:
    print(f" {i}*{n}={i*n}")
    i=i+1

#PRINTING VALUES IN A LIST
nums=[1,4,9,16,25,36,49,64,81,100]
i=0
while i<len(nums):
    print(f'value at {i} index is: {nums[i]}')
    i+=1

# SEARCHING x IN A TUPLE
nums=(1,4,9,16,25,36,49,64,81,100)

x=int(input("Enter a number you want to search: "))
i=0
while i<len(nums):
    if(x==nums[i]):
        print(f"Element found at index {i}")
        break
    else:
        print("finding...")
    i+=1
print("End of Loop")

#PRINTING ODD ELEMENTS
i=0
while i<10:
    if(i%2==0):
        i+=1
        continue
    print(i)
    i+=1

#PRINTING EVEN ELEMENTS upto n
i=0
n=int(input("Enter a number: "))
while i<n:
    if(i%2!=0):
        i+=1
        continue
    print(i)
    i=i+1