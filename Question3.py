#Brothers tuple
brothers=("Akhil","Durga","satish")  
print("brothers: ", brothers)
print(type(brothers))

#Sisters tuple
sisters=("manga","harini","usha") 
print("sisters: ", sisters)
print(type(sisters))

#Siblings tuple copy by adding                                                            
siblings=brothers+sisters                                                                     
print("my siblings are ",siblings)  

#How many siblings do you have
print("I have ",len(siblings), " siblings")

#Modifying the siblings tuple and setting it to family_members tuple
siblings=siblings+("Mahesh","Latha")  
family_members=siblings
print(family_members)                                   