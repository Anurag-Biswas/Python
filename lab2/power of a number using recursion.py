def power(m,n):
    if n==0:
        return 1
    else:
        return m*power(m,n-1)
m=int(input("Enter the first number:"))
n=int(input("Enter the second number:"))
print(power(m,n))
