#numpy review

import numpy as np
A = np.random.normal(25, 5, 10)
print(a)

#list review
x = [1, 2, 3, 4, 5, 6]

print(x[3])     #only that index
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
