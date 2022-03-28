import matplotlib.pyplot as plt

n = [100, 1000, 5000]
extra = 2

for test in range(len(n)):
  Z1, U1 = [12, 7], []
  Z2, U2 = [3, 5], []
  Z3, U3 = [2, 7], []
  U, N = [], []
  for i in range(2, n[test]+extra):
    new_z1 = (13*Z1[i-1] + 11*Z1[i-2] + 3) % 16
    new_u1 = new_z1 / 16
    Z1.append(new_z1)
    U1.append(new_u1)

    new_z2 = (12*(Z2[i-1]**2) + 13*Z2[i-2]) % 17
    new_u2 = new_z2 / 17
    Z2.append(new_z2)
    U2.append(new_u2)

    new_z3 = ((Z3[i-1]**3) + (Z3[i-2]**2)) % 15
    new_u3 = new_z3 / 15
    Z3.append(new_z3)
    U3.append(new_u3)

  for i in range(n[test]):
    if U1[i]+U2[i]+U3[i]>1:
      U.append((U1[i]+U2[i]+U3[i])-int(U1[i]+U2[i]+U3[i]))
    else:
      U.append(U1[i]+U2[i]+U3[i])

  print("When there are ",n[test]," random numbers:")
  print(U)
  for i in range(n[test]):
    N.append(i+1)
  plt.bar(N, U)
  plt.xlabel('index of a random number i')
  plt.ylabel('random number Ui')
  plt.show()