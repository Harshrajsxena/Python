from math import sqrt
n=int(input("enter a number greater then zero="))
x = (((1+sqrt(5))**n)-((1-sqrt(5)))**n)/(2**n*sqrt(5))
print(x)
