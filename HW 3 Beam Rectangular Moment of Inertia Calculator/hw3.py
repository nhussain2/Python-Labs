"""
HW 3
This program takes input of relevant Beam dimensions based on the type of beam
and calculates the beam's rectangular moment of inertia.
Author: Naveed Hussain
"""

menu = 1
while (menu != 0):

# Provide menu options for the beams

    print()
    print("This program calculates the rectangular moment of inertia for beams.")
    print("Choose the type of beam:")
    print("1. I-beam")
    print("2. Rectangular beam")
    print("3. Cylindrical beam")

# Takes menu item input

    menu = eval(input("Enter beam number to choose beam type, enter 0 to end the program:"))

    # Asks for data required and calculates accordingly

    if (menu == 1):
        print("I-beam")
        b = eval(input("Enter value of b in inches:"))
        B = eval(input("Enter value of B in inches:"))
        h = eval(input("Enter value of h in inches:"))
        H = eval(input("Enter value of H in inches:"))
        
        I = ((B*(H**3))-(b*(h**3)))/12

        print("The rectangular moment of inertia is %.2f in^4" % (I))
        
    elif (menu == 2):
        print("Rectangular beam")
        b = eval(input("Enter value of b in inches:"))
        h = eval(input("Enter value of h in inches:"))

        I = (b*(h**3))/12

        print("The rectangular moment of inertia is %.2f in^4" % (I))

    elif (menu == 3):
        print("Cylindrical beam")
        r = eval(input("Enter value of r in inches:"))

        I = (3.142 * (r**4))/4
        
        print("The rectangular moment of inertia is %.2f in^4" % (I))
        
# Terminating message

    elif (menu == 0):
        print("Program ended.")

# In case an invalid input is put

    else:
        print("This is not a valid menu item. Try again.")
