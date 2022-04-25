x=int(input("enter the first value="))
y=int(input("enter the last value="))
z=[]
for i in range(x,y):
    if i==0 or i==1:
        continue
    else:
        for j in range(2,(i-1)):
            if i%j==0:
                break
        else:
            z.append(i)
print(z)
