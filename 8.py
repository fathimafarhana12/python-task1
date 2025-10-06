a=int(input("enter rows:"))
for i in range(1,a+1):
    print('*' * i+' '* (2*a -2*i)+ '*'* i)
for i in range(a-1,0,-1):
    print('*' * i+' '* (2*a -2*i)+ '*'* i)
