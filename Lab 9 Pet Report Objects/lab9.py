"""
Lab 9
This program prompts user to enter name, type and age of their pet and then
uses the object's accessor methods to retrieve this data and output it.
Author: Naveed Hussain
"""

class Pet():

    # Creates attributes for class
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    # Assigns value to the name field

    def set_name(self, name):
        self.__name = name

    # Assigns value to the animal type field

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    # Assigns value to the age field

    def set_age(self, age):
        self.__age = age

    # Returns the value of the name field

    def get_name(self):
        return self.__name

    # Returns the value of the animal type field

    def get_animal_type(self):
        return self.__animal_type

    # Returns the value of the age field

    def get_age(self):
        return self.__age

    # Main program

def main():
    name= ""
    animal_type= ""
    age=0
    ans="Y"

    while(ans=="Y"):

        # Input Pet details
        name = input("Enter the name of the pet: ")
        animal_type = input("Enter the animal type: ")
        age = eval(input("Enter the animal age: "))
        
        # Create Pet
        pet1 = Pet(name, animal_type, age)
    
        #Input Pet details
        pet1.set_name(name)
        pet1.set_animal_type(animal_type)
        pet1.set_age(age)
    
        # Output Pet details
        print("\nABOUT YOUR PET:")
        print("\nYour pet's name is ", pet1.get_name())
        print("Your pet's animal type is ", pet1.get_animal_type())
        print("Your pet's age is ", pet1.get_age())

        # Asks to re-enter pet details
        ans = input("\nWould you like to re-enter the details? Y/N")

main()





        
        
