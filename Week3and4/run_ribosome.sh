#!/bin/bash

# Define the directory containing your genome files
genome_dir="../ncbi_dataset/data"

# Iterate over each .fna file in the directory
for fna_file in $(find "$genome_dir" -name "*.fna"); do
    echo "Processing $fna_file"

    # Extract the base name of the file (without directory and extension)
    base_name=$(basename "$fna_file" .fna)

    # Define the output file path
    output_file="${fna_file%.fna}_proteins3.txt"

    # Run the gene_finder3.py script
    python gene_finder3.py -f "$fna_file" -l 100 -r 20 > "$output_file"

    echo "Output saved to $output_file"
done

