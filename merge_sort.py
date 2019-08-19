#import tensorflow as tf
#import matplotlib.pyplot as plt
#import numpy as np
#from mpl_toolkits.mplot3d import Axes3D
import math
import random

a = math.inf
left = []
right = []
numbers = [i for i in range(128)]
random.shuffle(numbers)
total = len(numbers)
for j in range(math.floor(total/2)):
    left.append(numbers[j])

for k in range(math.ceil(total/2),total):
    right.append(numbers[k])
left.append(a)
right.append(a)

print(left)
print(right)
i,j,k = 0,0,0

for k in range(total):
    if left[i]>=right[j]:
        numbers[k]=right[j]
        j=j+1
    else:
        numbers[k]=left[i]
        i = i+1
    k =k+1
print(numbers)

