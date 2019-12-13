"""
Final Project ITM 313
This program creates three classes: Circle, Square and Cube and provides
accessor, mutator and find_area() methods to calculate the area of the shape
as well as a method display() to print the class name and area, using private
attributes. Ten objects will be created and added to a list based on a random
number generator b/w 1-3 for each shape. In the end, the user is promptsed
to save the result on a file or just print it on the screen. If the user chooses
file, then the program will ask the user to input a file name to save to.
Author: Naveed Hussain
"""

import math
import random

# Create Circle Class
class Circle():

    # Construct Circle object
    def __init__(self, radius=1):
        self.__radius = radius

    # Set Radius
    def set_radius(self, radius):
        self.__radius = radius

    # Get Area
    def find_area(self):
        return self.__radius * self.__radius * math.pi

# Create Square Class
class Square():

    # Construct Square object
    def __init__(self, side=2.3):
        self.__side = side

    # Set Side
    def set_side(self, side):
        self.__side = side

    # Get Area
    def find_area(self):
        return self.__side * self.__side

# Create Cube Class
class Cube():

    # Construct Cube object
    def __init__(self, length=2, width=2, height=2):
        self.__length= length
        self.__width= width
        self.__height= height

    # Set Length
    def set_length(self, length):
        self.__length = length

    # Set Width
    def set_width(self, width):
        self.__width= width

    # Set Height
    def set_height(self, height):
        self.__height= height

    # Get Area
    def find_area(self):
       return 2*((self.__length * self.__width) + (self.__length * self.__height) + (self.__height * self.__width))
def main():

    shapename=[]
    shapearea=[]

    # Create 10 Random Shapes
    for x in range(10):
        
        choice = random.randint(1,3)
        
    # Add conditions for each number and link to shape
        if (choice == 1):
            circle = Circle()
            shapename.append("Circle")
            shapearea.append("%.2f"%(circle.find_area()))

        elif (choice == 2):
            square = Square()
            shapename.append("Square")
            shapearea.append("%.2f"%(square.find_area()))

        elif (choice == 3):
            cube = Cube()
            shapename.append("Cube")
            shapearea.append(cube.find_area())

    print("Results have been generated")

    # Display Function: Conditions based on user answer 
    def display():
        if ans == str(1):

            # Input Filename to save
            filename = input("Create a file name to save the results: ")

            # Zip lists together and open and write them on file
            zipped = list(zip(shapename,shapearea))
            file1 = open(filename, "w")
            file1.write("Name \t Area")
            for i in zipped:
                file1.write("\n" +str(i))
            file1.close()
            print("The file has been saved.")
    
        elif ans == str(2):
            print("\nName \t Area")
            print("------------------")

            # Print list on-screen
            for object in range(len(shapename)):
                print(shapename[object],"\t",shapearea[object])

        # Condition that throws error message in case number is invalid       
        else:
            print("You did not input a valid number!")

    # Ask user to choose print on-screen or on-file
    ans = input("Enter 1 to print on file, Enter 2 to print on screen: ")
    display()

   
    
main()











