#!/bin/bash
#SBATCH -J "BLAST-Cox1"
#SBATCH -N 1
#SBATCH -p RM-shared
#SBATCH -t 24:00:00
#SBATCH --ntasks-per-node=24

#esearch -db nucleotide -query "cox1" | efetch -db nucleotide -format fasta >coi_sequences.fasta

#/ocean/projects/bio210089p/shared/PROGRAMS/ncbi-blast-2.12.0+/bin/blastn -query unique_sequences_MA-JF.fasta -db coi_db -outfmt 6 -max_target_seqs 1 -out MA-JF_BLAST_OUT.txt
/ocean/projects/bio210089p/shared/PROGRAMS/ncbi-blast-2.12.0+/bin/blastn -query unique_sequences_ME-JF.fasta -db coi_db -outfmt 6 -max_target_seqs 1 -out ME-JF_BLAST_OUT.txt
#/ocean/projects/bio210089p/shared/PROGRAMS/ncbi-blast-2.12.0+/bin/blastn -query unique_sequences_NH-JF.fasta -db coi_db -outfmt 6 -max_target_seqs 1 -out NH-JF_BLAST_OUT.txt
#/ocean/projects/bio210089p/shared/PROGRAMS/ncbi-blast-2.12.0+/bin/blastn -query unique_sequences_MA-MF.fasta -db coi_db -outfmt 6 -max_target_seqs 1 -out MA-MF_BLAST_OUT.txt
/ocean/projects/bio210089p/shared/PROGRAMS/ncbi-blast-2.12.0+/bin/blastn -query unique_sequences_ME-MF.fasta -db coi_db -outfmt 6 -max_target_seqs 1 -out ME-MF_BLAST_OUT.txt
#/ocean/projects/bio210089p/shared/PROGRAMS/ncbi-blast-2.12.0+/bin/blastn -query unique_sequences_NH-MF.fasta -db coi_db -outfmt 6 -max_target_seqs 1 -out NH-MF_BLAST_OUT.txt
/ocean/projects/bio210089p/shared/PROGRAMS/ncbi-blast-2.12.0+/bin/blastn -query unique_sequences_ME-SF.fasta -db coi_db -outfmt 6 -max_target_seqs 1 -out ME-SF_BLAST_OUT.txt
#/ocean/projects/bio210089p/shared/PROGRAMS/ncbi-blast-2.12.0+/bin/blastn -query unique_sequences_NH-SF.fasta -db coi_db -outfmt 6 -max_target_seqs 1 -out NH-SF_BLAST_OUT.txt