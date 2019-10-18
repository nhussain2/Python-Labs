"""
Lab 7
Program that returns sum, mean, median, smallest, largest and number of numbers
read from data files stored.
Author: Naveed Hussain
"""
import statistics
import os

# Input filename
file = input("Enter a filename: ").strip()

# Condition that file exists
if os.path.isfile(file):

    # Open file entered and read values
    infile = open(file, "r")

    # Make list

    s = infile.read()
    datalist = [eval(x) for x in s.split()]

    # Calculations
    largest = max(datalist)
    smallest = min(datalist)
    total = sum(datalist)
    length = len(datalist)
    mean = total/length
    median = statistics.median(datalist)

    # Output
    print("The sum of the values is %.2f" %(total))
    print("The mean of the values is %.2f" % (mean))
    print("The median of the values is %.2f" %(median))
    print("The smallest value is %.2f" % (smallest))
    print("The largest value is %.2f" % (largest))
    print("The total number of values are %.2f" % (length))
    
    
# Condition that file does not exist, outputs error message
else:
    print("The file you entered does not exist!")
    
    
