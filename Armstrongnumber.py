num=int(input("Enter any number"))
sum=0
x = num
while x > 0:
   y = x % 10
   sum =sum + (y ** 3)
   x = x//10
   
if sum==num:
    print("{} is a armstong".format(num))
else:
    print("{} is not a armstong".format(num))

