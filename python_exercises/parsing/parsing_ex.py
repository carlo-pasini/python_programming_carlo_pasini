#1) read content of file line by line and print it
seq = open('SingleSeq.fa')
for line in seq:
    print line

#2 open fasta file, read it line by line and then write its content to another file
seq = open('SingleSeq.fa')
seq_2 = open('SingleSeq2.fa', 'w')
for line in seq:
    seq_2.write(line)

seq_2.close()

#3 read fasta file and print only the header:
seq = open('SingleSeq.fa')
for line in seq:
    if line[0] == '>':
        print line

#4 read fasta file and write only headder to another file
seq = open('SingleSeq.fa')
seq_2 = open('SingleSeq2.fa','w')
for line in seq:
    if line[0] == '>':
        seq_2.write(line)

seq_2.close()

#5 open fasta file and write to new file only the sequence
seq = open('SingleSeq.fa')
seq_2= open('SingleSeq2.fa', 'w')
for line in seq:
    if line[0] != '>':
        seq_2.write(line)

seq_2.close()

#4+5 merge the two preceding excercises
fasta = open('SingleSeq.fa')
header = open('SingleSeq2.fa','w')
body = open('SingleSeq3.fa','w')
for line in fasta:
    if line[0] == '>':
        header.write(line)
    else:
        body.write(line)

header.close()
body.close()

#6 read fasta file line by line, save the header and the sequence in
# two different files, then print header and sequnce separetely
fasta = open('SingleSeq.fa')
b = ''
for line in fasta:
    if line[0] == '>':
        a = line
    else:
        b = b + line.strip() #strip eliminates leading and trailing white spaces
                             #senza strip il print stamperebbe una riga alla volta
print a, b
# N.B. se avessi scritto solo b = line (senza b = b + line) avrei ottenuto
# solo l'ultima line con il print

#7 implement task6 by also counting the numeber of cysteines
fasta = open('SingleSeq.fa')
b = ''
cys = 0
for line in fasta:
    if line[0] == '>':
        a = line
    else:
        b = b + line.strip()

for i in range(0,len(b)): # much simpler to write cys = b.count('C')
    if b[i] == 'C':
        cys = cys + 1

print a, b, cys

#8nread fasta file then write it to a file only if it's from Homo sapiens
seq_fasta = open('SingleSeq.fa')
header = ''
seq = ''
for line in seq_fasta:
    if line[0] == '>':
        if 'Homo sapiens' in line:
            header = line
    else:
        if header:               # the if conditions with empty object means that it's
            seq = seq + line     # false, unless it was filled(in this case is always false)

if header:                       #here the conditions for header might be fullfilled
    print header + seq
else:
    print 'This seq is not from H sapiens'

#9 write record headers to new files
seq_fasta = open('SwissProt-Human.fasta')
header = open('headers.txt','w')
for line in seq_fasta:
    if line[0] == '>':
        header.write(line)

header.close()

#10 write the fasta sequences to a new file, separated by a blanck eliminates
seq_fasta = open('SwissProt-Human.fasta')
seqs = open('seqs.txt','w')
for line in seq_fasta:
    if line[0] == '>':
        seqs.write('\n')
    elif line[0] != '>':
        seqs.write(line)

seqs.close()

#11 Read a file in FASTA format and copy to a new file the records' Accession Numbers (AC)
seq_fasta = open('SwissProt-Human.fasta')
seq = open('AccessionNumbers.txt','w')
for line in seq_fasta:
    if line[0] == '>':
        g = line.split('|') #creates list of all lines containig '>', in which each object is split according to '|'
        seq.write(g[1]+'\n')#writes to a new file only the accession number, every AC has a new line

seq.close()

#13 Read the multiple sequence FASTA file sprot_prot.fasta
#and write to a new file only the records from Homo sapiens.
seq_fasta = open('sprot_prot.fasta')
outfile = open('records_Hs.txt','w')
seq = ''
header = ''
for line in seq_fasta:
    if line[0] == '>' and seq == '':
        header = line
    elif line[0] != '>':
        seq = seq + line
    elif line[0] == '>' and seq != '':
        outfile.write(header + seq)
        seq =''
        header = line

if 'Homo sapiens' in header:
    outfile.write(header + seq)
outfile.close()

#12 Read FASTA records from a file
#   Count (and print) the cysteine residues in each sequence.
fasta = open('sprot_prot.fasta')
cys_count = open('cys_count.txt')
header = ''
seqs = ''
for line in fasta:
    if line[0] == '>' and seqs == '':
        header = line
    elif line[0] != '>':
        seqs = line.count('C')
    elif line[0] == '>' and seqs != '':
        print header, seqs, '\n'
        header = line
        seqs = ''

'''14) Read a multiple sequence file in FASTA format and only write to a new file the records the sequences of which start with a methionine ('M') and have at least two tryptophan residues ('W')
First:
Read a multiple sequence file in FASTA format and write to a new file only the records of the sequences starting with a methionine ('M')
Then
Read a multiple sequence file in FASTA format and write to a new file only the records of the sequences having at least two tryptophan residues ('W')
Finally merge the two steps
'''
fasta = open('SwissProt-Human.fasta')
output = open('only_trp.txt','w')
header = ''
seqs = ''
for line in fasta:
    if line[0] == '>' and seqs == '':
        header = line
    elif line[0] != '>':
        seqs = seqs + line
    elif line[0] == '>' and seqs != '':
        if seqs[0][0] == 'M' and seqs.count('W') > 1:
            output.write(header + seqs)
        header = line
        seqs = ''

if seqs [0][0] == 'M' and seqs.count('W') > 1:
    output.write(header + seqs)

'''15) Read a Genbank record and write to a file the nucleotide sequence in FASTA format. Extract and write to a file the gene sequence from the Candida albicans genomic DNA, chromosome 7, complete sequence (file ap006852.gbk)
'''

file = open('ap006852.gbk')
chr = open('candida_genome.fasta','w')
g = file.readlines()
for line in g:
    if 'ORIGIN' in line:
        f = g.index(line)
        only_seq = g[(f+1)::]

many_lines = []
for line in only_seq:
    many_lines = many_lines + line.split(' ')

l = range(949621)
for number in l:
    for line in many_lines:
        if str(number) == line:
            many_lines.remove(line)
    print many_lines
