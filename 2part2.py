#Written by Shiven Desai
import pickle

# define the filename for the pickle file
FILENAME = 'vegetables.dat'

# load the dictionary from the pickle file, or create a new one if the file doesn't exist
try:
    with open(FILENAME, 'rb') as file:
        vegetables = pickle.load(file)
except FileNotFoundError:
    vegetables = {}

# function to display the menu and get the user's choice
def get_user_choice():
    print('Menu:')
    print('1. View all vegetables')
    print('2. Add a new vegetable and price')
    print('3. Change the price of an existing vegetable')
    print('4. Delete an existing vegetable and price')
    print('5. Exit')
    choice = input('Enter your choice (1-5): ')
    while choice not in ['1', '2', '3', '4', '5']:
        choice = input('Invalid choice. Enter your choice (1-5): ')
    return int(choice)

# function to display all the vegetables and their prices
def view_vegetables():
    if not vegetables:
        print('There are no vegetables in the dictionary.')
    else:
        print('Vegetables:')
        for vegetable, price in vegetables.items():
            print(f'{vegetable}: ${price:.2f}')

# function to add a new vegetable and price
def add_vegetable():
    vegetable = input('Enter the name of the vegetable: ')
    while vegetable in vegetables:
        vegetable = input('That vegetable already exists. Enter the name of the vegetable: ')
    price = float(input('Enter the price of the vegetable: '))
    vegetables[vegetable] = price
    print(f'{vegetable} added with a price of ${price:.2f}.')

# function to change the price of an existing vegetable
def change_price():
    vegetable = input('Enter the name of the vegetable: ')
    while vegetable not in vegetables:
        vegetable = input('That vegetable does not exist. Enter the name of the vegetable: ')
    price = float(input('Enter the new price of the vegetable: '))
    vegetables[vegetable] = price
    print(f'The price of {vegetable} has been changed to ${price:.2f}.')

# function to delete an existing vegetable
def delete_vegetable():
    vegetable = input('Enter the name of the vegetable: ')
    while vegetable not in vegetables:
        vegetable = input('That vegetable does not exist. Enter the name of the vegetable: ')
    del vegetables[vegetable]
    print(f'{vegetable} has been deleted.')

# loop to display the menu and execute the user's choice
while True:
    choice = get_user_choice()
    if choice == 1:
        view_vegetables()
    elif choice == 2:
        add_vegetable()
    elif choice == 3:
        change_price()
    elif choice == 4:
        delete_vegetable()
    else:
        with open(FILENAME, 'wb') as file:
            pickle.dump(vegetables, file)
        print('Goodbye!')
        break
