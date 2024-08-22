student={'First Name':'Adarsh',
         'Last Name':'Das',
         'gender':'Male',
         'age':22,
         'is_married':'No',
         'skills':['Java','C','Python'],
         'country':'India',
         'City':'Kolkata',
         'Address':'Behala'}
print(student)
#Length
print("Length of the dictionary:",len(student))
print("Data type of skills :",type(student['skills']))

#modify Skills
student['skills'].append("React")
print(student['skills'])

#keys as list
print(student.keys())

#values as list
print(student.values())

# convert to tuple
print(student.items())
# remove one item from the dictionary
print("Deleted item is",student.pop('City'))

#delete the dictionary
del student
print("The dictionary has been deleted")
print(student)
