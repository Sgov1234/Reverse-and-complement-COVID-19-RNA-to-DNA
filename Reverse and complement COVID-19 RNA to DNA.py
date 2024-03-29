import Bio
from Bio.Seq import Seq
from Bio import SeqIO

print('DNA Sequence:')
file_path = r'C:\Users\shaan\Documents\Business & Projects\Python Projects\COVID-19 DNA Sequence.txt'
with open(file_path, 'r') as file:
    file_contents = file.read()
    print(file_contents)

#sequence functions
print(' Complemented DNA Sequence:')
my_seq = Seq(file_contents)
DNA = my_seq.complement()
print(DNA)

# Define a DNA sequence
dna_sequence = my_seq

# Transcribe DNA sequence to RNA
rna_sequence = my_seq.transcribe()

# Print the RNA sequence
print('RNA Sequence:')
print(rna_sequence)
