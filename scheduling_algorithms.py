import copy

# Function to implement FCFS scheduling
def FCFS(processes):
    # Sort processes by arrival time
    processes.sort(key=lambda x: x.get_arrival_time()) 

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

# Function to implement SJF scheduling
def SJF(processes):
    waiting_times = []
    current_time = 0

    while processes:
        ready_processes = [p for p in processes if p.get_arrival_time() <= current_time]
        if ready_processes:
            ready_processes.sort(key=lambda x: x.get_burst_time())
            current_process = ready_processes[0]

            if current_process.get_start_time() == 0:
                current_process.set_start_time(current_time)

            end_time = current_time + current_process.get_burst_time()
            current_process.set_end_time(end_time)
            current_process.set_waiting_time(current_process.get_start_time() - current_process.get_arrival_time())

            waiting_times.append(current_process)
            current_time = end_time
            processes.remove(current_process)

        else:
            current_time += 1

    return waiting_times


# Function to implement SRTF scheduling
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
                ongoing_process.decrement_remaining_time()

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

# Function to implement RR scheduling
def RR(processes, quantum):
    waiting_times = []
    current_time = 0
    queue = []

    while processes or queue:
        if processes:
            to_remove = []
            processes.sort(key=lambda x: x.get_arrival_time())
            for process in processes:
                if process.get_arrival_time() <= current_time:
                    idx = next((i for i, other in enumerate(queue) if process.get_arrival_time() <= other.get_previous_end_time()), len(queue))
                    queue.insert(idx, process)
                    to_remove.append(process)
        
            for x in to_remove:
                processes.remove(x)
        print("Queue: ", end="")
        print([p.get_id() for p in queue])
        if queue:
            current_process = queue.pop(0)
            current_process.set_start_time(current_time)

            if current_process.get_remaining_time() <= quantum:
                current_time += current_process.get_remaining_time()
                current_process.set_remaining_time(0)

            else:
                current_time += quantum
                current_process.set_remaining_time(current_process.get_remaining_time() - quantum)
                queue.append(current_process)

            current_process.set_end_time(current_time)
            current_process.set_waiting_time_intervals()
            
            waiting_times.append(copy.deepcopy(current_process))
            current_process.set_previous_end_time(current_time)

        else:
            current_time += 1

    return waiting_times