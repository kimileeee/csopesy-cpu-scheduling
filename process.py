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

    def set_remaining_time(self, remaining_time):
        self.remaining_time = remaining_time

    def decrement_remaining_time(self):
        self.remaining_time -= 1