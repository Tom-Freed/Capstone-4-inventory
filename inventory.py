#========Libraries==========
from tabulate import tabulate


#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # class method to return cost of the shoe 
    def get_cost(self):
        return int(self.cost)

    # class method to return quantity of the shoe 
    def get_quantity(self):
        return int(self.quantity)
    
    # class method to return code of the shoe 
    def get_code(self):
        return self.code
    
    # class method to set quantity of the shoe
    def set_quantity(self, stock):
        self.quantity = int(self.quantity) + stock

    # class method to return a string representation of the shoe 
    def __str__(self):
        return f'{self.country},{self.code},{self.product},{self.cost},{self.quantity}'.strip()


#=============Shoe list===========
shoe_list = []
# Error list of any entries not added
error_list = []
# A breakline to be used throughout program
breakline = '-' * 100


#==========Functions outside the class==============

# Function to import data from inverntory.txt
def read_shoes_data():
    # open inventory.txt and store entries in data
    with open('inventory.txt', 'r', encoding='utf-8') as f:
        data = f.readlines()
    
    # Iterate through each entry in data (excluding 1st entry)
    for entry in data[1:]:
        # try to create a Shoe object for each entry and append to shoe_list
        try:
            split_entry = entry.split(',')
            shoe_entry = Shoe(split_entry[0], split_entry[1], split_entry[2], split_entry[3], split_entry[4])
            shoe_list.append(shoe_entry)
        # if this fails add the entry to error_list
        except:
            error_list.append(entry)
    
    # print completion message and number of errors
    print(f'''{breakline}
Shoe data from inventory.txt has been imported
Number of entries unable to be added: {len(error_list)}''')


# Function to capture and store shoe data
def capture_shoes():
    # Store user inputs, ensure only ints are entered for cost and quantity
    capture_country = input('Enter the country: ')
    capture_code = input('Enter the code: ')
    capture_product = input('Enter the product: ')
    while True:
        try:
            capture_cost = int(input('Enter the cost: '))
            break
        except ValueError:
            print('Enter integers only, please try again')
    while True:
        try:
            capture_quantity = int(input('Enter the quantity: '))
            break
        except ValueError:
            print('Enter integers only, please try again')
    
    # Create Shoe object from user entries and append to shoe_list
    capture_shoe = Shoe(capture_country, capture_code, capture_product, capture_cost, capture_quantity)
    shoe_list.append(capture_shoe)

    # NOT IN INSTRUCTIONS - Inluded as otherwise capture_shoes data is not saved after program ends
    # Disregard and comment out next 4 lines if not needed 
    with open('inventory.txt', 'w', encoding='utf-8') as f:
        f.write('Country,Code,Product,Cost,Quantity\n')
        for shoe in shoe_list:
            f.write(str(shoe) + '\n')
    
    # print completion message
    print(f'{breakline}\nShoe data stored\n{breakline}')


# Function to print a table of all shoe details
def view_all():
    # Empty list to append to
    shoe_list_str = []
    # for each entry in shoe_list split the entry around ',' and append to shoe_list_str
    for entry in shoe_list:
        shoe_list_str.append(str(entry).split(','))
    # print details in shoe_list_str in a table 
    print(f'{breakline}\nShoe details:')
    print(tabulate(shoe_list_str, headers=['Country','Code','Product','Cost','Quantity'], tablefmt='fancy_grid'))


# Funtion to find shoe with lowest stock and give the user the option to add more stock 
def re_stock():
    # for each object in shoe_list get_quantity of shoe and return shoe with lowest stock
    lowest = min(shoe_list, key=lambda object:object.get_quantity())
    # Convert lowest object to a string, split around ',' and add to a list
    lowest_list = [str(lowest).split(',')]
    # print a table of lowest_list
    print(f'{breakline}\nShoe with the lowest stock:')
    print(tabulate(lowest_list, headers=['Country','Code','Product','Cost','Quantity'], tablefmt='fancy_grid'))
    
    
    stock_choice = ''
    while True:
        # Take user input on whether they want to restock the shoe, upper() the input for error handling
        stock_choice = input('Would you like to restock this shoe (Y/N): ').upper()
        
        # if user inputs 'Y', ask for the quantity of stock to be added
        if stock_choice == 'Y':
            while True:
                # try and convert add_stock to int, if successful break out of while loop
                try:
                    add_stock = int(input('Enter the quantity of stock you would like to add to this shoe: '))
                    break
                # if ValueError occurs, print error message and loop
                except ValueError:
                    print('Enter integers only, please try again')
            
            # Add the value of add_stock to the quantity of lowest
            lowest.set_quantity(add_stock)
            
            # write the contents of shoe_list to inventory.txt 
            with open('inventory.txt', 'w', encoding='utf-8') as f:
                f.write('Country,Code,Product,Cost,Quantity\n')
                for shoe in shoe_list:
                    f.write(str(shoe) + '\n')
            
            # print completion method
            print(f'{breakline}\nStock list updated\n{breakline}')
            return
        
        # if user inputs 'N', return to menu
        elif stock_choice == 'N':
            return
        
        # print error message for any other input
        else:
            print('Incorrect entry, please try again')


# Function to allow user to search for shoe via shoe code
def search_shoe():
    # Take user input, strip() and upper() for error handling
    search_code = input(f'{breakline}\nEnter the shoe code: ').strip().upper()
    
    # Check if search_code matches a shoe code in shoe_list
    for shoe in shoe_list:
        # if a match is found set search_match to shoe
        if shoe.get_code() == search_code:
            search_match = shoe
            break
        # else set search_match to None
        else:
            search_match = None
    
    # if search_match == None, print message and return to menu
    if search_match == None:
        print(f'{breakline}\nNo shoe matching this code was found')
        return
    # if a match is found, print a table of details of matching shoe
    else:
        print(f'{breakline}\nShoe matching this code:')
        search_list = [str(search_match).split(',')]
        print(tabulate(search_list, headers=['Country','Code','Product','Cost','Quantity'], tablefmt='fancy_grid'))


# Function to print table of shoe details and value
def value_per_item():
    value_list = []
    # for each shoe in shoe_list, calculate value, create string of shoe details and append to value_list
    for entry in shoe_list:
        value = entry.get_cost() * entry.get_quantity()
        temp = f'{str(entry)}, {str(value)}'
        value_list.append(temp.split(','))
    
    # print a table of shoe details and values
    print(f'{breakline}\nShoe details and values:')
    print(tabulate(value_list, headers=['Country','Code','Product','Cost','Quantity', 'Value'], tablefmt='fancy_grid'))


# Function to print details of shoe with highest quantity
def highest_qty():
    # for each object in shoe_list get_quantity of shoe and return shoe with highest stock
    highest = [str(max(shoe_list, key=lambda object:object.get_quantity())).split(',')]
    
    # print table of details of shoe with highest stock
    print(f'{breakline}\nShoe with the highest stock:')
    print(tabulate(highest, headers=['Country','Code','Product','Cost','Quantity'], tablefmt='fancy_grid'))


#==========Main Menu=============

# print welcome message and run read_shoes_data
print(f'{breakline}\nWelcome to the warehouse')
read_shoes_data()

# display menu options and take user input
choice = ''
while choice != 'ex':
    menu = input(f'''{breakline}
Select one of the following options:
cs - capture and store data about a shoe
va - view table of details of all shoes
rs - find and restock the shoe with lowest quantity
ss - use code to search for shoe
vi - view table of details and values of all shoes
hq - view shoe with highest quantity
ex - exit program
: ''')
    # Run different funtions depending on input
    if menu == 'cs':
        capture_shoes()
    elif menu == 'va':
        view_all()
    elif menu == 'rs':
        re_stock()
    elif menu == 'ss':
        search_shoe()
    elif menu == 'vi':
        value_per_item()
    elif menu == 'hq':
        highest_qty()
    # Allow user to exit and print error message
    elif menu == 'ex':
        print('Exiting program')
        break
    # Error handling for any other input
    else:
        print('Incorrect entry, please try again')