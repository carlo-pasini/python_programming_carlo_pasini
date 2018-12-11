# average_function.py
# For this exercise the pseudo-code is required (in this same file)
# Write a function that calculates the average of the values of
# any vector of 10 numbers
# Each single value of the vector should be read from the keyboard
# and added to a list.
# Print the input vector and its average
# Define separate functions for the input and for calculating the average

def average_vector():
    def input():
        input1 = input('Insert 1st number: ')
        input2 = input('Insert 2nd number: ')
        input3 = input('Insert 3rd number: ')
        input4 = input('Insert 4th number: ')
        input5 = input('Insert 5th number: ')
        input6 = input('Insert 6th number: ')
        input7 = input('Insert 7th number: ')
        input8 = input('Insert 8th number: ')
        input9 = input('Insert 9th number: ')
        input10 = input('Insert 10th number')
        v = [float(input1),float(input2),float(input3),float(input4),float(input5),float(input6),float(input7),float(input8),float(input9),float(input10)]
        return v
    def av_vector():
        return sum(v) / len(v)
    print av_vector
    print v
