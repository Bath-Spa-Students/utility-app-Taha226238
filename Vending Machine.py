class VendingMachine:
    def __init__(self):
        # Initialize menus with items, prices, and quantities
        self.snacks_menu = {"Chips": 1.50, "Cookies": 2.00, "Lays": 1.75, "Potato chips": 1.25, "Nuts": 2.50, "Pies": 1.80, "Corn": 2.25}
        self.drinks_menu = {"Soda": 1.25, "Water": 1.00, "Juice": 2.00, "Milk shake": 1.75, "Coffee": 1.50, "Smoothie": 2.50, "Mocha": 1.80}
        self.chocolates_menu = {"Mars": 2.00, "Snicker": 2.25, "Areo": 2.50, "Dairy milk": 2.75, "Cadbury": 3.00, "Hershey": 2.80, "Nestle": 2.20}
        
        # Initialize quantities for each item
        self.snacks_quantity = {item: 10 for item in self.snacks_menu}
        self.drinks_quantity = {item: 10 for item in self.drinks_menu}
        self.chocolates_quantity = {item: 10 for item in self.chocolates_menu}
        
        # Initialize total cost
        self.total_cost = 0.0

    def display_menu(self, menu, menu_name):
        print(f"\n{menu_name}")
        print("------------------------")
        for item, price in menu.items():
            print(f"{item}: ${price:.2f}")
        print("------------------------")

    def make_selection(self, menu, quantity_menu):
        selection = input("\nEnter item name (or 'done' to finish): ").capitalize()

        while selection != 'Done':
            if selection in menu:
                quantity = int(input(f"How many {selection}s would you like? (Available: {quantity_menu[selection]}): "))
                if quantity <= quantity_menu[selection]:
                    self.total_cost += menu[selection] * quantity
                    quantity_menu[selection] -= quantity
                    print(f"\nAdded {quantity} {selection}(s) to your cart.")
                else:
                    print(f"Sorry, not enough {selection}s in stock. Available: {quantity_menu[selection]}")
            else:
                print("Invalid selection. Please choose a valid item.")

            selection = input("\nEnter item name (or 'done' to finish): ").capitalize()

    def start_purchase(self):
        print("")
        print("\033[93m██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░  ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗")
        print("\033[93m██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░  ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝")
        print("\033[93m╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░  ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░")
        print("\033[93m░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗  ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░")
        print("\033[93m░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝  ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗")
        print("░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝")
        print("")
        print("")
        print("\033[91m█▀ █▄░█ ▄▀█ █▀▀ █▄▀ █▀")
        print("\033[91m▄█ █░▀█ █▀█ █▄▄ █░█ ▄█")
        print("")
        self.display_menu(self.snacks_menu, "Pick your item")
        
        self.make_selection(self.snacks_menu, self.snacks_quantity)
        print("")
        print("\033[92m█▀▄ █▀█ █ █▄░█ █▄▀ █▀")
        print("\033[92m█▄▀ █▀▄ █ █░▀█ █░█ ▄█")
        print("")
        self.display_menu(self.drinks_menu, "Pick your item")
        self.make_selection(self.drinks_menu, self.drinks_quantity)
        print("")
        print("\033[94m█▀▀ █░█ █▀█ █▀▀ █▀█ █░░ ▄▀█ ▀█▀ █▀▀ ▀ █▀")
        print("\033[94m█▄▄ █▀█ █▄█ █▄▄ █▄█ █▄▄ █▀█ ░█░ ██▄ ░ ▄█")
        print("")
        self.display_menu(self.chocolates_menu, "Pick your item")
        self.make_selection(self.chocolates_menu, self.chocolates_quantity)
        
        while True:
            print("")
            print("\033[93m██████████████████████████████████████████████████████████████████████████████████████")
            print("\033[93m█▄─▄▄─█▄─▀█▄─▄█─▄─▄─█▄─▄▄─█▄─▄▄▀███─▄─▄─█─█─█▄─▄▄─███▄─▀█▀─▄█─▄▄─█▄─▀█▄─▄█▄─▄▄─█▄─█─▄█")
            print("\033[93m██─▄█▀██─█▄▀─████─████─▄█▀██─▄─▄█████─███─▄─██─▄█▀████─█▄█─██─██─██─█▄▀─███─▄█▀██▄─▄██")
            print("\033[93m▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀▀▄▄▄▀▀▄▀▄▀▄▄▄▄▄▀▀▀▄▄▄▀▄▄▄▀▄▄▄▄▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀")
            print("")
            try:
                print()
                amount_paid = float(input("\033[93m\nEnter the amount of money you want to insert: $"))
                break
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

        change = amount_paid - self.total_cost
        if change < 0:
            print(f"\nInsufficient funds. You need an additional ${abs(change):.2f}.")
        else:
            print("")
            print("\033[39m█████████████████████████████████████████")
            print("\033[39m█▄─▄▄▀█▄─▄▄─█─▄▄▄─█▄─▄▄─█▄─▄█▄─▄▄─█─▄─▄─█")
            print("\033[39m██─▄─▄██─▄█▀█─███▀██─▄█▀██─███─▄▄▄███─███")
            print("\033[39m▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▀▀▀▀▄▄▄▀▀") 
            print("")

            print(f"Total Cost: ${self.total_cost:.2f}")
            print(f"Amount Paid: ${amount_paid:.2f}")
            print(f"Change: ${change:.2f}")

        print(f"\nYour total cost is: ${self.total_cost:.2f}")
        print("")
        print("")
        print("\033[91m▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█   █▀▀ █▀█ █▀█   █░█ █▀ █ █▄░█ █▀▀   ▀█▀ █░█ █▀▀   █░█ █▀▀ █▄░█ █▀▄ █ █▄░█ █▀▀")
        print("\033[91m░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█   █▀░ █▄█ █▀▄   █▄█ ▄█ █ █░▀█ █▄█   ░█░ █▀█ ██▄   ▀▄▀ ██▄ █░▀█ █▄▀ █ █░▀█ █▄█")
        print("")
        print("\033[91m█▀▄▀█ ▄▀█ █▀▀ █░█ █ █▄░█ █▀▀ █")
        print("\033[91m█░▀░█ █▀█ █▄▄ █▀█ █ █░▀█ ██▄ ▄")
        print("")
# Create an instance of the VendingMachine class and start the purchase process
vending_machine = VendingMachine()
vending_machine.start_purchase()     