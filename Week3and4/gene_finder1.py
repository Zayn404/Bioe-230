# This code was generated with the assistance of ChatGPT (version 3.5) and Yazeed Alroogi

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
    orfs = []
    
    # Check three different reading frames
    for frame in range(3): #iterates over the three possible reading frames
        start_positions = []
        for location in range(frame, len(sequence), 3): #iterates through the seq in steps of codons
            codon = sequence[location: location + 3]
            if codon == start_codon:
                start_positions.append(location)
            elif codon in stop_codons:
                while start_positions:
                    start_pos = start_positions.pop(0)
                    orf = sequence[start_pos:location + 3]
                    if orf not in orfs:  # Avoid duplicates
                        orfs.append(orf)
    
    return orfs

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
