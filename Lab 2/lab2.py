"""
Lab 2
This program takes 2 primary colors as input and displays the
secondary color created.
Author = Naveed Hussain
"""

print("Mix primary colors (red, blue, yellow) to find out the secondary produced!")

# input the two primary colors

first = input("Enter the first primary color: ")
second = input("Enter the second primary color: ")

# for Purple

if (first.lower() == "red" ) and (second.lower() == "blue"):
    print("Secondary color is Purple")
elif (first.lower() == "blue") and (second.lower() == "red"):
    print("Secondary color is Purple")

# for Orange

elif (first.lower() == "red" ) and (second.lower() == "yellow"):
    print("Secondary color is Orange")
elif (first.lower() == "yellow") and (second.lower() == "red"):
    print("Secondary color is Orange")

# for Green

elif (first.lower() == "blue" ) and (second.lower() == "yellow"):
    print("Secondary color is Green")
elif (first.lower() == "yellow") and (second.lower() == "blue"):
    print("Secondary color is Green")

# for the same values

elif (first.lower()==second.lower()):
    print("You input the same primary colors!")

# Error message for any non-primary color

else:
    print("Error: You did not input the correct primary colors!")






    
