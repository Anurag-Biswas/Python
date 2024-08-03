n=int(input("Enter a number:"))
b=0
d=n
while d>0:
    r=d%2
    b=b*10+r
    d=d//2
bi=b
b=0
while bi>0:
    r=bi%10
    b=b*10+r
    bi=bi//10
print(b)
