#PARSING A GFF FILE

#task 1: look for all lines with Mutagenesis
f = open('uniprot_file.gff') #prepare file for reading
l = f.readlines() #create a list in which each element is a line of the file
for line in l: #loop to go through each line and check for 'Mutagenesis'
    if 'Mutagenesis' in line:
        print line

#task 2: identify position where only single point mutations occur
f = open('uniprot_file.gff').readlines() #create a list with the file's lines as objects
for line in f:
    if 'Mutagenesis' in line: #look for lines containig 'Mutagenisis'
        g = line.split('\t')  #create a list where each element is a different field of the file (spaced by \t)
        if g[3] == g[4]:
            print g[3]

#task 3: find the occurred mutation
f = open('uniprot_file.gff').readlines() #create a list with the file's lines as objects
for line in f:
    if 'Mutagenesis' in line: #look for lines containig 'Mutagenisis'
        g = line.split('\t')  #create a list where each element is a different field of the file (spaced by \t)
        if g[3] == g[4]:
            a = g[8].index('->')
            print g[8][a-1:a+3]
