n=int(input("Enter a number:"))
c=n
rev=0
while c>0:
    rev=rev*10+c%10
    c=c//10
print("Reverse",rev)    
