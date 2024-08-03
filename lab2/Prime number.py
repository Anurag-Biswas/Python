n=int(input("Enter the number:"))
for i in range(2,n//2):
    if(n%i==0):
        print("Composite number",n)
        break
else:
    print("Prime number",n)
