import matplotlib.pyplot as plt
import re

r, q, l = 3, 5, 4
b = []
W, U, N = [], [], []
numbers = 1000 * l
for i in range(q):
  b.append(1)
for i in range(5, numbers+1):
  b.append(b[i-r] ^ b[i-q])
for i in range(0, numbers, 4):
  bit = b[i]*1000 + b[i+1]*100 + b[i+2]*10 + b[i+3]
  W.append(int(str(bit),2))
for i in range(len(W)):
  U.append(W[i]/(2**l))
  N.append(i+1)
print(W)
print(U)
plt.bar(N, U)
plt.xlabel('index of random number i')
plt.ylabel('random number Ui')
plt.show()
cycle = ''
for i in range(len(W)-1):
  cycle += str(W[i]) + " "
cycle += str(W[-1])
regex = re.compile(r'(.+ .+)( \1)+')
match = regex.search(cycle)
if match.group(1):
  print("Cycle Arived!!")