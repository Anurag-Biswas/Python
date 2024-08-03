n=int(input("Enter terms"))
a=0
b=1
c=0
print("Fibonacci series is")
print(a,",",b,end=',')
for i in range(3,n+1,1):
    c=a+b
    print(c,end=",")
    a,b=b,c
