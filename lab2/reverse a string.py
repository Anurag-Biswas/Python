s=input("Enter the string:")
rv=""
for i in range(len(s)-1,-1,-1):
    rv=rv+s[i]
print(rv)
