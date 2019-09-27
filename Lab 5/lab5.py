"""
This program will ask user to make a selection on which inertia to calculate,
based on the selection, it will ask the user to input the appropriate values
and then by calling appropriate function, it will calculate and output result
"""


# Beam Moment Function

def beamMoment(b, h):
    i = (b * (h ** 3))/12
    print("The beam moment is i=%.2f m^4"%(i))

# Annulus Moment Function

def annulusMoment(r1, r2):
    i = (3.14/4)*((r2**4)-(r1**4))
    print("The annulus moment is i=%.2f m^4"% (i))


# Main program Function
def main():
    
    # Display moment options
    
    print("Choose the moment of inertia you wish to calculate by entering number:")
    print("1. Beam Moment")
    print("2. Annulus Moment")

    # Takes input choice
    
    choice = eval(input("Enter choice:"))

    # Condition to check what values to take input

    # For Beam moment:
    
    if (choice == 1):
        print("Calculate Beam Moment")
        b = eval(input("Enter the base: "))
        h = eval(input("Enter the height: "))
        beamMoment(b,h)

    # For Annulus moment:
    
    elif (choice == 2):
        print("Calculate Annulus Moment")
        r1 = eval(input("Enter inner radius: "))
        r2 = eval(input("Enter outer radius: "))
        annulusMoment(r1,r2)

    # Error Message:
    
    else:
        print("You did not choose a valid number")

main()
    
        
        
