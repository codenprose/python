# Hello World
print("Hello World")

# Variables and Data Types
# ------------------------------------------------------------------------------

# Variables - Containers for information

# String
name = "Daniel K. Hunter"

# Number
age = 10 * 3 - 1

# Dictionary
dkh = { 
    'name': name,
    'age': age
}

# List
my_list = [name, age, dkh]

# Numbers

# Division always returns a float
8 / 2 # = 4.0

# Strings

# Interpolation
"Status Message: you currently have {} vistors on {}".format(90, "danielkhunter.com")
# "Status Message: you current have 90 visitors on danielkhunter.com"

"=" * 35 # ==================================

"hello world".split() # ["hello", "world"]

":".join(['nfl', 'nba', 'mlb']) # "nfl:nba:mlb"

"Favorite NBA players: {}".format(", ".join(['Lebron James', 'Russell Westbrook', 'Kevin Durant']))
# "Favorite NBA players: Lebron James, Russell Westbrook, Kevin Durant"

"Index Method".index("I") # returns first index match, 0

# covert number to string
str(3) # "3"

# Lists
primary = ['blue', 'red', 'yellow']
secondary = ['purple', 'orange', 'green']
list_concatenation = primary + secondary
numbers = [1, 2, 4]
numbers.extend([6, 8, 10]) # Adds each individual item in the given list to the numbers list
numbers.append([12, 14]) # Adds the given list as one item to the numbers list

# Error Types
# ------------------------------------------------------------------------------

# Name Error - You try to use a variable that doesn't exist
print(i_dont_exist)

# Type Error - Trying to add an integer to a string e.g. 2 + "Two"
print("Hello World" + 5)

# Syntax Error - You've written some code incorrectly and Python can't understand it
print("This print function isn't closed"

# Input function
# ----------------------
# Capture user input from command line
age = input("What's your age? ")
