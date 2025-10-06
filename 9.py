a=int(input("enter the num:"))
s=2*a-1
for i in range(s):
    for j in range(s):
        print(a -min(i,j,s-1-i,s-1-j), end="")
    print()