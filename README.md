# CSOPESY Machine Project 1: CPU Scheduling
Lee, Kim Williame and Racelis, Criscela Ysabelle  
CSOPESY S12, T1, A.Y. 2023-24

## Running the application
In order to run the application, simply open a terminal window in the directory of the project, and simply run the ff. command:
```
python main.py
```

After running this, the application should function and display the ff.:
```
CPU Scheduling Algorithm
0 First Come First Serve
1 Shortest Job First
2 Shortest Remaining Time First
3 Round Robin
```

Then, the inputs can be entered in the ff. format:
- First line: space-separated integers X Y Z, where
    - X denotes the numerical ID of the algorithm to be simulated,
    - Y denotes the number of processes, and
    - Z denotes the length of each quantum. For non-Round Robin algorithms, this value is ignored, but should still be inputted.
- Second line until (Y+1)th line: space separated integers A B C, where
    - A denotes the process ID,
    - B denotes the arrival time, and
    - C denotes the burst time.

Upon entering all valid inputs, the output should appear in a format similar to the one below.
```
1 start time: 5 end time: 10 | Waiting time: 0
2 start time: 10 end time: 15 | Waiting time: 4
3 start time: 15 end time: 20 | Waiting time: 8
4 start time: 20 end time: 25 | Waiting time: 12
5 start time: 25 end time: 30 | Waiting time: 16
6 start time: 30 end time: 35 | Waiting time: 20
7 start time: 35 end time: 40 | Waiting time: 24
8 start time: 40 end time: 45 | Waiting time: 28
9 start time: 45 end time: 50 | Waiting time: 33
10 start time: 50 end time: 55 | Waiting time: 37
Average waiting time: 18.2
```



 
