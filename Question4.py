
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
 
#length of IT companies set
CountIT = len(it_companies)
print("Total IT companies ",CountIT)    
#adding twitter to set
it_companies.add("Twitter") 
print("Added new Company ",it_companies)
it_companies.update(["Capgemini","Chase","BOK_Fin"])
print("Added multiple companies ",it_companies)
it_companies.remove("BOK_Fin")
print("After removing one values ",it_companies)
#----
# difference between remove and discard ? ----- Ans :remove() method will raise an error if the specified item does not exist, and the discard() method will not.
#----
AB_Joined=A.union(B)
print("A Union B ",AB_Joined)
AB_INtersection=A.intersection(B)

print("A Intersection B ",AB_INtersection)
print("is A is subset of B :",A.issubset(B))
print("is A and B are disjoint sets :",A.isdisjoint(B))
print("the symmetric difference between A and B :",A.symmetric_difference(B))
print("deleting set A and B ", A.clear(), B.clear())
AgeSet=set(age)                    #--converting age list to a set
print("converted age list to set ",AgeSet)
print("Comparing the length of the list and the set by making difference between length of age list and length of age set is ",len(age)-len(AgeSet)) #--comparing lengths of the list and set