from math import sqrt
n= int(input("Enter any number="))

x=(5*(n*n)+4) 
z=(5*(n*n)-4)
y=sqrt(x)
w=sqrt(z)

if x%y==0:
    print("number is Fibonacci number")
elif z%w==0:
    print("number is Fibonacci number")

else:
    print("number is not a Fibonacci number")
   