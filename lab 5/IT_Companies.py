It_companies={'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'}
A={19,22,24,20,25,26}
B={19,22,20,25,26,24,28,27}
age=[22,19,24,25,26,24,25,24]

#length of It_companies
print("Length of It companies:",len(It_companies))
It_companies.add("Twitter")
print("After adding :",It_companies)

#To add multiple IT companies
IT={"IBS","TCS","Wipro"}
It_companies.update(IT)
print("After adding multiple IT companies :", It_companies)

# To remove IBM from the IT companies
It_companies.remove("IBM")
print("After removing IBM the other software companies are: ",It_companies)

# The Difference between remove() and discard() is :-
#The remove() method will raise an error if the specified item does not exist.
#the discard() method will not raise any error if the item does not exist in the list.
