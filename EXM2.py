import numpy as np
from random import random
randnums= np.random.randint(-1000,101,5)
print("w",randnums)
x = 0
y = []
n = 3
a = 3
b = 20
#while(x <= 10):
#    y.append(int((random()*10 - 10) + 10 ))
#    x += 1
for i in range(0,n):
    temp = []
    for j in range(0,n):
        temp.append(int((random()*10 - 10) + 10 ))
    y.append(temp)
result = []
for i in range(0,n):
    for j in range(0,n):
        if (y[i][j] > a):
            result.append(y[i][j])
        print(y[i][j])


        
print('y=', result)
