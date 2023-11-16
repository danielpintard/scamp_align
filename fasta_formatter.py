#Formats plain text (.txt) of identifiers and sequences into fasta format. 

file = open('/Users/danielpintard/Documents/Code/Bioinformatics/scamp_align/SCAMP coding sequences.txt', 'r').read().strip() #original sequence file. best if plain text (txt). this can maybe get away with a docx but I have not tested that yet. nothing like and rtf though 
# file = open('/Users/danielpintard/Documents/Code/Bioinformatics/scamp_align/test_seqs.txt', 'r').read().strip()

sequences = file.split('\n')
sequences = [sequence.replace('\n', '') for sequence in sequences]

current_seq = []
indiv_seqs = []

for sequence in sequences: 
    if sequence: #if not empty line
        current_seq.append(sequence)
    else: #if line is empty 
        if current_seq: #if currently looped sequence is not empty 
            indiv_seqs.append(current_seq)
        current_seq = [] #reset current sequence for next in loop            
if current_seq:
    indiv_seqs.append(current_seq)

fasta_list = []

for sublist in indiv_seqs:
    if sublist: #is not empty
        sublist[0] = ">" + sublist[0].replace(':', '').replace(' ', '_')
        fasta_list.append(sublist)
    
#joining elements of sequence to make one losng string for sequences
for seq in range(len(fasta_list)):
    fasta_list[seq][1:] = ["".join(fasta_list[seq][1:])]

output_file = "SCAMP_coding_seqs.fasta" #output file name

with open(output_file, "w") as output:
    for sublist in fasta_list:
        header = sublist[0]
        sequence = sublist[1]
        output.write(header + "\n")
        output.write(sequence.replace(' ', '') + "\n" + '\n')
    

# Potential Improvements #
"""
I should refactor for following edge case:
------------------
First sequence

AAACCTCACTCACCACTGCC

second sequence

AATAAGGGGTCCTTACCTGA

third sequence

AGAATAAGTGTCAGCCAGTG
-------------------

It would be nice to always have the program return:
------------------
First sequence

AAACCTCACTCACCACTGCC

second sequence
AATAAGGGGTCCTTACCTGA

third sequence
AGAATAAGTGTCAGCCAGTG
-------------------

regardless of the amount of space between ID and sequence because that is a part of fasta format. This wouldn't be a fasta formatter if it didnt turn every txt file with sequences into a
viable fasta file. I can expand this to cover many other files (rtf's and any file that are IOwrapped with hidden text may be as pain in the ass)
"""