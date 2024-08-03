n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
if n1>n2:
    mx=n1
    mn=n2
else:
    mx=n2
    mn=n1
gcd=1
i=2
while i<=mn:
    if mx%i==0 and mn%i==0:
        mx=mx//i
        mn=mn//i
        gcd=gcd*i
    else:
        i=i+1
print("GCD:",gcd)
    
