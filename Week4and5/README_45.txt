## Question 1: ##
[almualzm@login509-02-r Week4and5]$ python genome_annotation1.py
>> The number of amino acids is: 30
>> The total number of bases in the ORF (including stop codon) is: 93

# Code for genome_annotation1.py
# Given amino acid sequence
amino_seq = "KVRMFTSELDIMLSVNGPADQIKYFCRHWT"

# Calculate the number of amino acids and total bases in the ORF
num_amino_acids = len(amino_seq)
total_bases = (num_amino_acids * 3) + 3

# Display the results with descriptive strings
print(f"The number of amino acids is: {num_amino_acids}")
print(f"The total number of bases in the ORF (including stop codon) is: {total_bases}")

## Question 2: ##
[almualzm@login509-02-r Week4and5]$ emacs Q2.sh
[almualzm@login509-02-r Week4and5]$ bash Q2.sh
>> Loading module for PRODIGAL v2.6.3
>> PRODIGAL v2.6.3 is now loaded
>> File: ../ncbi_dataset/data/GCA_000006745.1/GCA_000006745.1_ASM674v1_genomic.gff, CDS Count: 3594

# Code for the sh file:

#!/bin/bash

# Load the Prodigal module
module load prodigal

# Specify the input genome file
input_file="../ncbi_dataset/data/GCA_000006745.1/GCA_000006745.1_ASM674v1_genomic.fna"

# Define th gff file
gff_file="${input_file%.fna}.gff"

# Run Prodigal to annotate the genes, with quiet mode enabled
prodigal -i "$input_file" -o "$gff_file" -q

# Count the number of Coding Sequences annotated in the GFF file
cds_count=$(grep -c "CDS" "$gff_file")

# Output the file name and the CDS count
echo "File: $gff_file, CDS Count: $cds_count"

## Question 3: ##
