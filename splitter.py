import os

def split_fasta(input_file):
    with open(input_file, 'r') as file:
        sequences = {}
        current_header = ''
        current_sequence = ''
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if current_sequence:
                    sequences[current_header] = current_sequence
                    current_sequence = ''
                current_header = line[1:]
            else:
                current_sequence += line
        sequences[current_header] = current_sequence

    input_filename = os.path.splitext(input_file)[0]

    for header, sequence in sequences.items():
        if 'JF' in header:
            output_file = f"{input_filename}_JF.fasta"
        elif 'MF' in header:
            output_file = f"{input_filename}_MF.fasta"
        elif 'SF' in header:
            output_file = f"{input_filename}_SF.fasta"
        else:
            continue

        with open(output_file, 'a') as outfile:
            outfile.write('>' + header + '\n' + sequence + '\n')

    print("Splitting complete!")

# Provide the path to your input FASTA file
fasta_file = 'ME.fasta'

split_fasta(fasta_file)
