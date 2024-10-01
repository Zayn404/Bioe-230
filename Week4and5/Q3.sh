#!/bin/bash

# Load the Prodigal module
module load prodigal

find ../ncbi_dataset/data/ -name "*.fna" -type f | while read -r fna_file; do
    # Generate output GFF file path
    gff_file="${fna_file%.fna}.gff"

    # Run Prodigal to generate the GFF file
    prodigal -i "$fna_file" -o "$gff_file"

    # Count the number of CDS entries in the GFF file
    cds_count=$(grep -c "CDS" "$gff_file")

    # Print the GFF file path and the CDS count
    echo "$gff_file $cds_count"
done | sort -k2 -n | tail -n 1
