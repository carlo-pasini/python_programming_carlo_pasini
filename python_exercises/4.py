fasta = open('hemoglobins.txt')
humans = open('humans.txt','w')
seqs = ''
for line in fasta:
    if line[0] == '>'and  seqs == '':
        header = line
    elif line[0] != '>':
        seqs = seqs + line
    elif line[0] == '>' and seqs != '':
        if 'Homo sapiens' in header:
            humans.write(header + seqs)
        header = line
        seqs = ''

if 'Homo sapiens' in header:
    humans.write(header + seqs)

humans.close()


with open('hemoglobins.txt') as fasta:
    fasta = fasta.read().split('>')
    for seq in fasta:
        line = seq.split('\n')
        for i in range(1,len(line)):
            if  line[1].startswith('M') and seq.count('W') > 1:
                with open('trp_seqs.txt','w') as output:
                    output.write(seq)
            
