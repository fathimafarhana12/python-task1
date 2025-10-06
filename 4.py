def sum(n, p):
    if n==0:
     return 0
    return(n % 10)**p+sum(n//10,p)

def is_armstrong(n):
    digits=len(str(n))
    return n==sum(n,digits)

def find_armstrong(start,end):
    if start>end:
        return
    if is_armstrong(start):
        print(start)
    find_armstrong(start+1,end)

print("numbers between 1 and 500")
find_armstrong(1,500)