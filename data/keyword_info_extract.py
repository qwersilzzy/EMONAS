

import re
import os


def extract_info(filename, keyword):
    extracted_values = []

    # Compile two regex patterns:
    # 1) Matches the format "keyword = value"
    # 2) Matches the format "keyword value"
    pattern1 = re.compile(rf"{keyword}\s*=\s*([\S]+)")
    pattern2 = re.compile(rf"{keyword}\s+([\S]+)")

    with open(filename, 'r') as file:
        for line in file:
            # First, check the "keyword = value" format
            match = pattern1.search(line)
            if not match:
                # If not found, check the "keyword value" format
                match = pattern2.search(line)

            if match:
                extracted_values.append(match.group(1))

    return extracted_values

def extract_info_architecture(filename, keyword):
    extracted_data = []
    with open(filename, 'r') as file:
        for line in file:
            if keyword in line:
                # Extract the information after the keyword
                start_index = line.find(keyword) + len(keyword)
                info = line[start_index:].strip()
                extracted_data.append(info)
    return extracted_data




def save_to_file(data, directory, keyword):
    # Define the output filename
    output_filename = os.path.join(directory, f"{keyword.replace(' ', '_')}_info.txt")

    # Write the extracted data to the output file
    with open(output_filename, 'w') as output_file:
        for item in data:
            output_file.write(item + '\n')

# Example usage:
filename = f"D:/EMbedded System/degree project/thesis writing/fig/3. results and analysis/2023011_micro_evo_random/micro evolutionary/archi100_epoch20_micro_evolutionary.txt"
keyword = 'Genome'
# extracted_data = extract_info(filename, keyword)
extracted_data = extract_info_architecture(filename, keyword)
print(extracted_data)
#
# 
# # Save the extracted data to a new file
# save_to_file(extracted_data, os.path.dirname(filename), keyword)

