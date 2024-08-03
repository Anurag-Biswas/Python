import math
n=int(input("Enter the term:"))
v=1
s=0
x=int(input("Enter x:"))
print("Sine(x)",math.sin(x))
for i in range(1,n+1):
    f=1
    for j in range(1,v+1):
        f=f*j
    d=x**v/f
    f=1
    if(i%2==0):
        s=s+d
    else:
        s=s-d
    v=v+2
print(s)    
