import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)

m = int(input("Maximum Inventory: ")) #maximum capacity
n = int(input("review period: ")) #review period
print("")

begining_inventory = 3
ending_inventory = 0
shortage_quantity = 0
order_quantity = 8
days_until_order_arrives = 2
total_ending_inventory = 0
shortage_occuring_days = 0
cycles = 10

ending_inventory_each_day = []

for cycle in range(1, cycles+1):
  print("Cycle no: ", cycle)
  for day in range(1, n+1):
    #order arrives case
    if days_until_order_arrives==0:
      begining_inventory += order_quantity
      order_quantity = 0
    else:
      days_until_order_arrives -= 1
    print(" Day no: ", day)
    print(" Begining Inventory: ", begining_inventory)
    daily_demand = np.random.choice(a=[0,1,2,3,4],p=[0.10,0.25,0.35,0.21,0.09])
    print(" Demand", daily_demand)
    total_demand = daily_demand + shortage_quantity
    if total_demand<begining_inventory:
      ending_inventory = begining_inventory-total_demand
      shortage_quantity = 0
    else:
      shortage_quantity = total_demand-begining_inventory
      ending_inventory = 0
    if shortage_quantity:
      shortage_occuring_days += 1
    print(" Ending_inventory: ", ending_inventory)
    print(" Shortage_quantity: ", shortage_quantity)
    ending_inventory_each_day.append(ending_inventory)
    begining_inventory = ending_inventory
    total_ending_inventory += ending_inventory
    #order place, lead time
    if day==n:
      days_until_order_arrives = np.random.choice(a=[1,2,3],p=[0.6,0.3,0.1])
      order_quantity = m - ending_inventory
      print(" Order Quantity: ", order_quantity)
      print(" Days until Order Arrives: ", days_until_order_arrives)
    else:
      print(" Order Quantity: null")
      print(" Days until Order Arrives: ", days_until_order_arrives)
    print("")
  print("")

#average_ending_inventory
print("Average Ending Inventory: ", total_ending_inventory/(n*cycles))

#how many days shortage occurs
print("Shortage occurs on ",shortage_occuring_days," of ",n*cycles," days")

#graph: ending_inventory vs day 
x_axis = []
for i in range(n*cycles):
  x_axis.append(i+1)
plt.plot(x_axis, ending_inventory_each_day)
plt.title('inventory_level vs day graph') 
plt.xlabel("day number")
plt.ylabel("Ending_inventory of each day")
plt.show()