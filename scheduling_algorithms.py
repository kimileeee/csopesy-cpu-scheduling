import copy

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
