def remove_duplicate_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Create a new list to store non-duplicate lines
    new_lines = []

    # Initialize a variable to skip lines when needed
    skip_next = False

    for i in range(len(lines) - 1):  # -1 to avoid index out of range in the next step
        if skip_next:
            skip_next = False
            continue

        # Compare the current line with the next line
        if lines[i] == lines[i + 1]:
            skip_next = True

        new_lines.append(lines[i])

    # If the last line wasn't a duplicate, add it to the new_lines list
    if not skip_next:
        new_lines.append(lines[-1])

    # Write the new_lines to the file
    with open(filename, 'w') as file:
        file.writelines(new_lines)

# Example usage:
filename = f"D:/EMbedded System/degree project/thesis writing/fig/3. results and analysis/2023011_micro_evo_random/micro evolutionary/Architecture_info.txt"

remove_duplicate_lines(filename)
