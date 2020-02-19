#CTRL+SHIFT+P then Start REPL
import numpy as np 
# >>> import numpy as np
# >>> integers = np.array([[1,2,3],[4,5,6]])
# >>> integers
# array([[1, 2, 3],
#        [4, 5, 6]])
# >>> for i in integers.flat:
# ...     print(i)
# ...
# 1
# 2
# 3
# 4
# 5
# 6
# >>>
#################################################CTRL+K+C ---> comment out block

# >>> np.zeros(5)                               ######## this makes array of zeros
# array([0., 0., 0., 0., 0.])
# >>> np.ones(5)                                ######## this makes array of ones
# array([1., 1., 1., 1., 1.])                   
# >>> np.ones((2,4), dtype=int)                 ######## this makes 2 rows, 4 columns each with integers
# array([[1, 1, 1, 1],
#        [1, 1, 1, 1]])


import time
import random

start_time_list = time.time()

lsit1 = [random.randrange(1,7) for i in range(0,10_000_000)] ## the _ acts as commas in 10,000,000

print("process finished  --- %s seconds ---" % (time.time() - start_time_list)) ### times how long it takes to run this list

start_time_array = time.time()
arrazy1 = np.random.randint(1,7,10_000_000)
print("process finished  --- %s seconds ---" % (time.time() - start_time_array)) ### times how long it takes to run this array

############### arrray was 8 seconds faster
############### because python was built on C arrays (or something like that)

