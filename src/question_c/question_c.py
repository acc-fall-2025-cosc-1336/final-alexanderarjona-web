#write functions here, don't add input('') statements here!
class Stock:
    def __init__(self, symbol, company_name):
        # Private attributes using double underscore
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name

def test_config():
    return True

def get_stock_list():
    # Create the list of Stock objects based on Table 1
    stock1 = Stock("AAPL", "Apple Inc")
    stock2 = Stock("CAT", "Caterpillar")
    stock3 = Stock("EK", "Eastman Kodak")
    stock4 = Stock("GOOG", "Google")
    stock5 = Stock("MSFT", "Microsoft")
    
    return [stock1, stock2, stock3, stock4, stock5]

def menu():
    print("\n1-Display stock purchase history")
    print("2-Exit")

if __name__ == "__main__":
    # Get the list once as per instructions
    stocks = get_stock_list()

    while True:
        menu()
        option = input("Enter option: ")

        if option == "1":
            print("\nStock Report")
            print(f"{'Company':<15} {'Symbol':<10}")
            for stock in stocks:
                print(f"{stock.get_company_name():<15} {stock.get_symbol():<10}")
        elif option == "2":
            break
        else:
            print("Invalid option")