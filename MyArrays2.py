import numpy as np

''' grades = np.array([[87,96,70], [100,87,90],[100,87,90], [94,77,90],[100,81,82]])

print(grades.sum())
print(grades.min())
print(grades.max())
print(grades.mean())
print(grades.std())
print(grades.var())

print(grades.mean(axis = 0))  # shows mean per row --> shows the averages of each element in the array. So the 1st is the average of the 1st item, etc.

print(grades.mean(axis = 1))  # shows mean per column --> shows the averages for each student (so for each column value in each element)

numbers = np.array([1,4,9,16,25,36])

print(np.sqrt(numbers)) ## square root of eveyr number in the array

numbers2 = np.arange(1,7) * 10

print(numbers2) ## multiplies ever number from 1-7 by 10

print(np.add(numbers, numbers2)) # universal function to add arrays

print(np.multiply(numbers2, 5))

#Reshape numbers2 into a 2-by-3 array


numbers3 = numbers2.reshape(2,3)
print(numbers3) ### 2 rows, 3 columns

numbers4 = np.array([2,4,6])
print(np.multiply(numbers3, numbers4)) #then multiply its values bz a one-dimensional array of three elements
### it multiplied it by column 

grades = np.array([[87,96,70], [100,87,90],[100,87,90], [94,77,90],[100,81,82]])

print(grades[0][1]) ## first row, second column
print(grades[1]) # second row

print(grades[:2]) # row 1 and 2

print(grades[[1,3]]) # row two and 4 (have to use a list)

print(grades[:,0]) ## only takes 1st value of each sublist

print(grades[:, 1:3]) #second and third value of each row

print(grades[:,[0,2]]) ## first and third
'''
'''
##################### Shallow copies
numbers = np.arange(1,6)
numbers2 = numbers.view() ### whatever is changed in oneview affects the other

print(numbers2)

numbers[1] *= 10

print(numbers2) ## we made a change to numbers, but numbers2 got affected by it as well

numbers2[1] /= 5
print(numbers)  ### change on numbers2, and it affected numbers

numbers2 = numbers[0:3]
print(numbers2)
numbers[1] *= 20
print(numbers2)    ### when  you make a slice, it makes a view (shallow copy)

################## Deep copies
numbers2 = numbers.copy()

grades = np.array([[87,96,70], [100,87,90]])

print(grades.reshape(1,6)) ### creates a shallow copy (view)
print(grades)

grades.resize(1,6)
print(grades)

flattened = grades.flatten()
print(flattened)   ### produces a flattened DEEP copy

raveled = grades.ravel()
print(raveled) ## produces flattened SHALLOW copy

raveled[5] = 90
print(grades)

grades2 = grades.T  ### doesnt affect original 
print(grades2)
print(grades)
'''
grades = np.array([[87,96,70], [100,87,90]])
grades2 = np.array([[94,77,90],[100,81,82]])

######### Horizontal stack
h_grades = np.hstack((grades,grades2))
print(h_grades)

######### Vertical stack 
v_grades = np.vstack((grades,grades2))
print(v_grades)