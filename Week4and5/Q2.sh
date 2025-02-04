
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
