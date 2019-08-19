#import tensorflow as tf
#import matplotlib.pyplot as plt
#import numpy as np
#from mpl_toolkits.mplot3d import Axes3D
#import math,sympy
#import time,os,sys, 
#import requests,re
#with open    as file:
#import turtle as tt
import math
import random

a= list(range(0,1000))
random.shuffle(a)
count = [0]*len(a)
out = [0]*len(a)
print(a)
for i in a:
    count[i] = count[i]+1
for i in range(len(a)):      
    if i ==0:
        count[i]=count[i]
    else:
        count[i]=count[i]+count[i-1]
print(count)
for j in range(len(a)):
    out[count[a[j]]-1]=a[j]
    count[a[j]]=count[a[j]]-1
print(out)
    
