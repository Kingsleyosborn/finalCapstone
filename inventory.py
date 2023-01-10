from tabulate import tabulate

class Shoes:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f'{self.country} {self.code} {self.product} {self.cost} {self.quantity}'

    def get_list(self):
        return f'{self.country},{self.code},{self.product},{self.cost},{self.quantity}'

shoes_list = []

#store the data into Class
def read_shoes_data():
    with open('inventory.txt', 'r') as f:
        lines = f.readlines()
        header = lines[0]
        for line in lines[1:]:
            try:
                country, code, product, cost, quantity = line.split(',')
                shoes_list.append(Shoes(country, code, product, int(cost), int(quantity)))
            except ValueError:
                pass

#rewrite the file from the shoe list
def re_write():
    f = open("inventory.txt", "w+", encoding="utf-8")
    f.write("Country,Code,Product,Cost,Quantity\n")
    for shoes in shoes_list:
        f.write(str((shoes.get_list())+"\n"))
    f.close()
    pass

#get the new shoe info and rewrite the txt
def capture_shoes():
    print('Please enter the following information: ')
    country = input('Country: ')
    code = input('Code: ')
    product = input('Product: ')
    cost = int(input('Cost: '))
    quantity = int(input('Quantity: '))
    print("New Shoes details have been added")
    shoes_list.append(Shoes(country, code, product, cost, quantity))
    re_write()

#use tabulate to show all stocks
def view_all():
    shoes_list_formatted = [shoe.get_list().split(',') for shoe in shoes_list]
    print(tabulate(shoes_list_formatted, headers=["Country", "Code", "Product", "Cost", "Quantity"]))

#for the lowest quantity of product, add 10 more pairs
def re_stock():
    min_quantity = min([shoe.quantity for shoe in shoes_list])
    shoe_to_re_stock = [shoe for shoe in shoes_list if shoe.quantity == min_quantity]
    if len(shoe_to_re_stock) == 1:
        print(f'Need to re-stock {shoe_to_re_stock[0].product}')
        print(f'There are {shoe_to_re_stock[0].quantity} pairs left')
        answer = input('Do you want to re-stock this shoe? (y/n) ')
        if answer == 'y':
            shoe_to_re_stock[0].quantity += 10
            print(f'{shoe_to_re_stock[0].product} is now re-stocked.')
            re_write()
    elif len(shoe_to_re_stock) > 1:
        print('Need to re-stock to following products: ')
        for shoes in shoe_to_re_stock:
            print(f"{shoes.product}")
            print(f'There are {shoes.quantity} pairs left')
            answer = input('Do you want to re-stock this shoe? (y/n) ')
            if answer == 'y':
                shoes.quantity += 10
                print(f'{shoes.product} is now re-stocked.')
                re_write()
                continue
            if answer == "n":
                continue



def search_shoe(code):
    shoe = [shoe for shoe in shoes_list if shoe.code == code]
    if len(shoe) == 1:
        return shoe[0]
    else:
        return None

def value_per_item():
    for shoe in shoes_list:
        value = shoe.cost * shoe.quantity
        print(f'The total value for {shoe.product} is {value}')

def highest_qty():
    max_quantity = max([shoe.quantity for shoe in shoes_list])
    shoe_with_highest_qty = [shoe for shoe in shoes_list if shoe.quantity == max_quantity]
    if len(shoe_with_highest_qty) == 1:
        print(f'The shoe with the highest quantity is {shoe_with_highest_qty[0].product}, with {shoe_with_highest_qty[0].quantity}.')
    elif len(shoe_with_highest_qty) > 1:
        print(f'The shoes with the highest quantity are ')
        for shoe in shoe_with_highest_qty:
            print(f'{shoe.product}, with {shoe.quantity} pair.')

def main():
    read_shoes_data()
    while True:
        print('1 - View all shoes')
        print('2 - Capture a shoe')
        print('3 - Re-stock a shoe')
        print('4 - Search for a shoe')
        print('5 - Calculate the value per item')
        print('6 - Find the product with highest quantity')
        print('7 - Quit')
        choice = int(input('Please enter a choice: '))
        if choice == 1:
            view_all()
        elif choice == 2:
            capture_shoes()
        elif choice == 3:
            re_stock()
        elif choice == 4:
            code = input('Please enter the shoe code: ')
            result = search_shoe(code)
            if result:
                print(result)
            else:
                print(f'Shoe with code {code} not found')
        elif choice == 5:
            value_per_item()
        elif choice == 6:
            highest_qty()
        elif choice == 7:
            break
        else:
            print('Invalid choice.')

if __name__ == '__main__':
    main()