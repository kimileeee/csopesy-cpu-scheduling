from queue import PriorityQueue
import copy

class Process:
    def __init__(self, process_id, arrival_time, burst_time):
        self.process_id = process_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = 0
        self.end_time = 0
        self.waiting_time = 0
        self.remaining_time = burst_time
        self.previous_end_time = 0

    def __lt__(self, other):
        if self.burst_time == other.burst_time:
            return self.arrival_time < other.arrival_time
        return self.burst_time < other.burst_time

    def __str__(self):
        return f"{self.process_id} start time: {self.start_time} end time: {self.end_time} | Waiting time: {self.waiting_time}"

    def __eq__(self, other):
        if isinstance(other, Process):
            return self.process_id == other.process_id
        return False

    def get_id(self):
        return self.process_id
    
    def get_arrival_time(self):
        return self.arrival_time
    
    def get_burst_time(self):
        return self.burst_time
    
    def get_remaining_time(self):
        return self.remaining_time
    
    def get_start_time(self):
        return self.start_time
    
    def get_end_time(self):
        return self.end_time
    
    def get_previous_end_time(self):
        return self.previous_end_time
    
    def get_waiting_time(self):
        return self.waiting_time
    
    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time
    
    def set_burst_time(self, burst_time):
        self.burst_time = burst_time

    def set_start_time(self, start_time):
        self.start_time = start_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def set_previous_end_time(self, previous_end_time):
        self.previous_end_time = previous_end_time

    def set_waiting_time(self, waiting_time):
        self.waiting_time = waiting_time

    def decrement_remaining_time(self):
        self.remaining_time -= 1


def outputWaitingTimes(waiting_times, n):
    sum = 0
    for process in waiting_times:
        print(process)
        sum += process.get_waiting_time()
    print("Average waiting time: " + str(sum/n))

# Function to implement FCFS scheduling
def FCFS(processes):
    waiting_times = []
    prev_end_time = processes[0].get_arrival_time()
    
    for process in processes:
        start_time = prev_end_time
        end_time = start_time + process.get_burst_time()

        process.set_start_time(start_time)
        process.set_end_time(end_time)
        process.set_waiting_time(start_time - process.get_arrival_time())
        
        prev_end_time = end_time

        waiting_times.append(process)

    return waiting_times

def SRTF(processes):
    waiting_times = []
    current_time = 0
    ongoing_process = None
    is_done = {p.get_id(): False for p in processes}

    while any(not done for done in is_done.values()):
        min_burst = float('inf')
        shortest_arrived = None

        # Find process with minimum remaining time
        for idx in range(len(processes)):
            if processes[idx].get_arrival_time() <= current_time and processes[idx].get_remaining_time() < min_burst and processes[idx].get_remaining_time() > 0:
                min_burst = processes[idx].get_remaining_time()
                shortest_arrived = idx

        if shortest_arrived != None:
            process_to_execute = processes[shortest_arrived]

            if ongoing_process == None:
                ongoing_process = process_to_execute
                ongoing_process.set_start_time(current_time)

            else:
                if ongoing_process != process_to_execute:
                    # context switch
                    ongoing_process.set_end_time(current_time)
                    if ongoing_process.get_previous_end_time() == 0:
                        ongoing_process.set_waiting_time(ongoing_process.get_start_time() - ongoing_process.get_arrival_time())
                    else:
                        ongoing_process.set_waiting_time(ongoing_process.get_start_time() - ongoing_process.get_previous_end_time())
                    waiting_times.append(copy.deepcopy(ongoing_process))
                    
                    ongoing_process.set_previous_end_time(current_time)
                    ongoing_process = process_to_execute
                    ongoing_process.set_start_time(current_time)

                ongoing_process.decrement_remaining_time()
                if ongoing_process.get_remaining_time() == 0:
                    is_done[ongoing_process.get_id()] = True
                
        current_time += 1

    ongoing_process.set_end_time(current_time-1)
    if ongoing_process.get_previous_end_time() == 0:
        ongoing_process.set_waiting_time(ongoing_process.get_start_time() - ongoing_process.get_arrival_time())
    else:
        ongoing_process.set_waiting_time(ongoing_process.get_start_time() - ongoing_process.get_previous_end_time())
    waiting_times.append(copy.deepcopy(ongoing_process))
    return waiting_times

## INPUT
# The first line contains three integers separated by space, 𝑋 𝑌 𝑍.
# 𝑋 denotes the CPU scheduling algorithm.
# 𝑌 denotes the number of processes where 3 ≤𝑌 ≤100
# 𝑍 denotes a time quantum value (applicable for Round-Robin algorithm only), where 1 ≤ 𝑍 ≤ 100. 
    # If the CPU scheduling algorithm indicated by the value of 𝑋 is not the Round-Robin algorithm, 
    # this value must be set to 1 but ignored.
# There will be 𝑌 lines of space-separated integers 𝐴 𝐵 𝐶 where 𝐴 is the process ID, 𝐵 is the arrival time, and 𝐶 is the burst time.

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
    

