"""
Lab 3
This program reads an unspecified number of integers, counts the positive
and negative values, computes the total and average (not counting zeros) and
ends program at zero.
Author : Naveed Hussain
"""

# initial values before loop

pos = 0
neg = 0
sum = 0
how_many = 0
number = 1 

# Condition to end program
while( number != 0):

# Input number and add to count and sum

    number = eval(input("Enter an integer, the input ends if it is 0:"))
    how_many += 1
    sum = sum + number 

# To count positive and negative values
    if (number > 0):
        pos += 1
    if (number < 0):
        neg += 1

# If first input was zero and no more values were added

if (how_many == 1):
    print("You didn't enter any number")

# Final calculations and info displayed
    
if (how_many >1):
    # how many -1 to count for extra zero
    average = float(sum/(how_many-1))
    
    print("The number of positives is",pos)
    print("The number of negatives is",neg)
    print("The total is", sum)
    print("The average is %.2f" % (average))

