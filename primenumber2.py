num=int(input("Enter any number="))
x=False
if num>0:
    for i in range(2,num):
        if (num%i==0):
            x=True
            break
if x==True:
    print(num,"is not a prime number")
else:
    print(num,"is a prime number")