# 10

a=int(input("Enter rows:"))
for i in range(a,0,-1):
    print(" " * (a-i)+ "* "*i)
for i in range(2,a+1):
    print(" " * (a-i)+ "* "*i)
print()