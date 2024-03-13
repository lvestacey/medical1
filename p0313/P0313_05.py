# import random

from random import *

print(random.random())

print(random.uniform(10,20))

print(random.randrange(1,3))

print(random.choice([1,2,3,4,5]))

#리스트 내에 
print(random.sample([1,2,3,4,5],k=5))

# print(math.sin(1))
a_list=[1,2,3,4,5]
random.shuffle(a_list)
print(a_list)

print(random.randint(1,10))