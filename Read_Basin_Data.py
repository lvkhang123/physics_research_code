# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 15:20:55 2024

@author: TaiKhangHao
"""

# Define the filename

filename = 'basin_attraction_data.txt'

# Initialize a list to store the parsed data

parsed_data = []

# Open the file and read the lines

with open(filename, 'r') as file:
    lines = file.readlines()

    # Process each line
    
    for line in lines:
        
        # Strip whitespace and split the line by commas and spaces
        
        parts = line.strip().split(', ')

        # Extract and convert the relevant parts to floats
        
        try:
            part_1 = int(parts[0].strip('()'))  # Convert first value to integer
            part_2 = int(parts[1])  # Convert second value to integer
            part_3 = float(parts[2])  # Convert third value to float
            part_4 = float(parts[3].strip('()'))  # Convert fourth value to float
            
            # Append the tuple to the parsed_data list
            
            parsed_data.append((part_1, part_2, part_3, part_4))
        except ValueError as e:
            print(f"Error processing line: {line} - {e}")

# Print the parsed data to verify

for data in parsed_data:
    print(data)
