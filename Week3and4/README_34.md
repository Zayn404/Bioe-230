
## Q1 and Q2
 #This code was generated with the assistance of ChatGPT (version 3.5) and Yazeed Alroogi

from argparse import ArgumentParser #Used to parse command-line arguments.
from Bio import SeqIO #Used to read and write sequence data in various formats, including FASTA.
from Bio.Seq import Seq #Sequence manipulation, including getting the reverse complement

def get_sequences(file_path): #Take the path to the FASFA file as input
    "Read the FASTA file and return a dictionary of sequences."
    sequences = {} #Store Seq data
    for record in SeqIO.parse(file_path, "fasta"): #Read the FASFA file
        sequences[record.id] = str(record.seq) #Retrieves the sequence ID and the sequence itself, converting the sequence to a string
    return sequences

def find_orfs(sequence):
    "Find all ORFs in a given DNA sequence."
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]
    proteins = set()
    for frame in range(3):
        start_positions = []
        for location in range(frame, len(sequence), 3):
            codon = sequence[location: location + 3]
            if codon == start_codon:
                start_positions.append(location)
            elif codon in stop_codons:
                while start_positions:
                    start_pos = start_positions.pop(0)
                    orf = sequence[start_pos:location + 3]
                    protein_seq = str(Seq(orf).translate(to_stop=True))
                    if protein_seq not in proteins:  # Avoid duplicates
                        proteins.add(protein_seq)
    
    return proteins

def get_reverse_complement(sequence):
    "Return the reverse complement of the sequence."
    seq_obj = Seq(sequence)
    return str(seq_obj.reverse_complement())

def main():
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", help="FASTA file", required=True) #Specify FASTA file
    args = parser.parse_args()

    sequences = get_sequences(args.file)
    
    # Find ORFs in the original and reverse complement sequences
    all_proteins = set()  # Use a set to avoid duplicates
    for seq_id, sequence in sequences.items():
        orfs = find_orfs(sequence)
        all_proteins.update(orfs)
        
        rev_sequence = get_reverse_complement(sequence)
        rev_orfs = find_orfs(rev_sequence)
        all_proteins.update(rev_orfs)

    # Output distinct protein strings
    for protein in all_proteins:
        print(protein)

if __name__ == "__main__":
    main()

## Q3
[almualzm@login509-02-l Week3and4]$ nano gene_finder1.py
[almualzm@login509-02-l Week3and4]$ emacs rosalind_input.txt
[almualzm@login509-02-l Week3and4]$ python gene_finder1.py -f rosalind_input.txt
MISHNHTPVFGWP
MS
MRKEEAERNKRYMLRATFCA
MRVSASLNRTYLLVNI
MHKTLLVTLPYFLSGLKGDPVDSGTVSSL
MYYDTSKSPREGCQAPN
MCGLERCQYPSVVCP
MAVPVFLSSLLF
MHKTLLVTYISCFVQLLLFACLLQ
MPLRESLSAVPVESCLARSVHVVTVSGSGSSDSARSS
MGHNSSRLARLVKAIRKLECDCGIS
MPRGFTRLKNYHN
MPFTITLERG
MVMLRATFCA
MPST
MIRVRVRGKDAKHLINCDNS
MN
MGVAMCGLERCQYPSVVCP
MFGCRVGLLVSRIITIN
MKRLNKSEAAAKPCRGSYYPLSRVIVKGMRKEEAERNKRYMLRATFCA
MSSPYPDPGQATVHAALRYC
MALTSLAKRELLCPIVVVMYYDTSKSPREGCQAPN
MLRATFCA

## Q4
[almualzm@login509-02-l Week3and4]$ emacs Quesstion4.sh
[almualzm@login509-02-l Week3and4]$ bash Quesstion4.sh
../ncbi_dataset/data/GCA_000007125.1/GCA_000007125.1_ASM712v1_genomic.fna
../ncbi_dataset/data/GCA_000008545.1/GCA_000008545.1_ASM854v1_genomic.fna
../ncbi_dataset/data/GCA_000008565.1/GCA_000008565.1_ASM856v1_genomic.fna
../ncbi_dataset/data/GCA_000008625.1/GCA_000008625.1_ASM862v1_genomic.fna
../ncbi_dataset/data/GCA_000008725.1/GCA_000008725.1_ASM872v1_genomic.fna
../ncbi_dataset/data/GCA_000006745.1/GCA_000006745.1_ASM674v1_genomic.fna
../ncbi_dataset/data/GCA_000006825.1/GCA_000006825.1_ASM682v1_genomic.fna
../ncbi_dataset/data/GCA_000006865.1/GCA_000006865.1_ASM686v1_genomic.fna
../ncbi_dataset/data/GCA_000008605.1/GCA_000008605.1_ASM860v1_genomic.fna
../ncbi_dataset/data/GCA_000008785.1/GCA_000008785.1_ASM878v1_genomic.fna
../ncbi_dataset/data/GCA_000008525.1/GCA_000008525.1_ASM852v1_genomic.fna
../ncbi_dataset/data/GCA_000008745.1/GCA_000008745.1_ASM874v1_genomic.fna
../ncbi_dataset/data/GCA_000027305.1/GCA_000027305.1_ASM2730v1_genomic.fna
../ncbi_dataset/data/GCA_000091085.2/GCA_000091085.2_ASM9108v2_genomic.fna
[almualzm@login509-02-l Week3and4]$ ls
gene_finder_14.txt  Quesstion4.sh   README_34.md        rosalind_input.txt~
gene_finder1.py     Quesstion4.sh~  rosalind_input.txt
[almualzm@login509-02-l Week3and4]$ emacs gene_finder_14.txt
[almualzm@login509-02-l Week3and4]$ git add Week3and4
fatal: pathspec 'Week3and4' did not match any files
[almualzm@login509-02-l Week3and4]$ git add -r Week3and4
error: unknown switch `r'
usage: git add [<options>] [--] <pathspec>...

    -n, --dry-run         dry run
    -v, --verbose         be verbose

    -i, --interactive     interactive picking
    -p, --patch           select hunks interactively
    -e, --edit            edit current diff and apply
    -f, --force           allow adding otherwise ignored files
    -u, --update          update tracked files
    --renormalize         renormalize EOL of tracked files (implies -u)
    -N, --intent-to-add   record only the fact that the path will be added later
    -A, --all             add changes from all tracked and untracked files
    --ignore-removal      ignore paths removed in the working tree (same as --no-all)
    --refresh             don't add, only refresh the index
    --ignore-errors       just skip files which cannot be added because of errors
    --ignore-missing      check if - even missing - files are ignored in dry run
    --chmod (+|-)x        override the executable bit of the listed files
    --pathspec-from-file <file>
                          read pathspec from file
    --pathspec-file-nul   with --pathspec-from-file, pathspec elements are separated with NUL character

    
## Q5
[almualzm@login509-02-l Week3and4]$ cp gene_finder1.py genefinder2.py
[almualzm@login509-02-l Week3and4]$ emacs gene_finder2.py

#This code was generated with the assistance of ChatGPT (version 3.5) and Yazeed Alroogi

from argparse import ArgumentParser  # Used to parse command-line arguments.
from Bio import SeqIO  # Used to read and write sequence data in various formats, including FASTA.
from Bio.Seq import Seq  # Sequence manipulation, including getting the reverse complement.

def get_sequences(file_path):
    """Read the FASTA file and return a dictionary of sequences."""
    sequences = {}  # Store Seq data
    for record in SeqIO.parse(file_path, "fasta"):  # Read the FASTA file.
        # Retrieves the sequence ID and the sequence itself, converting the sequence to a string.
        sequences[record.id] = str(record.seq)  
    return sequences

def find_orfs(sequence, min_length):
    """Find all ORFs in a given DNA sequence and filter by length."""
    start_codon = "ATG"  # Start codon for translation.
    stop_codons = ["TAA", "TAG", "TGA"]  # List of stop codons.
    proteins = set()  # Set to store unique protein sequences.

    # Check three different reading frames.
    for frame in range(3):
        start_positions = []  # List to store positions of start codons.
        for location in range(frame, len(sequence), 3):  # Iterate through the sequence in codons.
            codon = sequence[location: location + 3]  # Get the current codon.
            if codon == start_codon:
                # Record the position of the start codon.
                start_positions.append(location)  
            elif codon in stop_codons:
                # If a stop codon is found, extract ORFs from start positions.
                while start_positions:
                    start_pos = start_positions.pop(0)  # Get the first start position.
                    orf = sequence[start_pos:location + 3]  # Extract the ORF.
                    # Calculate the length in codons (divided by 3).
                    orf_length = len(orf) // 3  
                    if orf_length >= min_length:  # Check if ORF meets the length requirement.
                        protein_seq = str(Seq(orf).translate(to_stop=True))  # Translate ORF to protein sequence.
                        if protein_seq not in proteins:  # Avoid duplicates.
                            proteins.add(protein_seq)  # Add the unique protein sequence to the set.
    
    return proteins  # Return the set of unique proteins.

def get_reverse_complement(sequence):
    """Return the reverse complement of the sequence."""
    seq_obj = Seq(sequence)  # Create a Seq object from the sequence.
    return str(seq_obj.reverse_complement())  # Return the reverse complement as a string.

def main():
    parser = ArgumentParser()  # Create argument parser.
    parser.add_argument("-f", "--file", help="FASTA file", required=True)  # Specify FASTA file.
    parser.add_argument("-l", "--length", type=int, default=100, help="Minimum ORF length in codons")  # Specify minimum length for ORFs.
    args = parser.parse_args()  # Parse command-line arguments.

    sequences = get_sequences(args.file)  # Read sequences from the provided FASTA file.
    
    # Find ORFs in the original and reverse complement sequences.
    all_proteins = set()  # Use a set to avoid duplicates.
    for seq_id, sequence in sequences.items():
        # Find ORFs in the original sequence.
        orfs = find_orfs(sequence, args.length)  # Pass the min length to the function.
        all_proteins.update(orfs)  # Update the set of all proteins with found ORFs.
        
        # Get the reverse complement of the sequence.
        rev_sequence = get_reverse_complement(sequence)  
        rev_orfs = find_orfs(rev_sequence, args.length)  # Find ORFs in the reverse complement.
        all_proteins.update(rev_orfs)  # Update the set with found ORFs from reverse complement.

    # Output distinct protein strings.
    for protein in all_proteins:
        print(protein)  # Print each unique protein sequence.

if __name__ == "__main__":
    main()  # Call the main function to execute the program.

    [almualzm@login509-02-r Week3and4]$ emacs run_gene_finder.sh
[almualzm@login509-02-r Week3and4]$ bash run_gene_finder.sh
Processing ../ncbi_dataset/data/GCA_000007125.1/GCA_000007125.1_ASM712v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000007125.1/GCA_000007125.1_ASM712v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCA_000008545.1/GCA_000008545.1_ASM854v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000008545.1/GCA_000008545.1_ASM854v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCA_000008565.1/GCA_000008565.1_ASM856v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000008565.1/GCA_000008565.1_ASM856v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCA_000008625.1/GCA_000008625.1_ASM862v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000008625.1/GCA_000008625.1_ASM862v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCA_000008725.1/GCA_000008725.1_ASM872v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000008725.1/GCA_000008725.1_ASM872v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCF_000007125.1/GCF_000007125.1_ASM712v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000007125.1/GCF_000007125.1_ASM712v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCF_000008545.1/GCF_000008545.1_ASM854v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000008545.1/GCF_000008545.1_ASM854v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCF_000008565.1/GCF_000008565.1_ASM856v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000008565.1/GCF_000008565.1_ASM856v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCF_000008625.1/GCF_000008625.1_ASM862v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000008625.1/GCF_000008625.1_ASM862v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCF_000008725.1/GCF_000008725.1_ASM872v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000008725.1/GCF_000008725.1_ASM872v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCA_000006745.1/GCA_000006745.1_ASM674v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000006745.1/GCA_000006745.1_ASM674v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCA_000006825.1/GCA_000006825.1_ASM682v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000006825.1/GCA_000006825.1_ASM682v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCA_000006865.1/GCA_000006865.1_ASM686v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000006865.1/GCA_000006865.1_ASM686v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCA_000008605.1/GCA_000008605.1_ASM860v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000008605.1/GCA_000008605.1_ASM860v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCA_000008785.1/GCA_000008785.1_ASM878v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000008785.1/GCA_000008785.1_ASM878v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCF_000006745.1/GCF_000006745.1_ASM674v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000006745.1/GCF_000006745.1_ASM674v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCF_000006825.1/GCF_000006825.1_ASM682v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000006825.1/GCF_000006825.1_ASM682v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCF_000006865.1/GCF_000006865.1_ASM686v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000006865.1/GCF_000006865.1_ASM686v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCF_000008605.1/GCF_000008605.1_ASM860v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000008605.1/GCF_000008605.1_ASM860v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCF_000008785.1/GCF_000008785.1_ASM878v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000008785.1/GCF_000008785.1_ASM878v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCA_000008525.1/GCA_000008525.1_ASM852v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000008525.1/GCA_000008525.1_ASM852v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCA_000008745.1/GCA_000008745.1_ASM874v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000008745.1/GCA_000008745.1_ASM874v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCA_000027305.1/GCA_000027305.1_ASM2730v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000027305.1/GCA_000027305.1_ASM2730v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCA_000091085.2/GCA_000091085.2_ASM9108v2_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000091085.2/GCA_000091085.2_ASM9108v2_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCF_000008525.1/GCF_000008525.1_ASM852v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000008525.1/GCF_000008525.1_ASM852v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCF_000008745.1/GCF_000008745.1_ASM874v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000008745.1/GCF_000008745.1_ASM874v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCF_000027305.1/GCF_000027305.1_ASM2730v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000027305.1/GCF_000027305.1_ASM2730v1_genomic_proteins.txt
Processing ../ncbi_dataset/data/GCF_000091085.2/GCF_000091085.2_ASM9108v2_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000091085.2/GCF_000091085.2_ASM9108v2_genomic_proteins.txt

## Q6
[almualzm@login509-02-l Week3and4]$ emacs gene_finder3.py
#This code was generated with the assistance of ChatGPT (version 3.5) and Yazeed Alroogi

from argparse import ArgumentParser  # Used to parse command-line arguments.
from Bio import SeqIO  # Used to read and write sequence data in various formats, including FASTA.
from Bio.Seq import Seq  # Sequence manipulation, including getting the reverse complement.

def get_sequences(file_path):
    """Read the FASTA file and return a dictionary of sequences."""
    sequences = {}  # Store Seq data
    for record in SeqIO.parse(file_path, "fasta"):  # Read the FASTA file.
        # Retrieves the sequence ID and the sequence itself, converting the sequence to a string.
        sequences[record.id] = str(record.seq)  
    return sequences

def find_orfs(sequence, min_length, rbs_length):
    """Find all ORFs in a given DNA sequence and filter by length and presence of RBS."""
    start_codon = "ATG"  # Start codon for translation.
    stop_codons = ["TAA", "TAG", "TGA"]  # List of stop codons.
    rbs_sequence = "AGGAGG"  # Shine-Dalgarno sequence to look for as RBS.
    proteins = set()  # Set to store unique protein sequences.

    # Check three different reading frames.
    for frame in range(3):
        start_positions = []  # List to store positions of start codons.
        for location in range(frame, len(sequence), 3):  # Iterate through the sequence in codons.
            codon = sequence[location: location + 3]  # Get the current codon.
            if codon == start_codon:
                # Record the position of the start codon.
                start_positions.append(location)  
            elif codon in stop_codons:
                # If a stop codon is found, extract ORFs from start positions.
                while start_positions:
                    start_pos = start_positions.pop(0)  # Get the first start position.
                    orf = sequence[start_pos:location + 3]  # Extract the ORF.
                    # Calculate the length in codons (divided by 3).
                    orf_length = len(orf) // 3  
                    
                    # Check if ORF meets the length requirement.
                    if orf_length >= min_length:
                        # Check for RBS in the upstream sequence.
                        upstream_start = max(0, start_pos - rbs_length)  # Ensure not to go out of bounds.
                        upstream_sequence = sequence[upstream_start:start_pos]
                        if rbs_sequence in upstream_sequence:  # Check if RBS is present.
                            protein_seq = str(Seq(orf).translate(to_stop=True))  # Translate ORF to protein sequence.
                            if protein_seq not in proteins:  # Avoid duplicates.
                                proteins.add(protein_seq)  # Add the unique protein sequence to the set.
    
    return proteins  # Return the set of unique proteins.

def get_reverse_complement(sequence):
    """Return the reverse complement of the sequence."""
    seq_obj = Seq(sequence)  # Create a Seq object from the sequence.
    return str(seq_obj.reverse_complement())  # Return the reverse complement as a string.

def main():
    parser = ArgumentParser()  # Create argument parser.
    parser.add_argument("-f", "--file", help="FASTA file", required=True)  # Specify FASTA file.
    parser.add_argument("-l", "--length", type=int, default=100, help="Minimum ORF length in codons")  # Specify minimum length for ORFs.
    parser.add_argument("-r", "--rbs_length", type=int, default=20, help="Length to scan upstream for RBS in bp")  # Specify upstream search length.
    args = parser.parse_args()  # Parse command-line arguments.

    sequences = get_sequences(args.file)  # Read sequences from the provided FASTA file.
    
    # Find ORFs in the original and reverse complement sequences.
    all_proteins = set()  # Use a set to avoid duplicates.
    for seq_id, sequence in sequences.items():
        # Find ORFs in the original sequence.
        orfs = find_orfs(sequence, args.length, args.rbs_length)  # Pass the min length and RBS length to the function.
        all_proteins.update(orfs)  # Update the set of all proteins with found ORFs.
        
        # Get the reverse complement of the sequence.
        rev_sequence = get_reverse_complement(sequence)  
        rev_orfs = find_orfs(rev_sequence, args.length, args.rbs_length)  # Find ORFs in the reverse complement.
        all_proteins.update(rev_orfs)  # Update the set with found ORFs from reverse complement.

    # Output distinct protein strings.
    for protein in all_proteins:
        print(protein)  # Print each unique protein sequence.

if __name__ == "__main__":
    main()  # Call the main function to execute the program.
[almualzm@login509-02-r Week3and4]$ emacs run_ribosome.sh
[almualzm@login509-02-r Week3and4]$ bash run_ribosome.sh
Processing ../ncbi_dataset/data/GCA_000007125.1/GCA_000007125.1_ASM712v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000007125.1/GCA_000007125.1_ASM712v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCA_000008545.1/GCA_000008545.1_ASM854v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000008545.1/GCA_000008545.1_ASM854v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCA_000008565.1/GCA_000008565.1_ASM856v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000008565.1/GCA_000008565.1_ASM856v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCA_000008625.1/GCA_000008625.1_ASM862v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000008625.1/GCA_000008625.1_ASM862v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCA_000008725.1/GCA_000008725.1_ASM872v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000008725.1/GCA_000008725.1_ASM872v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCF_000007125.1/GCF_000007125.1_ASM712v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000007125.1/GCF_000007125.1_ASM712v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCF_000008545.1/GCF_000008545.1_ASM854v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000008545.1/GCF_000008545.1_ASM854v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCF_000008565.1/GCF_000008565.1_ASM856v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000008565.1/GCF_000008565.1_ASM856v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCF_000008625.1/GCF_000008625.1_ASM862v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000008625.1/GCF_000008625.1_ASM862v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCF_000008725.1/GCF_000008725.1_ASM872v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000008725.1/GCF_000008725.1_ASM872v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCA_000006745.1/GCA_000006745.1_ASM674v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000006745.1/GCA_000006745.1_ASM674v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCA_000006825.1/GCA_000006825.1_ASM682v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000006825.1/GCA_000006825.1_ASM682v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCA_000006865.1/GCA_000006865.1_ASM686v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000006865.1/GCA_000006865.1_ASM686v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCA_000008605.1/GCA_000008605.1_ASM860v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000008605.1/GCA_000008605.1_ASM860v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCA_000008785.1/GCA_000008785.1_ASM878v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000008785.1/GCA_000008785.1_ASM878v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCF_000006745.1/GCF_000006745.1_ASM674v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000006745.1/GCF_000006745.1_ASM674v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCF_000006825.1/GCF_000006825.1_ASM682v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000006825.1/GCF_000006825.1_ASM682v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCF_000006865.1/GCF_000006865.1_ASM686v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000006865.1/GCF_000006865.1_ASM686v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCF_000008605.1/GCF_000008605.1_ASM860v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000008605.1/GCF_000008605.1_ASM860v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCF_000008785.1/GCF_000008785.1_ASM878v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000008785.1/GCF_000008785.1_ASM878v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCA_000008525.1/GCA_000008525.1_ASM852v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000008525.1/GCA_000008525.1_ASM852v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCA_000008745.1/GCA_000008745.1_ASM874v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000008745.1/GCA_000008745.1_ASM874v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCA_000027305.1/GCA_000027305.1_ASM2730v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000027305.1/GCA_000027305.1_ASM2730v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCA_000091085.2/GCA_000091085.2_ASM9108v2_genomic.fna
Output saved to ../ncbi_dataset/data/GCA_000091085.2/GCA_000091085.2_ASM9108v2_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCF_000008525.1/GCF_000008525.1_ASM852v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000008525.1/GCF_000008525.1_ASM852v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCF_000008745.1/GCF_000008745.1_ASM874v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000008745.1/GCF_000008745.1_ASM874v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCF_000027305.1/GCF_000027305.1_ASM2730v1_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000027305.1/GCF_000027305.1_ASM2730v1_genomic_proteins3.txt
Processing ../ncbi_dataset/data/GCF_000091085.2/GCF_000091085.2_ASM9108v2_genomic.fna
Output saved to ../ncbi_dataset/data/GCF_000091085.2/GCF_000091085.2_ASM9108v2_genomic_proteins3.txt
