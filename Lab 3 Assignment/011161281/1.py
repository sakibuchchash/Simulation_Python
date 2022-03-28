#1. Using Monte Carlo simulation, find the value of PI and area of the circle using the given circle and square. You have to simulate the value for n=100,1000,5000 and 10000 trials.
#   Show the scatter plot, value of PI, value of the area  for each value of n. ( Just as shown in the class). At the end of the simulation, draw three-bar diagrams. 
#   First Bar Plot:  x-axis: number of trials, y-axis: PI -value (Shown in the class)
#   Second Bar Plot:  x-axis: number of trials, y-axis: Error value [ Error value = abs(estimated pi value - 3.1416) ]
#   Third Bar Plot:  x-axis: number of trials, y-axis: Area of the circle

#Monte Carlo

import math as m
import numpy as np
import random
import matplotlib.pyplot as plt
random.seed(0)

hits_Values = []
n = [100, 1000, 5000, 10000]
pi_Values = []
circlelength = 1.5
squarelength = 4

centerX, centerY = 2, 2

PI_error = []
circle_area = []

for j in range(len(n)):
  hits = 0
  hits_x = []
  hits_y = []
  miss_x = []
  miss_y = []
  for i in range(0,n[j],1): 
    x =  random.uniform(0, squarelength)
    y =  random.uniform(0, squarelength)
    length = m.sqrt((x-centerX)**2 + (y-centerY)**2)
    if length<=circlelength:
      hits+=1
      hits_x.append(x)
      hits_y.append(y)
    else:
      miss_x.append(x)
      miss_y.append(y)
  pi = ((squarelength**2)/(circlelength**2)) * (hits/n[j])
  pi_Values.append(pi)
  hits_Values.append(hits)
  PI_error.append(abs(pi-3.1416))
  area = (squarelength**2) * (hits/n[j])
  circle_area.append(area)
  print("Value of PI for " +str(n[j])+" trials : ", pi)
  print("Value of Area for " +str(n[j])+" trials : ", circle_area[j])
  plt.title('Scatter plot for hits and misses for '+str(n[j])+' trials')
  plt.scatter(hits_x, hits_y, color='red', label="Hit Points")
  plt.scatter(miss_x, miss_y, color='green', label="Miss Points")
  plt.legend(loc='upper right')
  plt.show()

#First Bar Plot
N = ['100', '1000', '5000', '10000']
plt.bar(N, pi_Values)
plt.xlabel('number of trials') 
plt.ylabel('value of PI') 
plt.ylim(0,5)
plt.title('1. PI values') 
plt.show()

#Second Bar Plot
plt.bar(N, PI_error)
plt.xlabel('number of trials') 
plt.ylabel('Error value') 
plt.ylim(0,0.5)
plt.title('2. Error value in PI') 
plt.show()

#Third Bar Plot
plt.bar(N, circle_area)
plt.xlabel('number of trials') 
plt.ylabel('Area of circle') 
plt.ylim(0,10)
plt.title('3. Area of the Circle') 
plt.show()