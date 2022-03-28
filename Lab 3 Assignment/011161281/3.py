#3. Find the area under the curve below using the monte Carlo simulation. Use the drawn rectangle.
#   Equation of curve - (i) is : y2 = 4x
#   Equation of (ii) is: y = 8 - x
#   Simulate this area for n=100,1000,5000,10000 trials. For each value of n, print the area and scatter plot.

#Monte Carlo

import math as m
import numpy as np
import random
import matplotlib.pyplot as plt
random.seed(0)

hits_Values = []
n = [100, 1000, 5000, 10000]

pointX, pointY = 8, 4

area_under_curve = []

for j in range(len(n)):
  hits = 0
  hits_x = []
  hits_y = []
  miss_x = []
  miss_y = []
  for i in range(0,n[j],1): 
    x =  random.uniform(0, pointX)
    y =  random.uniform(0, pointY)
    shade1 = m.sqrt(4 * x)
    shade2 = 8 - x
    if ((x<4 and y<=shade1) or (x>4 and y<=shade2)) or x==4:
      hits+=1
      hits_x.append(x)
      hits_y.append(y)
    else:
      miss_x.append(x)
      miss_y.append(y)
  hits_Values.append(hits)
  area = (pointX*pointY) * (hits/n[j])
  area_under_curve.append(area)
  print("Value of Shaded Area for " +str(n[j])+" trials : ", area_under_curve[j])
  plt.title('Area under the curve of the graph for '+str(n[j])+' trials')
  plt.scatter(hits_x, hits_y, color='red', label="Hit Points")
  plt.scatter(miss_x, miss_y, color='green', label="Miss Points")
  plt.legend(loc='upper right')
  plt.show()

N = ['100', '1000', '5000', '10000']
plt.bar(N, area_under_curve)
plt.xlabel('number of trials') 
plt.ylabel('Area under  curve') 
plt.ylim(0,20)
plt.title('1. Area under the Curve') 
plt.show()