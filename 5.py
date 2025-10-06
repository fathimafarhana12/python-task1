a=float(input("enter the value of a:"))
coef=[3,2,1,5]
result=0
power =len(coef)-1
for i in range(len(coef)):
    result += coef[i] * (a ** power)
    power -=1
print("Polynomial value at a=",a,"is",result)