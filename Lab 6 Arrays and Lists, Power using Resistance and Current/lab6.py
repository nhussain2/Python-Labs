"""
Lab 6- Arrays/Lists
This program stores values in a list named resistance, and then inputs 5 values
in list for current and then calculates the power and stores all these values
in a table and outputs it.
Author: Naveed Hussain
"""

# values for resistance list:

resistance = [16,27,39,56,81]


# input values for current list:

current = []
print("Enter currents for the 5 resistance values:")

for i in range(len(resistance)):
    n = eval(input("Enter value: "))
    current.append(n)


# calculate power for each resistance value

power = []

for i in range(len(resistance)):
    p = resistance[i] * current[i] **2
    power.append(p)

# prints the output

print()
print("Resistance\tCurrent\t\tPower")

for i in range(len(resistance)):
    print(resistance[i],"\t\t", current[i],"\t\t", power[i])
    


