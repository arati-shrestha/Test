import random 
#used to generate pseudo random numbers

# a = random.random()
# print(a)

# a = random.uniform(1,10)
# print(a)
# b = random.randint(1,6)
# print(b)
# c= random.normalvariate(0,1)
# print(c)

# my_list = list("ABSJEOJKL")

# random.shuffle(my_list)
# print(my_list)

# random.seed(1)
# print(random.random())
# print(random.randint(1,10))
# random.seed(2)
# print(random.random())
# print(random.randint(1,10))

# import secrets #generates true random numbers
# #only three function '''
# # 1. randbelow
# # 2. randbit
# # 3. '''

# a = secrets.randbelow(10)
# print(a)
# a = secrets.randbits(4)
# print(a)

# my_list = list("ABCDEFGH")
# a = secrets.choice(my_list)
# print(a)

import numpy as np
a =np.random.randint(0,10,(3,3))
print(a)

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr)
np.random.shuffle(arr)
print(arr)

np.random.seed(1)
print(np.random.rand(3,3))



                  



