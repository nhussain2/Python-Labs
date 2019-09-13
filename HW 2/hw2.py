"""
HW 2
This program asks user to enter number of books purchased and then calculates
and displays the points awarded.
Author: Naveed Hussain
"""

print("Calculate the points you have earned from your book purchases!")

# Input number of books

num_books = eval(input("Enter the number of books purchased: "))

# Point conditions

if (num_books == 0):
    points = 0
    
elif (num_books == 1):
    points = 5
    
elif (num_books == 2):
    points = 15

elif (num_books == 3):
    points = 30

elif (num_books >= 4):
    points = 60

# Displays output points

print("You have earned", points,"points from your purchases!")
