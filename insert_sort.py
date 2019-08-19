import time 
import random

numbers = [i for i in range(10000)]
random.shuffle(numbers)
print(numbers)

t1 = time.time()

total = len(numbers)

for i in range(1,total):
    key = numbers[i]
    j = i-1
    while j>=0 and key < numbers[j]:
        numbers[j+1] = numbers[j]
        numbers[j] = key
        j = j-1
        
t2 = time.time()
t = t2-t1
print(numbers)
print("time:",t)
