# Given amino acid sequence
amino_seq = "KVRMFTSELDIMLSVNGPADQIKYFCRHWT"

# Calculate the number of amino acids and total bases in the ORF
num_amino_acids = len(amino_seq)
total_bases = (num_amino_acids * 3) + 3

# Display the results with descriptive strings
print(f"The number of amino acids is: {num_amino_acids}")
print(f"The total number of bases in the ORF (including stop codon) is: {total_bases}")
