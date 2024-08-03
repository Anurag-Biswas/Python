import math
def quadratic(a,b,c):
    d=b*b-4*a*c
    root1=0
    root2=0
    if(d>0):
        root1=(-b+math.sqrt(d))/(2*a)
        root2=(-b-math.sqrt(d))/(2*a)
        print("root1",root1)
        print("root2",root2)
    elif(d==0):
        root1=(-b/(2*a))
        root2=(-b/(2*a))
    q1=a*root1**2+b*root1+c
    q2=a*root2**2+b*root2+c
    print("Quadratic equation 1:",q1)
    print("Quadratic equation 2:",q2)
a=float(input("Enter the value of a:"))
b=float(input("Enter the value of b:"))
c=float(input("Enter the value of c:"))
quadratic(a,b,c)
