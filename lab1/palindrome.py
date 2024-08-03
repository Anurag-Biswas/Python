n=int(input("Enter a number:"))
c=n
rev=0
while c>0:
    rev=rev*10+c%10
    c=c//10
if(n==rev):
    print("palindrome number:",n)
else:
    print("Not a palindrome number:",n)
