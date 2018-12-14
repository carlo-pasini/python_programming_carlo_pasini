#13 Read the multiple sequence FASTA file sprot_prot.fasta
#and write to a new file only the records from Homo sapiens.
fasta = open('sprot_prot.fasta')
humans = open('humans.txt','w')
header = ''
seqs = ''
for line in fasta:
    if line[0] == '>' and seq = '':
        header = line
    elif line[0] != '>':
        seq = seq + line
    elif line[0] == '>' and seq != '':
        if 'Homo sapiens' in header:
            humans.write(header + seq)
if 'Homo sapiens' in header:
    humans.write(header + seq)
humans.close()
