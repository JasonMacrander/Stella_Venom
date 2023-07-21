import sys
from Bio import SeqIO

# dictionary to store the unique sequences for each individual
sequences = {}

# iterate over each fasta file provided
for file_name in sys.argv[1:]:
    for record in SeqIO.parse(file_name, "fasta"):
        # extract location and individual from sequence name
        locn = record.name[0:2]
        indv = record.name[2:4]
        
        # extract sequence and remove whitespace
        seq = str(record.seq).replace(" ", "")
        
        # combine location and individual to form dictionary key
        key = f"{locn}_{indv}"
        
        # check if key already exists in dictionary
        if key in sequences:
            # check if sequence is already in dictionary
            if seq in sequences[key]["sequences"]:
                # increment count for this sequence
                sequences[key]["sequences"][seq] += 1
            else:
                # add new sequence to dictionary
                sequences[key]["sequences"][seq] = 1
        else:
            # add new individual to dictionary
            sequences[key] = {"count": 1, "filename": file_name, "sequences": {seq: 1}}

# iterate over unique sequences and write to output file

name_add = sys.argv[1:]
precursor = name_add[0].split(".")

out_file = open("unique_sequences.fasta", "w")
for i, (key, info) in enumerate(sequences.items()):
    # extract location and individual from key
    locn, indv = key.split("_")
    
    # count the number of unique sequences for this individual
    unique_count = len(info["sequences"])
    
    # iterate over sequences for this individual and write to output file
    for j, (seq, count) in enumerate(info["sequences"].items()):
        # rename sequence with location, individual, and count information
        record_id = f"{locn}_{indv}_seq{j+1}_count{count}"
        
        # write sequence to output file
        out_file.write(f">{record_id}\n{seq}\n")
out_file.close()
