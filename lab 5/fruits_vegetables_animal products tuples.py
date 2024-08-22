fruits=('Mango','Banana','Apple','Lichi')
vegetables=('Potato','Tomato','Ladies finger')
animal=('Tiger','Deer','Lion','Monkey')

print("Friuts tuple:",fruits)
print('vegetables tuple:',vegetables)
print('animal tuple',animal)

#join 3 tuples
food_stuff_tp=fruits+vegetables+animal
print("Joined tuple:",food_stuff_tp)

# convert tuple to list
food_stuff_It=list(food_stuff_tp)
print("The converted list is:",food_stuff_It)

#middle item
lt=len(food_stuff_tp)
lst=len(food_stuff_It)
m1=lt//2
m2=lst//2
print("Middle element of tuple:",food_stuff_tp[m1])
print("Middle element of list:",food_stuff_It[m2])

#slice out 1st 3 items and last 3 items of list
print("The first 3 items:",food_stuff_It[0:4])
print("The last 3 items:",food_stuff_It[-1:-4:-1])

# to delete the tuple
