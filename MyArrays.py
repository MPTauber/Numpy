## pip install numpy --user
## ctrl, SHIFT,P --> Python: Start REPL
import numpy as np
'''integers = np.array([x for x in range(2,21,2)]) ## gives even number (third values means steps of 2)
print(integers)

two_dim = np.array([[1,2,3],[4,5,6]]) ## dont forget inital [] around the two sets of bracketed lists 
print(two_dim)

## Find the type fo elements in array
print(integers.dtype)
## Find the number of dimensions
print(two_dim.ndim)
## Find shape
print(two_dim.shape)
## Find total number of elements in array
print(two_dim.size)
##Find number of bytes of item
print(two_dim.itemsize) ## byte PER ITEM --> since it's 4, the whole array takes up 24 bytes (since 4x6 = 24)

##### CTRL+K+C comments out block

print(np.full((3,5),13)) # np.full() let's zou specify number (13 in our case). Produces 3 rows, 5 elements of the number 13

print(np.arange(5)) # makes a range 0-4

print(np.arange(5,10)) # starts at 5, ends at 9

print(np.arange(5,1,-2)) # starts at 5 and goes down in increments of 2

print(np.linspace(0.0,1.0,num=6))

array1 = np.arange(1,21) # makes range from 1-20
print(array1)
array2 = array1.reshape(4,5)  ## arranges arra1 in shape of 4 rows, 5 items each
print(array2)

array3 = np.arange(1,100_001).reshape(4,25_000) ## shapes numbers 1-100,000 into an array of 4 rows and 25,000 columns.
### This doesnt show middle because it's too large
print(array3)

array4 = np.arange(1,100_001).reshape(100,1000)
print(array4) '''

numbers = np.arange(1,6)
print(numbers**2)

# numbers += 10
# print(numbers)

numbers2 = np.linspace(1.1,5.5,5)
print(numbers2)
print (numbers * numbers2)

print(numbers >= 3) #gives logical array 
print(numbers2 < numbers)
