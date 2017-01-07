def open_list(file):
    return file.read().split('\n')

# make a list that will hold onto our items
try:
    f = open('shopping_list.txt', 'r')
    shopping_list = open_list(f)
    f.close()
except FileNotFoundError:
    shopping_list = []

print("What do you want to pick up at the store?")

# print out intructions on how to use the app)
def show_help():
    info = """
"Enter 'DONE' to stop adding items."
"Enter 'HELP' to display this help."
"Enter 'SHOW' to display current list of items."
"Enter 'SAVE' to save the current list of items."
"""
    print(info)

show_help()

def display_list(list):
    for item in list:
        print(item)

def add_to_list(new_item):
    # add new items to our list
    shopping_list.append(new_item)
    print("Added new item {}. List now has {} items.".format(new_item, len(shopping_list)))

def save_list(list):
    file = open('shopping_list.txt', 'w')
    file.write('\n'.join(list))
    file.close()

# ask for new items
while True:
    user_input = input("> ").upper()
    # be able to quit the app
    if user_input == 'DONE':
        break
    elif user_input == 'HELP':
        show_help()
        continue
    elif user_input == 'SHOW':
        display_list(shopping_list)
        continue
    elif user_input == 'SAVE':
        save_list(shopping_list)
        continue
    add_to_list(user_input)

# print out the list
print("Here's your list:")
display_list(shopping_list)
