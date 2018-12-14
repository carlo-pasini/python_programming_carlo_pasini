#1 Write a program that reads the file with neuron lengths (neuron_data.txt)
#  and stores neuron lengths as floating point numbers into a list.
neuron_lenght = []
for line in open('neuron_data.txt'):
    neuron_lenght.append(float(line.strip()))

print neuron_lenght

#2 Extend the program so that it read data form neuron_data-2.txt and
#stores primary and secondary neuron lengths to different lists.
primary = []
secondary = []
for line in open('neuron_data-2.txt'):
    g = line.split()
    if g[0] == '1':
        primary.append(float(g[1]))
    else:
        secondary.append(float(g[1]))

#3 Extend program 2 so that it calculates the neuron length average separately
#for primary and secondary neurons. Print the two averages: which neurons are on average longer?
primary = []
secondary = []
for line in open('neuron_data-2.txt'):
    g = line.split()
    if g[0] == '1':
        primary.append(float(g[1]))
    else:
        secondary.append(float(g[1]))

print sum(primary)/len(primary), sum(secondary)/len(secondary)
if (sum(primary)/len(primary)) > (sum(secondary)/len(secondary)):
    print'Primary neurons are on average longer!'
else:
    print 'Secondary neurons are on average longer'


#4Extend program 3 so that it calculates the standard deviation of the neuron length.

av_1 = sum(primary)/len(primary)
av_2 = sum(secondary)/len(secondary)
from math import sqrt
def std_1():
    tot = 0.0
    for i in primary:
        tot = tot + (i - av_1)**2
    return sqrt(1/len(primary) * tot)
