s=input("Enter a sentence:")
l=0
d=0
for i in s:
    if i.isalpha()== True:
        l=l+1
    elif i.isdigit()==True:
        d=d+1
print("LETTERS",l)
print("DIGITS",d)
