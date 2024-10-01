#!/bin/bash

# Directory containing the 14 genome files
genome_dir="../ncbi_dataset/data/"

# Loop over each genome file with .fna extension
find "$genome_dir" -name "*.fna" | while read -r genome_file; do
    echo "Processing $genome_file"
    
    # Run gene_finder2.py on the current genome file
    python gene_finder2.py -f "$genome_file" -l 100 > "${genome_file%.fna}_proteins.txt"
    
    echo "Output saved to ${genome_file%.fna}_proteins.txt"
done
