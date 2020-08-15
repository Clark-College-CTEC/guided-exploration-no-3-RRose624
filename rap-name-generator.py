# Guided Exploration No. 3
# Ryan C. Rose

# Import the "random" library for use in the program.
import random

# Initialize the "possible_names" list for future use.
possible_names = []

# Open/Create a text file titled "rape-names-output.txt" and assign writing access to it to the outputFile variable
outputFile = open('rap-names-output.txt', 'w')

# Temporarily opens the file "rap-names.txt" for reading within the "dataFile" variable for the duration of the "with" block.
with open('rap-names.txt', 'r') as dataFile:
    # Cycles through every line of "dataFile"
    for name in dataFile:
        # Appends the lines from "dataFile" to the "possible_names" list and performs a right strip on the lines to remove the line feed.
        possible_names.append(name.rstrip())

# Asks the user to input how many rap names they'd like to create (Which will be used in the following loop)
count = int(input('How many rap names would you like to create? '))
# Asks the user how many parts the rap names will have.
parts = int(input('How many parts should the name contain? '))

# Loop for the user-inputted number of rap names
for i in range(count):
    # Initialize/Clear the "name_parts" list.
    name_parts = []
    # Loop for the user-inputted number of parts to be used for the names
    for j in range(parts):
        # Append "name_parts" with a random entry from the "possible_names" list.
        name_parts.append(
            possible_names[random.randint(0, len(possible_names)-1)])

# Write the rap name to the "outputFile" by formatting a string made up of the "name_parts" list with its entries separated by spaces and culminating in a line feed
    outputFile.write(f"{' '.join(name_parts)}\n")
# Print out to the console what was just written to the "outputFile"
    print(f"{' '.join(name_parts)}")

# Close the "outputFile"
outputFile.close()
