import matplotlib.pyplot as plt
import re

r = 3
q = 5
l = 4

b = []
W = []
U = []
Trial = []

for i in range(0, q):
  b.append(1)

for i in range(5, (1000 * l)+1):
  b.append(b[i-r] ^ b[i-q])

for i in range(0, (1000 * l), 4):
  binary_number = b[i]*1000 + b[i+1]*100 + b[i+2]*10 + b[i+3]
  W.append(int(str(binary_number),2))

for i in range(len(W)):
  U.append(W[i]/(2**l))
  Trial.append(i+1)

print("U: ", U)
plt.bar(Trial, U)

plt.xlabel('Index of random number i')
plt.ylabel('Random number Ui')
plt.show()

isCycle = ""
for i in range(len(U)):
  if i==len(U)-1:
    isCycle += str(U[i])
  isCycle += str(U[i]) + " "
regex = re.compile(r'(.+ .+)( \1)+')
match = regex.search(isCycle)
if match.group(1):
  print("Yes, cycle Arives in random numbers!!")