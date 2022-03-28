#Suppose there are 4 cars, A, B, C, and D. D is chased by B, C is chased by A, B is chased by C, A is chased by D.
#Initial positions of A, B, C, and D are (10,0), (0,10), (10,10) and (0,0). Velocities of A, B, C, and D are 3, 5, 7, and 2 ms-1.  
#Now Simulate this Chase Problem for t=20 unit time. 
#Print the x and y coordinate value of each vehicle at every time step. If the distance between any 2 vehicles is less than 5 m then a car will shoot its target [not destroy]. 
#Print all the shootings and finally print the number of times each car got shot during the simulation.  
#Also, draw the graph showing the path of each car.  Use plt.plot() function to do this. 

import math as m
import matplotlib.pyplot as plt

x_A = [10]
y_A = [0]
x_B = [0]
y_B = [10]
x_C = [10]
y_C = [10]
x_D = [0]
y_D = [0]
v_A = 3
v_B = 5
v_C = 7
v_D = 2

C_to_A = []
D_to_B = []
B_to_C = []
A_to_D = []

shoot_A = 0
shoot_B = 0
shoot_C = 0
shoot_D = 0

for t in range(0, 20):
  D_to_B.append(m.sqrt( m.pow((x_D[t]-x_B[t]),2) + m.pow((y_D[t]-y_B[t]),2)))
  C_to_A.append(m.sqrt( m.pow((x_C[t]-x_A[t]),2) + m.pow((y_C[t]-y_A[t]),2)))
  B_to_C.append(m.sqrt( m.pow((x_B[t]-x_C[t]),2) + m.pow((y_B[t]-y_C[t]),2)))
  A_to_D.append(m.sqrt( m.pow((x_A[t]-x_D[t]),2) + m.pow((y_A[t]-y_D[t]),2)))

  print("At time = ", t)
  print("x_A = ",x_A[t],"y_A = ",y_A[t])
  print("x_B = ",x_B[t],"y_B = ",y_B[t])
  print("x_C = ",x_C[t],"y_C = ",y_C[t])
  print("x_D = ",x_D[t], "y_D = ",y_D[t])
  
  print("D to B Distance=", D_to_B[t])
  print("C to A Distance=", C_to_A[t])
  print("B to C Distance=", B_to_C[t])
  print("A to D Distance=", A_to_D[t])
  
  if D_to_B[t]<5:
    shoot_D+=1
    print("Car B shoots Car D at time= ", t)
  if C_to_A[t]<5:
    shoot_C+=1
    print("Car A shoots Car C at time= ", t)
  if B_to_C[t]<5:
    shoot_B+=1
    print("Car C shoots Car B at time= ", t)
  if A_to_D[t]<5:
    shoot_A+=1
    print("Car D shoots Car A at time= ", t)
    
  sin = (y_C[t] - y_A[t])/C_to_A[t]
  cos = (x_C[t] - x_A[t])/C_to_A[t]
  x_A.append(x_A[t] + v_A * cos)
  y_A.append(y_A[t] + v_A * sin)

  sin = (y_D[t] - y_B[t]) / D_to_B[t]
  cos = (x_D[t] - x_B[t]) / D_to_B[t]
  x_B.append(x_B[t] + v_B * cos)
  y_B.append(y_B[t] + v_B * sin)
  
  sin = (y_B[t] - y_C[t]) / B_to_C[t]
  cos = (x_B[t] - x_C[t]) / B_to_C[t]
  x_C.append(x_C[t] + v_C * cos)
  y_C.append(y_C[t] + v_C * sin)

  sin = (y_A[t] - y_D[t]) / A_to_D[t]
  cos = (x_A[t] - x_D[t]) / A_to_D[t]
  x_D.append(x_D[t] + v_D * cos)
  y_D.append(y_D[t] + v_D * sin)

print("Car A has shot for ",shoot_A," times")
print("Car B has shot for ",shoot_B," times")
print("Car C has shot for ",shoot_C," times")
print("Car D has shot for ",shoot_D," times")

plt.plot(x_A, y_A, color="blue", label="Path A")
plt.plot(x_B, y_B, color="orange", label="Path B")    
plt.plot(x_C, y_C, color="green", label="Path C")
plt.plot(x_D, y_D, color="red", label="Path D")

plt.show()