from process import Process
from scheduling_algorithms import FCFS, SJF, SRTF, RR

# Function to output the calculated waiting times
def outputWaitingTimes(waiting_times, n):
    waiting_times.sort(key=lambda x: x.get_id())
    sum = 0
    for process in waiting_times:
        print(process)
        sum += process.get_waiting_time()
    print("Average waiting time: " + str(sum/n))


# CPU Scheduling Algorithm Options
print("CPU Scheduling Algorithm")
print("0 First Come First Serve")
print("1 Shortest Job First")
print("2 Shortest Remaining Time First")
print("3 Round Robin")

# Input
algo, n, q = [int(x) for x in input().split(" ")]
processes = []
for i in range(n):
    id, at, bt = input().split(" ")
    processes.append(Process(int(id), int(at), int(bt)))

# Algorithm
waiting_times = []
if algo == 0: 
    waiting_times = FCFS(processes)

elif algo == 1: 
    waiting_times = SJF(processes)

elif algo == 2: 
    waiting_times = SRTF(processes)
    
elif algo == 3: 
    waiting_times = RR(processes, q)

else:
    print("Invalid input")

# Output
if waiting_times:
    outputWaitingTimes(waiting_times, n)
    
