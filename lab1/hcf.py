num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
while(num2!=0):
    temp=num2
    num2=num1%num2
    num1=temp
print("num1")    
