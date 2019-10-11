"""
Midterm
This program takes input of relevant beam dimensions based on the type of beam
and calculates the beam's rectangular moment of inertia by calling the
appropriate beam function
Author: Naveed Hussain
"""

# Beam Functions

# I-beam function:

def i_beam(b,B,h,H):
    print("I-beam")

    # input values within function
    
    b = eval(input("Enter value of b in inches:"))
    B = eval(input("Enter value of B in inches:"))
    h = eval(input("Enter value of h in inches:"))
    H = eval(input("Enter value of H in inches:"))
        
    I = ((B*(H**3))-(b*(h**3)))/12
    
    # Function calculates and returns moment of inertia
    
    return I

# Rectangular beam function:

def rectangular_beam(b,h):
    print("Rectangular beam")

    # input values within the function
    
    b = eval(input("Enter value of b in inches:"))
    h = eval(input("Enter value of h in inches:"))

    I = (b*(h**3))/12

    # Function calculates and returns moment of inertia

    return I

# Cylindrical beam function:

def cylindrical_beam(r):
    print("Cylindrical beam")

    # input values within the function

    r = eval(input("Enter value of r in inches:"))

    I = (3.142 * (r**4))/4
    
    # Function calculates and returns moment of inertia
    
    return I
    



# Main program
def main():

    
    # Dummy Values

    b=0
    B=0
    h=0
    H=0
    r=0
    menu = 1
    
    while (menu != 0):

        # provide menu options for the beams

        print()
        print("This program calculates the rectangular moment of inertia for beams.")
        print("Choose the type of beam:")
        print("1. I-beam")
        print("2. Rectangular beam")
        print("3. Cylindrical beam")

        # Takes menu item input

        menu = eval(input("Enter beam number to choose beam type, enter 0 to end the program:"))

        # Conditions to call each beam function

        if (menu == 1):
            print("The rectangular moment of inertia is %.2f in^4" % (i_beam(b,B,h,H)))

        elif (menu == 2):
            print("The rectangular moment of inertia is %.2f in^4" % (rectangular_beam(b,h)))

        elif (menu == 3):
            print("The rectangular moment of inertia is %.2f in^4" % (cylindrical_beam(r)))
        # Terminating message

        elif (menu == 0):
            print("Program ended.")

        # In case an invalid input is put

        else:
            print("This is not a valid menu item. Try again.")
        

main()
    
