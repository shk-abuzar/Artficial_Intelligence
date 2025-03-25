#PRINTING FROM 1 TO 100
print("PRINTING FROM 1 TO 100")
for i in range(1,100):
    print(i)

#range(Starting (optional by default 0),ending,Increment or Decrement(optional by default 1))
#PRINTING FROM 100 TO 1 in reverse order
print("Printing FROM 100 TO 1 in reverse order")
for j in range(100,0,-1):
    print(j)

for k in range(5):
    print(k)

#PRINTING MULTIPES OF N
n=int(input("Enter a number to print multiples of that number: "))
print("Multiples of " ,n)
for h in range(1,11):
    print(n,"x",h,"=",n*h)

#Printing sum using for Loop
sum=0
n=int(input("Enter a number: "))
for o in range(n+1):
    sum+=o
print(f"Sum from 1 upto {n}= {sum}")


#Printing sum using while loop

summ=0
count=0
while(count<n+1):
    summ=summ+count
    count=count+1
print(f"from while Sum from 1 upto {n}= {summ}")

#Printing Factorial of a number
fac=1
num=int(input("Enter a number to calculate the factorial: "))
if(num==0):
    print(f"Factorial of {num} is 1")
elif(num<0):
    print("Factorial of -ve numbers is not possible!")
else:
    for f in range(1,num+1):
        fac=fac*f
    print("Factorial of", num, "is", fac)  
