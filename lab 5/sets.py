A={19,22,24,20,25,26}
B={19,22,20,25,26,24,28,27}
print("Set A:",A)
print("Set B:",B)
# join two sets
C=A.union(B)
print("Join",C)

#intersection
print("Intersection:",A.intersection(B))

#subset checking
print("Set A is subset of set B :",A.issubset(B))

#disjoint sets
print("Set A and Set B are disjoint Set :",A.isdisjoint(B))


# join A with B
print("Join A with B :",A.union(B))
#join B with A
print("Join B with A:",B.union(A))

#Symmetric difference
print("Symmetric difference between SET A and SET B:",A.symmetric_difference(B))

# delete the Set A completely
del A
print("The set has been deleted")
print(A)
