# parsing_fasta.py
# For this exercise the pseudo-code is required (in this same file)
# Write a script that:
# a) Reads sprot_prot.fasta line by line
# b) Copies to a new file ONLY the record(s) that are not from Homo sapiens
# b) And prints their source organism and sequence lenght
# Use separate functions for the input and the output
fasta = open('sprot_prot.fasta')       #open the fasta file
nonhumans = open('nonhumans.fasta','w')#create output file
header = ''                            #create empty variable for 1st line of fasta seqs
seq = ''                               #create empty variable for aa sequence of fasta
for line in fasta:                     #loop for each line of fasta
    if line[0] == '>' and seq == '':   #consider 1st line of the fasta file
        header = line                  #fill variable header
    elif line[0] != '>':               #consider each line that is not a new seq
        seq = seq  + line              #fill seq with aa seq
    elif line[0] == '>' and seq != '': #consider finishing of the previous seqs
        if 'Homo sapiens' not in header: #considder only those without 'Homo sapiens'
            nonhumans.write(header +seq) #write header and seq to new file

if 'Homo sapiens' not in header:       #same reasoning for last seq
    nonhumans.write(header + seq)      #it doesn't work and I honestly wrote this by memory,
                                       # can't really grasp the concept here
nonhumans.close()
