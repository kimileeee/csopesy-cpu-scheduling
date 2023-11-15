import os
import subprocess
import docx2txt

def process_input(input_path, output_path):
    input_data = ""
    if(input_path.endswith('.txt')):
        input_data = open(input_path).read()
    else:
        input_data = docx2txt.process(input_path)
    subprocess.run(['python', 'main.py'], input=input_data, text=True, stdout=open(output_path, 'w'))


def process_folder(input_folder, output_folder):
    # Iterate through each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt') or filename.endswith('.docx'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename.replace('input', 'output'))
            print(input_path, output_path)

            # Process the input and write the output
            process_input(input_path, output_path)

def main():
    # Define the input and output folders
    input_folder = "INPUT"
    output_folder = "OUTPUT"

    # Iterate through each subfolder in the input folder
    for subfolder in os.listdir(input_folder):
        subfolder_path = os.path.join(input_folder, subfolder, 'input')

        # Skip if it's not a directory
        if not os.path.isdir(subfolder_path):
            continue

        # Create corresponding output subfolder if not exists
        output_subfolder = os.path.join(output_folder, subfolder)
        os.makedirs(output_subfolder, exist_ok=True)

        # Process files in the subfolder
        process_folder(subfolder_path, output_subfolder)

if __name__ == "__main__":
    main()
