import sys
from Bio import Entrez
from Bio import SeqIO

# set email address for Entrez
Entrez.email = "jmacrander@flsouthern.edu"

# read in list of accessions from file
acc_file = sys.argv[1]
accessions = []
with open(acc_file, "r") as f:
    for line in f:
        sample,accession,count = line.split("\t")
        #print (sample)
        #print (accession)
        #print (count.rstrip())

        # Fetch the taxonomy record from NCBI using the accession
        handle = Entrez.efetch(db="nucleotide", id=accession, retmode="xml")
        record = Entrez.read(handle)
        #print (record)

        # Print the taxonomic information
        taxid = record[0]["GBSeq_taxonomy"]
        print (sample,"\t",count.rstrip(),"\t",accession,"\t",taxid)
        #handle = Entrez.efetch(db="taxonomy", id=taxid, retmode="xml")
        #taxonomy = Entrez.read(handle)
        #lineage = taxonomy[0]["Lineage"]
        #print(accession, lineage)


# retrieve GenBank records and parse taxonomic information
#handle = Entrez.efetch(db="nucleotide", id=accessions, rettype="gb", retmode="text")
#records = SeqIO.parse(handle, "genbank")
#for record in records:
#    # extract taxonomic information
#    taxid = record.annotations['taxonomy'][-1].split()[-1]
#    handle = Entrez.efetch(db="taxonomy", id=taxid, retmode="xml")
#    records = Entrez.read(handle)
#    lineage = records[0]['Lineage']
#    name = records[0]['ScientificName']
#
#    # print taxonomic information
#    print(record.id, name, lineage, sep="\t")
