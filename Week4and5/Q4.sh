#!/bin/bash

# Create a temporary directory for output
mkdir tmp

# Load the Prokka module
module load prokka

# Find all FNA files and process them
find ../ncbi_dataset/data/ -name "*.fna" -type f | while read -r fna_file; do
    # Generate output GFF file path
    gff_file="tmp/$(basename "${fna_file%.fna}.gff")"

    # Run the Prokka command to generate a GFF file
    prokka --outdir tmp/ --force --prefix "$(basename "${fna_file%.fna}")" "$fna_file" > /dev/null 2>&1

    # Count the number of CDS entries in the GFF file
    cds_count=$(grep -c "CDS" "$gff_file")

    # Print the GFF file path and the CDS count
    echo "File: $gff_file, CDS Count: $cds_count"
<<<<<<< HEAD
done | sort -k3 -n
=======
done | sort -k3 -n 
>>>>>>> 4ba59630aaaeb3825c1854d0e155414519d7c9e6
