# This code was generated with the assistance of ChatGPT (version 3.5) and Yazeed Alroogi

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
