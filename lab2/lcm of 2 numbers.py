n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
lcm=1
if n1>n2:
    mx=n1
    mn=n2
else:
    mx=n2
    mn=n1
i=2
while i<mn:
    if mx%i==0 and mn%i==0:
        mx=mx//i
        mn=mn//i
        lcm=lcm*i
    else:
        i=i+1
lcm=lcm*mx*mn
print("lcm",lcm)


