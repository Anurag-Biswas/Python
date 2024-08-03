marks1=int(input("Enter the marks in mathematics:"))
marks2=int(input("Enter the marks in Physics:"))
marks3=int(input("Enter the marks in Chemistry:"))
total=marks1+marks2+marks3
totalmp=marks1+marks2
print("Total marks in all 3 subjects",total)
print("Total marks got in mathematics and Physics",totalmp)
if(marks1>=60 and marks2>=50 and marks3>=40 and total>=200 and totalmp>=150):
    print("Student is eligible for admission")
else:
    print("Student is not eligible for admission")
