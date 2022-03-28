#D is chased by B
#C is chased by A
#B is chased by C
#A is chased by D

import math
import matplotlib.pyplot as plt

x_A, y_A =  [10], [0]
x_B, y_B =  [0], [10]
x_C, y_C =  [10], [10]
x_D, y_D =  [0], [0]
v_A, v_B, v_C, v_D = 3, 5, 7, 2

dist_DB = []
dist_CA = []
dist_BC = []
dist_AD = []

T = 20
B_shooting_D, A_shooting_C, C_shooting_B, D_shooting_A = 0, 0, 0, 0

for t in range(0, T):
  dist_DB.append(math.sqrt((x_D[t]-x_B[t])**2 + (y_D[t]-y_B[t])**2))
  dist_CA.append(math.sqrt((x_C[t]-x_A[t])**2 + (y_C[t]-y_A[t])**2))
  dist_BC.append(math.sqrt((x_B[t]-x_C[t])**2 + (y_B[t]-y_C[t])**2))
  dist_AD.append(math.sqrt((x_A[t]-x_D[t])**2 + (y_A[t]-y_D[t])**2))

  print("At time = ", t)
  print("x_A = ",x_A[t],"y_A = ",y_A[t])
  print("x_B = ",x_B[t],"y_B = ",y_B[t])
  print("x_C = ",x_C[t],"y_C = ",y_C[t])
  print("x_D = ",x_D[t], "y_D = ",y_D[t])
  
  print("D to B Distance=", dist_DB[t])
  print("C to A Distance=", dist_CA[t])
  print("B to C Distance=", dist_BC[t])
  print("A to D Distance=", dist_AD[t])

  shoot = 5
  
  if dist_DB[t]<shoot:
    B_shooting_D+=1
    print("Car B shoots Car D at time= ", t)
  if dist_CA[t]<shoot:
    A_shooting_C+=1
    print("Car A shoots Car C at time= ", t)
  if dist_BC[t]<shoot:
    C_shooting_B+=1
    print("Car C shoots Car B at time= ", t)
  if dist_AD[t]<shoot:
    D_shooting_A+=1
    print("Car D shoots Car A at time= ", t)
    

  sin = (y_D[t] - y_B[t]) / dist_DB[t]
  cos = (x_D[t] - x_B[t]) / dist_DB[t]
  x_Bnew = x_B[t] + v_B * cos
  y_Bnew = y_B[t] + v_B * sin
  x_B.append(x_Bnew)
  y_B.append(y_Bnew)

  sin = (y_C[t] - y_A[t]) / dist_CA[t]
  cos = (x_C[t] - x_A[t]) / dist_CA[t]
  
  x_Anew = x_A[t] + v_A*cos
  y_Anew = y_A[t] + v_A*sin
  x_A.append(x_Anew)
  y_A.append(y_Anew)
  
  sin = (y_B[t] - y_C[t]) / dist_BC[t]
  cos = (x_B[t] - x_C[t]) / dist_BC[t]
  x_Cnew = x_C[t] + v_C * cos
  y_Cnew = y_C[t] + v_C * sin
  x_C.append(x_Cnew)
  y_C.append(y_Cnew)

  sin = (y_A[t] - y_D[t]) / dist_AD[t]
  cos = (x_A[t] - x_D[t]) / dist_AD[t]
  x_Dnew = x_D[t] + v_D * cos
  y_Dnew = y_D[t] + v_D * sin
  x_D.append(x_Dnew)
  y_D.append(y_Dnew)

print("Car A got shoot for ",D_shooting_A," times")
print("Car B got shoot for ",C_shooting_B," times")
print("Car C got shoot for ",A_shooting_C," times")
print("Car D got shoot for ",B_shooting_D," times")

plt.plot(x_A, y_A, color="blue", label="Path A")
plt.plot(x_B, y_B, color="orange", label="Path B")    
plt.plot(x_C, y_C, color="green", label="Path C")
plt.plot(x_D, y_D, color="red", label="Path D")

plt.show()