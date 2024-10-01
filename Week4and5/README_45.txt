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
[almualzm@login509-02-r Week4and5]$ emacs Q3.sh
[almualzm@login509-02-r Week4and5]$ bash Q3.sh
Loading module for PRODIGAL v2.6.3
PRODIGAL v2.6.3 is now loaded
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...3294955 bp seq created, 57.22 pct GC
Locating all potential starts and stops...213618 nodes
Looking for GC bias in different frames...frame bias scores: 0.83 0.28 1.89
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2117144 bp)...done!
Finding genes in sequence #2 (1177787 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1860725 bp seq created, 46.25 pct GC
Locating all potential starts and stops...92480 nodes
Looking for GC bias in different frames...frame bias scores: 1.27 0.19 1.54
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1860725 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...3284204 bp seq created, 66.61 pct GC
Locating all potential starts and stops...191980 nodes
Looking for GC bias in different frames...frame bias scores: 0.73 0.11 2.16
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2648638 bp)...done!
Finding genes in sequence #2 (412348 bp)...done!
Finding genes in sequence #3 (45704 bp)...done!
Finding genes in sequence #4 (177466 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1590815 bp seq created, 43.30 pct GC
Locating all potential starts and stops...51125 nodes
Looking for GC bias in different frames...frame bias scores: 1.67 0.24 1.09
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1551335 bp)...done!
Finding genes in sequence #2 (39456 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1042519 bp seq created, 41.31 pct GC
Locating all potential starts and stops...37422 nodes
Looking for GC bias in different frames...frame bias scores: 2.60 0.20 0.20
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1042519 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...3294955 bp seq created, 57.22 pct GC
Locating all potential starts and stops...213618 nodes
Looking for GC bias in different frames...frame bias scores: 0.83 0.28 1.89
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2117144 bp)...done!
Finding genes in sequence #2 (1177787 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1860725 bp seq created, 46.25 pct GC
Locating all potential starts and stops...92480 nodes
Looking for GC bias in different frames...frame bias scores: 1.27 0.19 1.54
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1860725 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...3284204 bp seq created, 66.61 pct GC
Locating all potential starts and stops...191980 nodes
Looking for GC bias in different frames...frame bias scores: 0.73 0.11 2.16
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2648638 bp)...done!
Finding genes in sequence #2 (412348 bp)...done!
Finding genes in sequence #3 (45704 bp)...done!
Finding genes in sequence #4 (177466 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1590815 bp seq created, 43.30 pct GC
Locating all potential starts and stops...51125 nodes
Looking for GC bias in different frames...frame bias scores: 1.67 0.24 1.09
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1551335 bp)...done!
Finding genes in sequence #2 (39456 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1042519 bp seq created, 41.31 pct GC
Locating all potential starts and stops...37422 nodes
Looking for GC bias in different frames...frame bias scores: 2.60 0.20 0.20
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1042519 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...4033488 bp seq created, 47.49 pct GC
Locating all potential starts and stops...219838 nodes
Looking for GC bias in different frames...frame bias scores: 2.21 0.16 0.62
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2961149 bp)...done!
Finding genes in sequence #2 (1072315 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...2257487 bp seq created, 40.40 pct GC
Locating all potential starts and stops...96476 nodes
Looking for GC bias in different frames...frame bias scores: 2.65 0.14 0.21
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2257487 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...2365589 bp seq created, 35.33 pct GC
Locating all potential starts and stops...86378 nodes
Looking for GC bias in different frames...frame bias scores: 2.54 0.16 0.29
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2365589 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1138011 bp seq created, 52.77 pct GC
Locating all potential starts and stops...73375 nodes
Looking for GC bias in different frames...frame bias scores: 2.03 0.23 0.74
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1138011 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1643831 bp seq created, 39.19 pct GC
Locating all potential starts and stops...71171 nodes
Looking for GC bias in different frames...frame bias scores: 1.58 0.14 1.28
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1643831 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...4033488 bp seq created, 47.49 pct GC
Locating all potential starts and stops...219838 nodes
Looking for GC bias in different frames...frame bias scores: 2.21 0.16 0.62
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2961149 bp)...done!
Finding genes in sequence #2 (1072315 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...2257487 bp seq created, 40.40 pct GC
Locating all potential starts and stops...96476 nodes
Looking for GC bias in different frames...frame bias scores: 2.65 0.14 0.21
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2257487 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...2365589 bp seq created, 35.33 pct GC
Locating all potential starts and stops...86378 nodes
Looking for GC bias in different frames...frame bias scores: 2.54 0.16 0.29
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2365589 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1138011 bp seq created, 52.77 pct GC
Locating all potential starts and stops...73375 nodes
Looking for GC bias in different frames...frame bias scores: 2.03 0.23 0.74
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1138011 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1643831 bp seq created, 39.19 pct GC
Locating all potential starts and stops...71171 nodes
Looking for GC bias in different frames...frame bias scores: 1.58 0.14 1.28
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1643831 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1667867 bp seq created, 38.87 pct GC
Locating all potential starts and stops...71998 nodes
Looking for GC bias in different frames...frame bias scores: 1.71 0.15 1.14
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1667867 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1230230 bp seq created, 40.58 pct GC
Locating all potential starts and stops...40543 nodes
Looking for GC bias in different frames...frame bias scores: 2.57 0.21 0.22
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1230230 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1830138 bp seq created, 38.15 pct GC
Locating all potential starts and stops...72389 nodes
Looking for GC bias in different frames...frame bias scores: 2.68 0.13 0.19
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1830138 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1234409 bp seq created, 40.57 pct GC
Locating all potential starts and stops...40703 nodes
Looking for GC bias in different frames...frame bias scores: 2.57 0.21 0.22
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1229853 bp)...done!
Finding genes in sequence #2 (4532 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1667867 bp seq created, 38.87 pct GC
Locating all potential starts and stops...71998 nodes
Looking for GC bias in different frames...frame bias scores: 1.71 0.15 1.14
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1667867 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1230230 bp seq created, 40.58 pct GC
Locating all potential starts and stops...40543 nodes
Looking for GC bias in different frames...frame bias scores: 2.57 0.21 0.22
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1230230 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1830138 bp seq created, 38.15 pct GC
Locating all potential starts and stops...72389 nodes
Looking for GC bias in different frames...frame bias scores: 2.68 0.13 0.19
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1830138 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1229853 bp seq created, 40.57 pct GC
Locating all potential starts and stops...40520 nodes
Looking for GC bias in different frames...frame bias scores: 2.57 0.21 0.22
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1229853 bp)...done!
>> ../ncbi_dataset/data/GCF_000006745.1/GCF_000006745.1_ASM674v1_genomic.gff 3594

# bash file code:
File Edit Options Buffers Tools Sh-Script Help
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

## Question 4: ##
<<<<<<< HEAD
=======
Prokka is very slow. Also, the output is smaller than we Prodgal was used
# Prokka
[almualzm@login509-02-r Week4and5]$ emacs Q4.sh
>>>>>>> 28a8b147cdd93517c097b7136eb51161c7ae6e0c
[almualzm@login509-02-r Week4and5]$ bash Q4.sh
Loading module for Prokka
Prokka 1.14.6 modules now loaded
File: tmp/GCF_000091085.2_ASM9108v2_genomic.gff, CDS Count: 1052
<<<<<<< HEAD
=======
# Prodigal
>>>>>>> 28a8b147cdd93517c097b7136eb51161c7ae6e0c
[almualzm@login509-02-r Week4and5]$ emacs Q4_prodigal.sh
[almualzm@login509-02-r Week4and5]$ bash Q4_prodigal.sh
Loading module for PRODIGAL v2.6.3
PRODIGAL v2.6.3 is now loaded
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...3294955 bp seq created, 57.22 pct GC
Locating all potential starts and stops...213618 nodes
Looking for GC bias in different frames...frame bias scores: 0.83 0.28 1.89
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2117144 bp)...done!
Finding genes in sequence #2 (1177787 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1860725 bp seq created, 46.25 pct GC
Locating all potential starts and stops...92480 nodes
Looking for GC bias in different frames...frame bias scores: 1.27 0.19 1.54
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1860725 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...3284204 bp seq created, 66.61 pct GC
Locating all potential starts and stops...191980 nodes
Looking for GC bias in different frames...frame bias scores: 0.73 0.11 2.16
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2648638 bp)...done!
Finding genes in sequence #2 (412348 bp)...done!
Finding genes in sequence #3 (45704 bp)...done!
Finding genes in sequence #4 (177466 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1590815 bp seq created, 43.30 pct GC
Locating all potential starts and stops...51125 nodes
Looking for GC bias in different frames...frame bias scores: 1.67 0.24 1.09
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1551335 bp)...done!
Finding genes in sequence #2 (39456 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1042519 bp seq created, 41.31 pct GC
Locating all potential starts and stops...37422 nodes
Looking for GC bias in different frames...frame bias scores: 2.60 0.20 0.20
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1042519 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...3294955 bp seq created, 57.22 pct GC
Locating all potential starts and stops...213618 nodes
Looking for GC bias in different frames...frame bias scores: 0.83 0.28 1.89
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2117144 bp)...done!
Finding genes in sequence #2 (1177787 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1860725 bp seq created, 46.25 pct GC
Locating all potential starts and stops...92480 nodes
Looking for GC bias in different frames...frame bias scores: 1.27 0.19 1.54
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1860725 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...3284204 bp seq created, 66.61 pct GC
Locating all potential starts and stops...191980 nodes
Looking for GC bias in different frames...frame bias scores: 0.73 0.11 2.16
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2648638 bp)...done!
Finding genes in sequence #2 (412348 bp)...done!
Finding genes in sequence #3 (45704 bp)...done!
Finding genes in sequence #4 (177466 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1590815 bp seq created, 43.30 pct GC
Locating all potential starts and stops...51125 nodes
Looking for GC bias in different frames...frame bias scores: 1.67 0.24 1.09
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1551335 bp)...done!
Finding genes in sequence #2 (39456 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1042519 bp seq created, 41.31 pct GC
Locating all potential starts and stops...37422 nodes
Looking for GC bias in different frames...frame bias scores: 2.60 0.20 0.20
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1042519 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...4033488 bp seq created, 47.49 pct GC
Locating all potential starts and stops...219838 nodes
Looking for GC bias in different frames...frame bias scores: 2.21 0.16 0.62
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2961149 bp)...done!
Finding genes in sequence #2 (1072315 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...2257487 bp seq created, 40.40 pct GC
Locating all potential starts and stops...96476 nodes
Looking for GC bias in different frames...frame bias scores: 2.65 0.14 0.21
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2257487 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...2365589 bp seq created, 35.33 pct GC
Locating all potential starts and stops...86378 nodes
Looking for GC bias in different frames...frame bias scores: 2.54 0.16 0.29
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2365589 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1138011 bp seq created, 52.77 pct GC
Locating all potential starts and stops...73375 nodes
Looking for GC bias in different frames...frame bias scores: 2.03 0.23 0.74
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1138011 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1643831 bp seq created, 39.19 pct GC
Locating all potential starts and stops...71171 nodes
Looking for GC bias in different frames...frame bias scores: 1.58 0.14 1.28
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1643831 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...4033488 bp seq created, 47.49 pct GC
Locating all potential starts and stops...219838 nodes
Looking for GC bias in different frames...frame bias scores: 2.21 0.16 0.62
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2961149 bp)...done!
Finding genes in sequence #2 (1072315 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...2257487 bp seq created, 40.40 pct GC
Locating all potential starts and stops...96476 nodes
Looking for GC bias in different frames...frame bias scores: 2.65 0.14 0.21
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2257487 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...2365589 bp seq created, 35.33 pct GC
Locating all potential starts and stops...86378 nodes
Looking for GC bias in different frames...frame bias scores: 2.54 0.16 0.29
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (2365589 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1138011 bp seq created, 52.77 pct GC
Locating all potential starts and stops...73375 nodes
Looking for GC bias in different frames...frame bias scores: 2.03 0.23 0.74
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1138011 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1643831 bp seq created, 39.19 pct GC
Locating all potential starts and stops...71171 nodes
Looking for GC bias in different frames...frame bias scores: 1.58 0.14 1.28
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1643831 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1667867 bp seq created, 38.87 pct GC
Locating all potential starts and stops...71998 nodes
Looking for GC bias in different frames...frame bias scores: 1.71 0.15 1.14
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1667867 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1230230 bp seq created, 40.58 pct GC
Locating all potential starts and stops...40543 nodes
Looking for GC bias in different frames...frame bias scores: 2.57 0.21 0.22
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1230230 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1830138 bp seq created, 38.15 pct GC
Locating all potential starts and stops...72389 nodes
Looking for GC bias in different frames...frame bias scores: 2.68 0.13 0.19
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1830138 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1234409 bp seq created, 40.57 pct GC
Locating all potential starts and stops...40703 nodes
Looking for GC bias in different frames...frame bias scores: 2.57 0.21 0.22
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1229853 bp)...done!
Finding genes in sequence #2 (4532 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1667867 bp seq created, 38.87 pct GC
Locating all potential starts and stops...71998 nodes
Looking for GC bias in different frames...frame bias scores: 1.71 0.15 1.14
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1667867 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1230230 bp seq created, 40.58 pct GC
Locating all potential starts and stops...40543 nodes
Looking for GC bias in different frames...frame bias scores: 2.57 0.21 0.22
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1230230 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1830138 bp seq created, 38.15 pct GC
Locating all potential starts and stops...72389 nodes
Looking for GC bias in different frames...frame bias scores: 2.68 0.13 0.19
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1830138 bp)...done!
-------------------------------------
PRODIGAL v2.6.3 [February, 2016]
Univ of Tenn / Oak Ridge National Lab
Doug Hyatt, Loren Hauser, et al.
-------------------------------------
Request:  Single Genome, Phase:  Training
Reading in the sequence(s) to train...1229853 bp seq created, 40.57 pct GC
Locating all potential starts and stops...40520 nodes
Looking for GC bias in different frames...frame bias scores: 2.57 0.21 0.22
Building initial set of genes to train from...done!
Creating coding model and scoring nodes...done!
Examining upstream regions and training starts...done!
-------------------------------------
Request:  Single Genome, Phase:  Gene Finding
Finding genes in sequence #1 (1229853 bp)...done!
../ncbi_dataset/data/GCA_000008725.1/GCA_000008725.1_ASM872v1_genomic.gff 897
../ncbi_dataset/data/GCF_000008725.1/GCF_000008725.1_ASM872v1_genomic.gff 897
../ncbi_dataset/data/GCA_000008605.1/GCA_000008605.1_ASM860v1_genomic.gff 1009
../ncbi_dataset/data/GCF_000008605.1/GCF_000008605.1_ASM860v1_genomic.gff 1009
../ncbi_dataset/data/GCF_000091085.2/GCF_000091085.2_ASM9108v2_genomic.gff 1057
../ncbi_dataset/data/GCA_000008745.1/GCA_000008745.1_ASM874v1_genomic.gff 1063
../ncbi_dataset/data/GCA_000091085.2/GCA_000091085.2_ASM9108v2_genomic.gff 1063
../ncbi_dataset/data/GCF_000008745.1/GCF_000008745.1_ASM874v1_genomic.gff 1063
../ncbi_dataset/data/GCA_000008785.1/GCA_000008785.1_ASM878v1_genomic.gff 1505
../ncbi_dataset/data/GCF_000008785.1/GCF_000008785.1_ASM878v1_genomic.gff 1505
../ncbi_dataset/data/GCA_000008525.1/GCA_000008525.1_ASM852v1_genomic.gff 1579
../ncbi_dataset/data/GCF_000008525.1/GCF_000008525.1_ASM852v1_genomic.gff 1579
../ncbi_dataset/data/GCA_000027305.1/GCA_000027305.1_ASM2730v1_genomic.gff 1748
../ncbi_dataset/data/GCF_000027305.1/GCF_000027305.1_ASM2730v1_genomic.gff 1748
../ncbi_dataset/data/GCA_000008625.1/GCA_000008625.1_ASM862v1_genomic.gff 1776
../ncbi_dataset/data/GCF_000008625.1/GCF_000008625.1_ASM862v1_genomic.gff 1776
../ncbi_dataset/data/GCA_000008545.1/GCA_000008545.1_ASM854v1_genomic.gff 1866
../ncbi_dataset/data/GCF_000008545.1/GCF_000008545.1_ASM854v1_genomic.gff 1866
../ncbi_dataset/data/GCA_000006825.1/GCA_000006825.1_ASM682v1_genomic.gff 2032
../ncbi_dataset/data/GCF_000006825.1/GCF_000006825.1_ASM682v1_genomic.gff 2032
../ncbi_dataset/data/GCA_000006865.1/GCA_000006865.1_ASM686v1_genomic.gff 2383
../ncbi_dataset/data/GCF_000006865.1/GCF_000006865.1_ASM686v1_genomic.gff 2383
../ncbi_dataset/data/GCA_000007125.1/GCA_000007125.1_ASM712v1_genomic.gff 3152
../ncbi_dataset/data/GCF_000007125.1/GCF_000007125.1_ASM712v1_genomic.gff 3152
../ncbi_dataset/data/GCA_000008565.1/GCA_000008565.1_ASM856v1_genomic.gff 3248
../ncbi_dataset/data/GCF_000008565.1/GCF_000008565.1_ASM856v1_genomic.gff 3248
../ncbi_dataset/data/GCA_000006745.1/GCA_000006745.1_ASM674v1_genomic.gff 3594
../ncbi_dataset/data/GCF_000006745.1/GCF_000006745.1_ASM674v1_genomic.gff 3594
