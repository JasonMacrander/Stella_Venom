import os

# Define the directory where the files are located
directory = "/jet/home/jmacrand/MiSeq_Nematostella/"

# Create empty dictionaries to store values
column2_values = {}
column3_values = {}

# Get the list of files with "_Output.txt" in their names
files = [filename for filename in os.listdir(directory) if filename.endswith("_Output.txt")]

# Loop through the files in the directory
for filename in files:
    file_path = os.path.join(directory, filename)
    # Extract the column header from the file name
    column_header = filename.replace("_Output.txt", "")

    # Open the file for reading
    with open(file_path, "r") as file:
        # Read the lines of the file
        lines = file.readlines()

        # Loop through each line
        for line in lines:
            # Split the line into columns
            columns = line.strip().split("\t")
            identifier = columns[0]
            value2 = columns[1]
            value3 = columns[2]

            # Add the identifier and corresponding values to the dictionaries
            if identifier in column2_values:
                column2_values[identifier][column_header] = value2
                column3_values[identifier][column_header] = value3
            else:
                column2_values[identifier] = {column_header: value2}
                column3_values[identifier] = {column_header: value3}

# Create the output files for values2 and values3
output_values2_file = "Unique_Seqs_output.txt"
output_values3_file = "Unique_Reads_output.txt"

# Get the unique column headers
unique_headers = list(set([header for header_dict in column2_values.values() for header in header_dict]))

# Write the combined data to the output files
with open(output_values2_file, "w") as values2_file, open(output_values3_file, "w") as values3_file:
    # Write the column headers to the files
    values2_file.write("Identifier\t" + "\t".join(unique_headers) + "\n")
    values3_file.write("Identifier\t" + "\t".join(unique_headers) + "\n")

    # Write the identifier and corresponding values to the files
    for identifier in column2_values.keys():
        values2 = [column2_values[identifier].get(header, '0') for header in unique_headers]
        values3 = [column3_values[identifier].get(header, '0') for header in unique_headers]
        values2_file.write(identifier + "\t" + "\t".join(values2) + "\n")
        values3_file.write(identifier + "\t" + "\t".join(values3) + "\n")
