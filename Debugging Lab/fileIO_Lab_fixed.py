"""
This program was debugged. It is meant to read a set of values from a text file
and return the total, mean and median from the file.
Author: Naveed Hussain
"""

import os
import statistics

def main():

    # Prompt user to enter filename
    
    f1 = input("Enter a filename: ").strip()

    if os.path.isfile(f1):

        # Open file for input after checking for it
        infile = open(f1, "r")
        all = infile.read()
        
        scores = [ eval(x) for x in all.split() ]
        print("Calculating data from the file...\n")

        # Output
        print("There are", len(scores), " scores")
        print("The total is ", sum(scores))
                      
        mean = sum(scores) / len(scores)
        print("The mean is %.2f" % mean)
                      
        medians = statistics.median(scores)
        print("The median is", medians)

        # Close file after reading it
        infile.close()

    # Error message in case file does not exist
    else:
        print("Failed to open file!")
        
main()


