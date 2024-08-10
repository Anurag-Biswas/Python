s=input("Enter a string:")
ch=input("Enter a character to remove:")
for i in s:
    if i!=ch:
        print(i,end="")
