#Creating an empty dictionary dog
dog = ()   
print(type(dog))

#adding given items as keys and empty values to dictionary                                                                                                    
dog={"Name":"Rocky","Color":"Black","Breed":"GSD","Legs":"4","Age":"7"} 
print(dog)
                               
#Creating an student dictionary      
student=()                         
student={"first_name":"Rakesh","last_name":"Peddapalli",                          
"gender":"male","age":26,"maritial_status":"Unmarried","skills":["Coding ,testimg"],
"country":"India","city":"Hyderabad","address":"6655 W kansas"}
print(student)

#length of the student dictionary
print(len(student))

#get the value of skills and check the data type, it should be a list
student["skills"]
print(type(student["skills"]))

#modifying the skills values by adding one or two skills
student["skills"].append("Machine learning python")
print(student["skills"])

#get the dictionary keys as a list
print (list(student.keys()))

#get the dictionsry values as list
print (list(student.values()))




