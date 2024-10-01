
#!/bin/bash

# Extract unique gene names from all GFF files in the "tmp" directory
grep -h "gene=" tmp/*.gff | sed -n 's/.*gene=\([^;]*\).*/\1/p' | sort | uniq > unique_genes.txt

# Display the first five gene names
head -n 5 unique_genes.txt
