import matplotlib.pyplot as plt
import math as m

trials = [100, 1000, 5000]

for trial in range(len(trials)):
  Z1 = [12, 7]
  U1 = []
  Z2 = [3, 5]
  U2 = []
  Z3 = [2, 7]
  U3 = []
  U = []

  for t in range(2, trials[trial]+2):
    new_z_1 = (13*Z1[t-1] + 11*Z1[t-2] + 3) % 16
    new_u_1 = new_z_1 / 16
    Z1.append(new_z_1)
    U1.append(new_u_1)

    new_z_2 = (12*m.pow(Z2[t-1],2) + 13*Z2[t-2]) % 17
    new_u_2 = new_z_2 / 17
    Z2.append(new_z_2)
    U2.append(new_u_2)

    new_z_3 = (m.pow(Z3[t-1],3) + m.pow(Z3[t-2],2)) % 15
    new_u_3 = new_z_3 / 15
    Z3.append(new_z_3)
    U3.append(new_u_3)

  for i in range(trials[trial]):
    if U1[i]+U2[i]+U3[i]<=1:
      U.append(U1[i]+U2[i]+U3[i])
    else:
      U.append((U1[i]+U2[i]+U3[i])-int(U1[i]+U2[i]+U3[i]))

  print("For trial ",trials[trial],":")
  print("U:",U)
  Trial = []
  for i in range(trials[trial]):
    Trial.append(i+1)
  
  plt.bar(Trial, U)
  plt.xlabel('Index of a random number i')
  plt.ylabel('Random number Ui')
  plt.show()