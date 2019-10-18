"""
HW7
This program reads data from ticket.txt and outputs a report into output.txt
that includes minimum, maximum and average ticket price.
Author: Naveed Hussain
"""

# Read ticket file

read_ticket = open("ticket.txt", "r")
line = read_ticket.read()

# Make split list of all values on ticket file

for x in line:
    splitLine = line.split()

# Remove column titles present in split list

splitLine.remove("Ticket")
splitLine.remove("Price")

price = []

# Alternate through list and add price values to new price list

for i in range(1, len(splitLine), 2):
    price.append(eval(splitLine[i]))

# Calculate minimum, maximum and average values from price list

maximum = max(price)
minimum = min(price)
avg = (sum(price))/(len(price))

read_ticket.close()


# Output ticket report on output.txt

report_ticket = open("output.txt", "w")
report_ticket.write("**************************************\n")
report_ticket.write("\tTICKET REPORT\t\n")
report_ticket.write("**************************************\n\n")
report_ticket.write("There are %.0f tickets in the database.\n\n" % (len(price)))
report_ticket.write("Maximum Ticket price is $%.2f.\n" % (maximum))
report_ticket.write("Minimum Ticket price is $%.2f.\n" % (minimum))
report_ticket.write("Average Ticket price is $%.2f.\n\n" % (avg))
report_ticket.write("Thank you for using our ticket system!\n\n")
report_ticket.write("**************************************")

report_ticket.close()


