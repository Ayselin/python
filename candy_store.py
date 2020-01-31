candies = {
    'gummy worms': 30,
    'gum': 40,
    'chocolate bars': 50,
    'licorice': 60,
    'lollipops': 20,
    }

message = input("Enter the number of the option you want to check?:  \n1. To check the stock. \n2. How many candies have you sold? \n3. Shipment of new stock.")

if message == '1':
    for candy, amount in candies.items():
        amount = int(amount)
        print(f"{candy}: {amount}")
elif message == '2':
    # for candy, amount in candies.items():
    items = input("Please enter the product you want to check: ")
    sold = input("How many candies have you sold?: ")
    sold = int(sold)
    candies[items] = candies[items] - sold
    print(f"{candies[items]}")
elif message == '3':
    # for candy, amount in candies.items():
    product = input("Please enter the product you want to check: ")
    received = input("How many items were delivered?: ")
    received = int(received)
    candies[product] = candies[product] + received
    print(f"{candies[product]}")
    



    
    

