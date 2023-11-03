from process import Process
from scheduling_algorithms import FCFS, SRTF

def outputWaitingTimes(waiting_times, n):
    sum = 0
    for process in waiting_times:
        print(process)
        sum += process.get_waiting_time()
    print("Average waiting time: " + str(sum/n))


print("CPU Scheduling Algorithm")
print("0 First Come First Serve")
print("1 Shortest Job First")
print("2 Shortest Remaining Time First")
print("3 Round Robin")

algo, n, q = [int(x) for x in input().split(" ")]
processes = []

for i in range(n):
    id, at, bt = input().split(" ")
    processes.append(Process(int(id), int(at), int(bt)))

processes.sort(key=lambda x: x.get_id())

waiting_times = []

if algo == 0: # First Come First Serve
    waiting_times = FCFS(processes)
    outputWaitingTimes(waiting_times, n)
elif algo == 1: # Shortest Job First
    pass
elif algo == 2: # Shortest Remaining Time First
    waiting_times = SRTF(processes)
    outputWaitingTimes(waiting_times, n)
elif algo == 3: # Round Robin
    pass
else:
    print("Invalid input")
    

