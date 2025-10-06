a=int(input("enter the amount:"))
for i in [100,50,20,10,5,2,1]:
    count=a//i
    if count>0:
        print(count,"x",i)
        a=a%i