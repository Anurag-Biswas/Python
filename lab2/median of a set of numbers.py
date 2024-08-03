n=int(input("Enter the total number:"))
s=0
for i in range(1,n+1):
    num=int(input("Enter a number:"))
    s=s+num
m=s/n
print("Median",m)
