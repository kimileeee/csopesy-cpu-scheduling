import os

# Get the absolute path of the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Set the input and output folders relative to the script's directory
input_folder = os.path.join(script_dir, "INPUT")
output_folder = os.path.join(script_dir, "CONVERTED_INPUT")

# Assuming files are named input00.txt, input01.txt, ..., input29.txt
num_files = 30

def process_file(input_file_path, output_file_path):
    with open(input_file_path, 'r') as input_file:
        # Extract X, Y, Z values
        x, y, z = map(int, input_file.readline().split())

        # Seek back to the beginning of the file
        input_file.seek(0)

        # Skip the first line
        input_file.readline()

        # Extract arrival times and burst times
        lines = input_file.readlines()
        data = [line.split()[1:] for line in lines]
        arrival_times = [int(item[0]) for item in data]
        burst_times = [int(item[1]) for item in data]

    # Write converted data to the output file
    with open(output_file_path, 'w') as output_file:
        # Write Y value (number of processes)
        output_file.write(f"{x} {y} {z}\n\n")

        # Write arrival times
        output_file.write(" ".join(map(str, arrival_times)) + "\n\n")

        # Write burst times
        output_file.write(" ".join(map(str, burst_times)) + "\n")

def main():
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for subfolder in ['A', 'B', 'C', 'D']:
        input_folder_path = os.path.join(input_folder, subfolder, 'input')
        print(f"Looking for files in: {input_folder_path}")
        for i in range(num_files):
            input_file_path = os.path.join(input_folder_path, f'input{i:02d}.txt')
            output_file_path = os.path.join(output_folder, f'{subfolder}input{i:02d}.txt')

            if os.path.exists(input_file_path):
                process_file(input_file_path, output_file_path)
                print(f"Converted and saved: {output_file_path}")
            else:
                print(f"Input file not found: {input_file_path}")

if __name__ == "__main__":
    main()
