"""
Lab 1
This program calculates and displays the area of a triangle
Author: Naveed Hussain
"""

print("Thank you for using my program.")
name = input("Please enter your full name: ")

# Greeting message
print("")
print("Hello ", name)
print("Welcome to my program. This program is about finding the area of a triangle.")
print("The program will ask you to enter the base and the height values of a triangle.")

print("")
base = eval(input("Enter the base value: "))
height = eval(input("Enter the height value: "))

# Formula for area of triangle
area = 1/2 * base * height

# Prints result
print("")                    
print("Here is the result: ")
print("Base=", base, " inches")
print("Height=", height, " inches")
print("Area = %.3f inches" % area)

print("")
print("Thank you and have a nice day.")
print("Good bye!")


