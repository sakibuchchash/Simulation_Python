import numpy as np
np.random.seed(0)

class SSQ:
  def __init__(self, n):
    #self.interarrivals= [0.4,1.2,0.5,1.7,0.2,1.6,0.2,1.4,1.9]
    #self.interarrivals= [0.8,1.6,0.5,2.2,1.3,0.7,0.5,1.9,1.8]
    #self.service_times= [2.0,0.7,0.2,1.1,3.7,0.6,0.8,0.4,1.2]
    self.interarrivals = list(np.random.exponential(1/3.0, n+1))
    self.service_times =list(np.random.exponential(1/4.0, n+1))
    print(self.interarrivals)
    print(self.service_times)
    self.clock = 0.0
    self.clock_prev = 0.0
    
    self.next_arrival = self.interarrivals.pop(0)
    self.next_departure_1 = float('inf')
    self.next_departure_2 = float('inf')

    self.num_in_queue = 0
    self.num_in_queue_prev = 0
    self.times_of_arrivalqueue = []
    self.service_times_in_queue = []
    
    self.total_delay = 0.0
    self.num_of_delays = 0.0
    self.area_under_q = 0.0
    self.area_under_b1 = 0.0
    self.area_under_b2 = 0.0
    
    self.server1_status = 0
    self.server1_prev_status = 0 
    self.server2_status = 0
    self.server2_prev_status = 0 
    self.last_event_time = 0.0


  def start(self, policy_type, n):
    self.policy = int(policy_type)
    while self.num_of_delays<=n:
      self.timing()
      if self.num_of_delays==n:
        break
    print("Average Delay: "+str("{:.2f}".format(self.total_delay/self.clock)))
    print("Expected Number of Customers in the queue: "+str("{:.2f}".format(self.area_under_q/self.clock)))
    print("Expected Utilization of the server-1: "+str("{:.2f}".format(self.area_under_b1/self.clock)))
    print("Expected Utilization of the server-2: "+str("{:.2f}".format(self.area_under_b2/self.clock)))
    print(" ")
  
  def timing(self):
    self.clock_prev = self.clock
    self.clock= min(self.next_arrival,self.next_departure_1,self.next_departure_2)
    self.server1_prev_status = self.server1_status
    self.server2_prev_status = self.server2_status

    if self.clock==self.next_arrival:
      print("Arrival at Clock: " +str(self.clock))
      self.arrival()

    elif self.clock==self.next_departure_1:
      print("Departure of 1st server at Clock: " +str(self.clock))
      self.departure_1()

    else:
      print("Departure of 2nd server at Clock: " +str(self.clock))
      self.departure_2()

    print("Server 1 Status: "+str(self.server1_status))
    print("Server 2 Status: "+str(self.server2_status))
    print("Times of arrivals in Queue: "+ str(self.times_of_arrivalqueue))
    print("Service times in Queue: "+str(self.service_times_in_queue))
    print("Number of Delays: "+str(self.num_of_delays))
    print("Total Delay: " +str(self.total_delay))
    print("Area under qt: " +str(self.area_under_q))
    print("Area under bt of 1st server: " +str(self.area_under_b1))
    print("Area under bt of 2nd server: " +str(self.area_under_b2))
    print("Next Arrival Time: "+str(self.next_arrival))
    print("Next Departure Time of 1st server: "+str(self.next_departure_1))
    print("Next Departure Time of 2nd server: "+str(self.next_departure_2))
    print(" ")


  
  def arrival(self):
    self.next_arrival+=self.interarrivals.pop(0)
    if self.server1_status==0:
      self.server1_status = 1
      delay = 0.0
      self.total_delay += delay  
      self.num_of_delays += 1
      q_area = (self.clock - self.clock_prev) * self.num_in_queue_prev
      self.area_under_q += q_area
      b1_area = (self.clock - self.clock_prev) * self.server1_prev_status
      self.area_under_b1 += b1_area
      b2_area = (self.clock - self.clock_prev) * self.server2_prev_status
      self.area_under_b2 += b2_area
      self.next_departure_1 = self.clock+ self.service_times.pop(0)
    
    elif self.server2_status==0:
      self.server2_status = 1
      delay = 0.0
      self.total_delay += delay  
      self.num_of_delays += 1
      q_area = (self.clock - self.clock_prev) * self.num_in_queue_prev
      self.area_under_q += q_area
      b1_area = (self.clock - self.clock_prev) * self.server1_prev_status
      self.area_under_b1 += b1_area
      b2_area = (self.clock - self.clock_prev) * self.server2_prev_status
      self.area_under_b2 += b2_area
      self.next_departure_2 = self.clock+ self.service_times.pop(0)
    
    else:
      self.num_in_queue_prev = self.num_in_queue
      self.num_in_queue+=1
      self.times_of_arrivalqueue.append(self.clock) 
      self.service_times_in_queue.append(self.service_times.pop(0))
      q_area = (self.clock - self.clock_prev) * self.num_in_queue_prev
      self.area_under_q += q_area
      b1_area = (self.clock - self.clock_prev) * self.server1_prev_status
      self.area_under_b1 += b1_area
      b2_area = (self.clock - self.clock_prev) * self.server2_prev_status
      self.area_under_b2 += b2_area 

  def departure_1(self):
    if self.num_in_queue==0:
      self.server1_prev_status = self.server1_status
      self.server1_status = 0
      self.next_departure_1= float('infinity')
      q_area = (self.clock - self.clock_prev) * self.num_in_queue_prev
      self.area_under_q += q_area
      b1_area = (self.clock - self.clock_prev) * self.server1_prev_status
      self.area_under_b1 += b1_area
      b2_area = (self.clock - self.clock_prev) * self.server2_prev_status
      self.area_under_b2 += b2_area
    
    else:
      self.num_in_queue_prev = self.num_in_queue
      self.num_in_queue-=1
      self.num_of_delays+=1
      #AS FIFO, pop first arrival and service time from the queue.
      if self.policy==1:
        arrival = self.times_of_arrivalqueue.pop(0)
        delay = self.clock - arrival
        self.total_delay += delay
        q_area = (self.clock - self.clock_prev) * self.num_in_queue_prev
        self.area_under_q += q_area
        b1_area = (self.clock - self.clock_prev) * self.server1_prev_status
        self.area_under_b1 += b1_area
        b2_area = (self.clock - self.clock_prev) * self.server2_prev_status
        self.area_under_b2 += b2_area
        self.next_departure_1 = self.clock + self.service_times_in_queue.pop(0)
      #For LIFO, pop last arrival and service time from the queue.
      elif self.policy==2:
        arrival = self.times_of_arrivalqueue.pop(-1)
        delay = self.clock - arrival
        self.total_delay+=delay
        q_area = (self.clock - self.clock_prev) * self.num_in_queue_prev
        self.area_under_q += q_area
        b1_area = (self.clock - self.clock_prev) * self.server1_prev_status
        self.area_under_b1 += b1_area
        b2_area = (self.clock - self.clock_prev) * self.server2_prev_status
        self.area_under_b2 += b2_area
        self.next_departure_1 = self.clock + self.service_times_in_queue.pop(-1)
      #For SJF, find the index of minimum service time from  service_times_in_queue list.
      else:
        minimum_service_time_index = self.service_times_in_queue.index(min(self.service_times_in_queue))
        arrival = self.times_of_arrivalqueue.pop(minimum_service_time_index)
        delay = self.clock - arrival
        self.total_delay += delay
        q_area = (self.clock - self.clock_prev) * self.num_in_queue_prev
        self.area_under_q += q_area
        b1_area = (self.clock - self.clock_prev) * self.server1_prev_status
        self.area_under_b1 += b1_area
        b2_area = (self.clock - self.clock_prev) * self.server2_prev_status
        self.area_under_b2 += b2_area
        self.next_departure_1 = self.clock + self.service_times_in_queue.pop(minimum_service_time_index)
      
  def departure_2(self):
    if self.num_in_queue==0:
      self.server2_prev_status = self.server2_status
      self.server2_status = 0
      self.next_departure_2= float('infinity')
      q_area = (self.clock - self.clock_prev) * self.num_in_queue_prev
      self.area_under_q += q_area
      b1_area = (self.clock - self.clock_prev) * self.server1_prev_status
      self.area_under_b1 += b1_area
      b2_area = (self.clock - self.clock_prev) * self.server2_prev_status
      self.area_under_b2 += b2_area
    
    else:
      self.num_in_queue_prev = self.num_in_queue
      self.num_in_queue-=1
      self.num_of_delays+=1
      #AS FIFO, pop first arrival and service time from the queue.
      if self.policy==1:
        arrival= self.times_of_arrivalqueue.pop(0)
        delay = self.clock - arrival
        self.total_delay+=delay
        q_area = (self.clock - self.clock_prev) * self.num_in_queue_prev
        self.area_under_q += q_area
        b1_area = (self.clock - self.clock_prev) * self.server1_prev_status
        self.area_under_b1 += b1_area
        b2_area = (self.clock - self.clock_prev) * self.server2_prev_status
        self.area_under_b2 += b2_area
        self.next_departure_2 = self.clock+ self.service_times_in_queue.pop(0)
      #For LIFO, pop last arrival and service time from the queue.
      elif self.policy==2:
        arrival= self.times_of_arrivalqueue.pop(-1)
        delay = self.clock - arrival
        self.total_delay+=delay
        q_area = (self.clock - self.clock_prev) * self.num_in_queue_prev
        self.area_under_q += q_area
        b1_area = (self.clock - self.clock_prev) * self.server1_prev_status
        self.area_under_b1 += b1_area
        b2_area = (self.clock - self.clock_prev) * self.server2_prev_status
        self.area_under_b2 += b2_area
        self.next_departure_2 = self.clock+ self.service_times_in_queue.pop(-1)
      #For SJF, find the index of minimum service time from  service_times_in_queue list.
      else:
        minimum_service_time_index = self.service_times_in_queue.index(min(self.service_times_in_queue))
        arrival= self.times_of_arrivalqueue.pop(minimum_service_time_index)
        delay = self.clock - arrival
        self.total_delay+=delay
        q_area = (self.clock - self.clock_prev) * self.num_in_queue_prev
        self.area_under_q += q_area
        b1_area = (self.clock - self.clock_prev) * self.server1_prev_status
        self.area_under_b1 += b1_area
        b2_area = (self.clock - self.clock_prev) * self.server2_prev_status
        self.area_under_b2 += b2_area
        self.next_departure_2 = self.clock+ self.service_times_in_queue.pop(minimum_service_time_index)
  
  def update_register(self):
    time_difference = self.clock - self.last_event_time
    last_event_time = self.clock


N = [10, 50, 100]
for i in range(len(N)):
  model=SSQ(N[i]) #create SSQ object; __init__ is called
  print("Press 1 for FIFO, 2 for LIFO, 3 for SJF")
  model.start(input(), N[i])