# For Loop
numbers = [1, 2, 3, 4]
for num in numbers:
    if num % 2 == 0:
        print('even')
    else:
        print('odd')

# While Loop
countdown = 10
while countdown:
    print(countdown)
    countdown -= 1

# Break
names = ["Kelly", "John", "Lisa", "Derrick", "Quit", "Bob"]
for name in names:
    if name == "Quit":
        break
    print(name)

# Continue (skips current index)
for name in names:
    if name == "Quit":
        continue
    print(name)
