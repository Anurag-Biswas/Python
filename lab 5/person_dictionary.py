person={'first_name':'Asabeneh',
         'last_name':'Yetayeh',
         'gender':'Male',
         'age':250,
        'country':'Finland',
         'is_married':'True',
         'skills':['javaScript','React','Node','MongoDB','Python'],
         'Address':{'street':'Space street','Zipcode':'02210'}
        }
print(person)

for i in person.keys():
   if i=='skills':
      l=len(i)
      print("The middle element of the skill:",person['skills'][l//2])

for i in person.keys():
   if i=='skills':
      for j in person['skills']:
         if j=='Python':
            print("Python skill is present")
            break

      else:
         print("Python skill is not present")


# conditions

if len(person['skills'])==2 and 'javaScript' in person['skills'] and 'React' in person['skills']:
   print("He is front end developer")
elif 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
   print("He is a fullstack developer")
else:
   print("Unknown Title")

# format
if person['is_married']=='True' and person['country']=='Finland':
   print(person['first_name']," ",person['last_name']," lives in ",person['country'],".He is married")
