#A is chased by C, C is chased by D, D is chased by B and B is chased by A

import math
import matplotlib.pyplot as plt

x_A, y_A =  [-10], [0]
x_B, y_B =  [0], [-10]
x_C, y_C =  [-10], [-10]
x_D, y_D =  [0], [0]
v_A, v_B, v_C, v_D = 3, 5, 7, 4

dist_AC = []
dist_CD = []
dist_DB = []
dist_BA = []

T = 10
C_shooting_A, D_shooting_C, B_shooting_D, A_shooting_B = 0, 0, 0, 0

for t in range(0, T):
  dist_AC.append(math.sqrt((x_A[t]-x_C[t])**2 + (y_A[t]-y_C[t])**2))
  dist_CD.append(math.sqrt((x_C[t]-x_D[t])**2 + (y_C[t]-y_D[t])**2))
  dist_DB.append(math.sqrt((x_D[t]-x_B[t])**2 + (y_D[t]-y_B[t])**2))
  dist_BA.append(math.sqrt((x_B[t]-x_A[t])**2 + (y_B[t]-y_A[t])**2))

  print("At time = ", t)
  print("x_A = ",x_A[t],"y_A = ",y_A[t])
  print("x_B = ",x_B[t],"y_B = ",y_B[t])
  print("x_C = ",x_C[t],"y_C = ",y_C[t])
  print("x_D = ",x_D[t], "y_D = ",y_D[t])
  
  print("A to C Distance=", dist_AC[t])
  print("C to D Distance=", dist_CD[t])
  print("D to B Distance=", dist_DB[t])
  print("B to A Distance=", dist_BA[t])

  shoot = 4.5
  
  if dist_AC[t]<shoot:
    C_shooting_A+=1
    print("Car C shoots Car A at time= ", t)
  if dist_CD[t]<shoot:
    D_shooting_C+=1
    print("Car D shoots Car C at time= ", t)
  if dist_DB[t]<shoot:
    B_shooting_D+=1
    print("Car B shoots Car D at time= ", t)
  if dist_BA[t]<shoot:
    A_shooting_B+=1
    print("Car A shoots Car B at time= ", t)
    

  sin = (y_A[t] - y_C[t]) / dist_AC[t]
  cos = (x_A[t] - x_C[t]) / dist_AC[t]
  x_Cnew = x_C[t] + v_C * cos
  y_Cnew = y_C[t] + v_C * sin
  x_C.append(x_Cnew)
  y_C.append(y_Cnew)

  sin = (y_C[t] - y_D[t]) / dist_CD[t]
  cos = (x_C[t] - x_D[t]) / dist_CD[t]
  x_Dnew = x_D[t] + v_D * cos
  y_Dnew = y_D[t] + v_D * sin
  x_D.append(x_Dnew)
  y_D.append(y_Dnew)
  
  sin = (y_D[t] - y_B[t]) / dist_DB[t]
  cos = (x_D[t] - x_B[t]) / dist_DB[t]
  x_Bnew = x_B[t] + v_B * cos
  y_Bnew = y_B[t] + v_B * sin
  x_B.append(x_Bnew)
  y_B.append(y_Bnew)

  sin = (y_B[t] - y_A[t]) / dist_BA[t]
  cos = (x_B[t] - x_A[t]) / dist_BA[t]
  x_Anew = x_A[t] + v_A * cos
  y_Anew = y_A[t] + v_A * sin
  x_A.append(x_Anew)
  y_A.append(y_Anew)

print("Car A got shoot for ",C_shooting_A," times")
print("Car B got shoot for ",A_shooting_B," times")
print("Car C got shoot for ",D_shooting_C," times")
print("Car D got shoot for ",B_shooting_D," times")
