# miscellaneous.py
# For the following exercises, pseudo-code is not required

# Exercise 1
# Create a list L of numbers from 21 to 39
# print the numbers of the list that are even
# print the numbers of the list that are multiples of 3
list = range(21,40)
for i in list:
    if i % 2 == 0:
        print i
    elif i % 3 == 0:
        print i


# Exercise 2
# Print the last two elements of L
g = len(L)
print L[(g-2):(g+1)]




# Exercise 3
# What's wrong with the following piece of code? Fix it and
# modify the code in order to have it work AND to have "<i> is in the list"
# printed at least once

L = ['1', '2', '3']
for i in range(10):
    if str(i) in str(L):
        print('%d is in the list'%i)
    else:
        print('%d not found'%i)


# Exercise 4
# Read the first line from the sprot_prot.fasta file
# Split the line using 'OS=' as delimiter and print the second element
# of the resulting list
fasta = open('sprot_prot.fasta')
seq = fasta.readline().split('OS=')
print seq[1]


# Exercise 5
# Split the second element of the list of Exercise 4 using blanks
# as separators, concatenate the first and the second elements and print
# the resulting string
blanks = seq[1].split(' ')
first_2_elements = [blanks[0],blanks[1]]
conc = ' '.join(first_2_elements)
print conc




# Exercise 6
# reverse the string 'asor rosa'
string1 = 'asor rosa'
string2 = string1[::-1]
print string2

# Exercise 7
# Sort the following list: L = [1, 7, 3, 9]
L = [1, 7, 3, 9]
L.sort()
print L


# Exercise 8
# Create a new sorted list from L = [1, 7, 3, 9] without modifying L
L = [1, 7, 3, 9]
g = sorted(L)
print g



# Exercise 9
# Write to a file the following 2 x 2 table:
# 2 4
# 3 6
outfile = open('table_2x2.txt','w')
outfile.write('2\t4\n3\t6')
outfile.close()
