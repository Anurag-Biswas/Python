
def calculate_slope(x1,y1,x2,y2):
    m=(y2-y1)/(x2-x1)
    return m
x1=int(input("Enter the value of x1:"))
x2=int(input("Enter the value of x2:"))
y1=int(input("Enter the value of y1:"))
y2=int(input("Enter the value of y2:"))
print("Slope of a linear equation",calculate_slope(x1,y1,x2,y2))
