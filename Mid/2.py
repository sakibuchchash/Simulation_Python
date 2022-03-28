import math
import numpy as np
import random
import matplotlib.pyplot as plt
random.seed(0)

hits_Values = []
n = [1000, 5000, 10000]

a, b = 8, 4
errorValue = []
for i in range(len(n)):
  f_sum = 0
  f_square_sum = 0
  for j in range(n[i]):
    x = random.uniform(0, a)
    y = random.uniform(0, b)
    functionV1 = math.sqrt(4 * x)
    functionV2 = 8-x
    if x<=4 and y<=functionV1:
      f_sum += functionV1
      f_square_sum += (functionV1**2)
    elif x>=4 and y<=functionV2:
      f_sum += functionV2
      f_square_sum += (functionV2**2)
  f_avg = f_sum/n[i]
  f_square_avg = f_square_sum/n[i]
  error = ((b-a)/math.sqrt(n[i])) * math.sqrt(f_square_avg - (f_avg**2))
  Integral = (b-a) * f_avg
  errorValue.append(error)
  print(n[i], Integral, errorValue[i])

N = ['1000', '5000', '10000']
plt.bar(N, errorValue)
plt.xlabel('The number of trials') 
plt.ylabel('Estimated error value') 
plt.show()