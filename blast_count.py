import csv

# dictionary to store the count for each subject within each individual
counts = {}

# open the BLAST output file
with open('ME-SF_BLAST_OUT.txt', 'r') as blast_file:
    blast_reader = csv.reader(blast_file, delimiter='\t')
    for row in blast_reader:
        # extract the individual and subject from the query ID
        query_id = row[0]
        individual = query_id[0:5]
        subject = row[1]
        #print(row)

        # extract the count from the query ID
        count = int(query_id.split('_')[-1].replace('count', ''))
        #print (individual, count)
        # check if this individual is already in the dictionary
        if individual in counts:
            # check if this subject is already in the dictionary for this individual
            if subject in counts[individual]:
                # add the count to the existing value for this subject
                #print(subject)
                counts[individual][subject] += count
            else:
                # add a new key for this subject with the count as the value
                counts[individual][subject] = count
        else:
            # add a new key for this individual with a new dictionary for the subjects
            counts[individual] = {subject: count}
#print (counts)
# print out the results
for individual in counts:
    for subject in counts[individual]:
        count = counts[individual][subject]
        print(f'{individual}\t{subject}\t{count}')
