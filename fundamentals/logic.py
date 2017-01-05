# Booleans
# -------------------------------------------

# True & False
True # = 1
False # = 0
True + True # = 2
bool([]) # False
bool('') # False
bool('Jackie Robinson') # True
bool(None) # False

# Comparisons
5 == 5 # True
5 == 10 # False
3 < 4 # True
10 > 5 # True
1 >= 0 # True
5 <= 6 # True
"Hello" != "World" # True
football_player is None # True
football_player = "Peyton Manning"
football_player is None # False

# Note: Python doesn't do Type coercion so we don't need === like JavaScript

# if / else / elif
if "Lebron" != "Jordan":
    print("Yeah, stop comparing them please...")

age = 57
if age >= 65:
    print("Time to Retire!")
elif age <= 46:
    print("You've got a long ways to go")
else:
    print("Less than 20 years left to go, hang in there")

if not age >= 30:
    print("Whippersnapper")

# Containment / Inclusion
numbers = [5, 3, 10, 30, 12]
5 in numbers # = True
"e" in "Pizza" # = False

days_open ["Monday", "Wednesday", "Friday", "Saturday"]
today = "Wednesday"

if today not in days_open:
    print("Sorry, we're closed")
