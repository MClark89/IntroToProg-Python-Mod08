# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# MClark, 3.8.2021, Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProducts = []


class Product(object):
    """Stores data about a product:
    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        MClark, 3.8.2021, Created Script
    """

    # initializer
    def __init__(self, product= str, price= float):
        self.__product = product
        self.__price = price

    @property
    # getter
    def product_name(self):
        return str(self.__product)

    @product_name.setter
    # setter
    def product_name(self, product):
        if product == "":
            print("This must be a product")
        elif str(product).isnumeric():
            print("No Numbers, please")
        else:
            self.__product = product

    @property
    # getter
    def product_price(self):
        return float(self.__price)

    def add_to_list(self, list_of_rows):
        row = {"Product": self.__product, "Price": self.__price}
        list_of_rows.append(row)
        return list_of_rows, "Data Saved."

    @product_price.setter
    def product_price(self, value: float):
        if str(value).isnumeric():
            self.__product_price = float(value)
        else:
            raise Exception("Prices must be numbers")


# Data -------------------------------------------------------------------- #


# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:
    methods:
        save_data_to_file(file_name, list_of_product_objects): saves list to a file
        read_data_from_file(file_name): -> (a list of product objects)
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        MClark, 3.8.2021, Modified code to complete assignment 8
    """

    def read_data_from_file(file_name, list_of_rows):
        with open(file_name, "r") as f:
            for row in f:
                p1, p2 = row.split(",")
                row = {"Product": p1.strip(), "Price": p2.strip()}
                list_of_rows.append(row)
            return list_of_rows

    @staticmethod
    def save_data_to_file(file_name, list_of_rows):
        with open(file_name, "w") as f:
            table = ""
            for row in list_of_rows:
                new_row = row["Product"] + "," + str(row["Price"]) + "\n"
                table += new_row
            f.write(table)
            return "Data Saved"


# Processing  ------------------------------------------------------------- #


# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    @staticmethod
    # Main Menu Selection
    def print_menu_tasks():
        """  User Menu"""
        print("""
        *** Main Menu ***

        1) Display Current Products
        2) Add a Product to the List
        3) Save Data to File and Exit Program
        """)

    @staticmethod
    def input_menu_choice():
        user_choice = str(input("Please Select a Choice from 1 - 3: ")).strip()
        print()
        return user_choice

    @staticmethod
    def print_current_products_in_list(list_of_rows):
        print("The Current List is:")
        for row in list_of_rows:
            print("Product: " + row["Product"] + ' | ' + "Price: " + str("$%.2f" % float((row["Price"]))))

    @staticmethod
    def input_new_product_and_price():
        product = input("Product: ")
        price = float(input("Price (Please enter in XX.XX format): "))
        return product, price


# Presentation (Input/Output)  -------------------------------------------- #


# Main Body of Script  ---------------------------------------------------- #
def main():
    # Load data from file into a list of product objects when script starts
    try:
        FileProcessor.read_data_from_file(strFileName, lstOfProducts)
    # Display this error if the file has not been created yet
    except FileNotFoundError:
        print()
        print("File not found")
        print("Please Enter a Product")
    choice = None
    while choice != "3":
        # Show user a menu of options
        IO.print_menu_tasks()
        # Get user's menu option choice
        choice = IO.input_menu_choice()
        # Show user current data in the list of product objects
        if choice == "1" and lstOfProducts == []:
            print("There is no data entered")
            print("Please enter product information")
        elif choice == "1":
            IO.print_current_products_in_list(lstOfProducts)
        # Let user add data to the list of product objects
        elif choice == "2":
            try:
                nproductname, nproductprice = IO.input_new_product_and_price()
                if nproductname.isnumeric():
                    print()
                    print("This is not a valid option please try again")
                    continue
            except ValueError:
                print("This is not a valid number, please re-enter value.")
            else:
                nproduct = Product(nproductname, nproductprice)
                status = nproduct.add_to_list(lstOfProducts)[1]
                print(status)
        # let user save current data to file and exit program
        elif choice == "3":
            status = FileProcessor.save_data_to_file(strFileName, lstOfProducts)
            print(status, "Thank you, Goodbye!")
# Run the program
main()
input("Select Enter to Exit.")
# Main Body of Script  ---------------------------------------------------- #