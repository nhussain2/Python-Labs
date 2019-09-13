#ITM 313 - Naveed Mustafa Hussain hw1

# Takes name input and then displays a greeting message
name = input("Please enter your full name: ")
print("Hello, ", name, ", nice meeting you.")

# Takes temperature input in Fahrenheit
temp_f = eval(input("\nEnter temperature in Fahrenheit: "))
celcius = 5.0/9.0 * (temp_f - 32.0)

# Prints result for conversion to Celcius
print("For a Fahrenheit temperature of", temp_f, "degrees,")
print("The equivalent Celcius temperature is %.2f degrees." % celcius)

# Takes temperature input in Celcius
temp_c = eval(input("\nEnter temperature in Celcius: "))
fahrenheit = (temp_c * 9.0/5.0) + 32.0

# Prints result for conversion to Fahrenheit
print("For a Celcius temperature of", temp_c, "degrees,")
print("The equivalent Fahrenheit temperature is %.2f degrees." % fahrenheit)



