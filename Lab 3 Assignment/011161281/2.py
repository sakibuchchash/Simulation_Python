#2. Find the area of the shaded part below using the monte Carlo simulation.
#   Simulate this area for n=100,1000,5000,10000 trials. For each value of n, print the area and scatter plot.

#Monte Carlo

import math as m
import numpy as np
import random
import matplotlib.pyplot as plt
random.seed(0)

hits_Values = []
n = [100, 1000, 5000, 10000]

pointX, pointY = 3, 5

shaded_area = []

for j in range(len(n)):
  hits = 0
  hits_x = []
  hits_y = []
  miss_x = []
  miss_y = []
  for i in range(0,n[j],1): 
    x =  random.uniform(0, pointX)
    y =  random.uniform(0, pointY)
    length = x + 2
    if y<=length:
      hits+=1
      hits_x.append(x)
      hits_y.append(y)
    else:
      miss_x.append(x)
      miss_y.append(y)
  hits_Values.append(hits)
  area = (pointX*pointY) * hits/n[j]
  shaded_area.append(area)
  print("Value of Shaded Area for " +str(n[j])+" trials : ", shaded_area[j])
  plt.title('Area of the shaded part of the graph for '+str(n[j])+' trials')
  plt.scatter(hits_x, hits_y, color='red', label="Hit Points")
  plt.scatter(miss_x, miss_y, color='green', label="Miss Points")
  plt.legend(loc='upper right')
  plt.show()

N = ['100', '1000', '5000', '10000']
plt.bar(N, shaded_area)
plt.xlabel('number of trials') 
plt.ylabel('Area of Shade Area') 
plt.ylim(0,12)
plt.title('1. Area of the Shaded Part') 
plt.show()