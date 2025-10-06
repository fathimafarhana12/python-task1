a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))
d=b**2-4*a*c
if d >= 0:
    root1=(-b + d**0.5) / (2*a)
    root2=(-b - d**0.5) / (2*a)
else:
    real= -b / (2*a)
    imag=abs(d)**0.5 / (2*a)
    root1=complex(real,imag)
    root2=complex(real,-imag)

print( root1,"and",root2)