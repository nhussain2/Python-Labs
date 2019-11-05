"""
This program is a debugged progream that inputs current and outputs power
according to the different resistance values.
Author: Naveed Hussain
"""

# Values
current = []
power = []
currentSum = 0
powerSum = 0
resistance = [16, 27, 39, 56, 81]

# Takes input and adds to list
for i in range(5):
    current.append(eval(input('Enter current value: ')))
    power.append(resistance[i] * current[i]**2)

print("\nResistance \t Current \t Power")

# Output        
for x in range(5):
     print(resistance[x],"\t\t", current[x],"\t\t", power[x],"\n")
     currentSum += current[x];
     powerSum += power[x];

print("Total: \t\t", currentSum, "\t\t" ,powerSum)
