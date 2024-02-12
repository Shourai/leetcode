import os
import sys

# Get first argument
argv = sys.argv[1]

# Split the argument in the number and the name
string = argv.split(" ")

# Format number into 4 digit format
problem_number = string[0]
problem_number = problem_number.rstrip(".")
problem_number = f"{int(problem_number):04}"

# Lowercase the name and change spaces to _
problem_name = ""

for word in string[1:]:
    problem_name += "_" + word.lower()

# Add extension
problem_name += ".py"

# Create file
os.system(f"touch {problem_number}{problem_name}")
