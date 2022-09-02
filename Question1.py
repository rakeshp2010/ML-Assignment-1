ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
#sorting ages
ages.sort()
print(ages)

#minimum min(ages)
print("Minimum of list",min(ages))

#maximum max(ages)
print("maximum of list",max(ages))

#Add min age and Max age to list
ages.append(19)
print(ages)
ages.append(26)
print(ages)

# Import statistics Library
import statistics

# Calculate middle values
statistics.median(ages)     
print(statistics.median(ages))

#find the average age(sum of all items divided by their number)
#sum() and len() in built funcyions in python used to find average
avg = sum(ages)/len(ages)
print("Average",round(avg,2))

#find the range of the ages (max minus min)
range = max(ages) - min(ages)
print(range)