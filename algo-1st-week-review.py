#numpy review
import numpy as np
A = np.random.normal(25, 5, 10)
print(A)

#list review
x = [1, 2, 3, 4, 5, 6]

print(x[3])     #to show only the following index
print(x[3:])    #index 3 till last
print(x[2:5])   #index 2 to 5
print(x[:4])    #show index 0 to below 4

#adding list to list

x.extend([7,8])
print(x)
x.append(9)     #append() only have one argument, not like extend() that able do more
print(x)

y = [10, 11, 12]    #adding another list ffs
listoflists = (x,y)
print(listoflists)

#dictionaries
captains = {}
captains["Enterprise"] = "James T. Kirk"
captains["Arcadia"] = "Harlock"
captains["Black Pearl"] = "Barbosa"

print(captains["Black Pearl"])  #just to print one
for ship in captains:           #use this loop to print all
    print(ship + " : " + captains[ship])
