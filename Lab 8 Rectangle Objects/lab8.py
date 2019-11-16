"""
Lab 8
This program has a class Rectangle that, when implemented, displays the
width, height, area and perimeter of each rectangle.
Author: Naveed Hussain
"""

# Create class for Rectangle

class Rectangle():

    # Constructor with width and height default values
    
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height


    def getPerimeter(self):
        p = 2*(self.width) + 2*(self.height)
        return p

    def getArea(self):
        a = (self.width) * (self.height)
        return a

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.height = height

def main():

    # Create rectangle1 and set width 4, height 40
    
    rectangle1 = Rectangle()
    rectangle1.setWidth(4)
    rectangle1.setHeight(40)

    # Output  for rectangle1

    print("\nRectangle 1")
    print("The width of the rectangle is %.2f" % (rectangle1.width))
    print("The height of the rectange is %.2f" % (rectangle1.height))
    print("The area of the rectangle is %.2f" % (rectangle1.getArea()))
    print("The perimeter of the rectangle is %.2f" %(rectangle1.getPerimeter()))
    
    # Create rectangle2 and set width 3.5, height 35.7
    
    rectangle2 = Rectangle()
    rectangle2.setWidth(3.5)
    rectangle2.setHeight(35.7)

    # Output for rectangle2
    
    print("\nRectangle 2")
    print("The width of the rectangle is %.2f" % (rectangle2.width))
    print("The height of the rectange is %.2f" % (rectangle2.height))
    print("The area of the rectangle is %.2f" % (rectangle2.getArea()))
    print("The perimeter of the rectangle is %.2f" %(rectangle2.getPerimeter()))
    
main()    
    
        
