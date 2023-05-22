print("Welcome!\n")
print("This program is to apply offers to different items based on thier price and quantity. This program is developed by Adhithya Valsan.")

print("Offers:")
print("1.Buy puchase worth $200 to get flat 10% discount.")
print("2.Buy item in bulk of 10 units to get 5% discount.")
print("3.Buy item in bulk of 20 units to get 10% discount.")
print("4.Buy items in bulk of 30 to get 50% discount.\n")

print("No."+"  "+"Product"+"     "+"Price")
print("1"+" "+"Product A"+"    "+"$20")
print("2"+" "+"Product B"+"    "+"$40")
print("3"+" "+"Product C"+"    "+"$50\n")
print("Gift wrap cost per unit: $1.")
print("Shipping fee: 10 units can be packed in one package, and the shipping fee for each package is $5.\n")

def discount(quantity, total_quantity, total):

    offers = set()
    
    while True:
        
        if quantity > 50:
            print("quantity exceeds the limit!")
            return offers
        
        elif quantity > 15 and total_quantity > 30:
            offers.add(50)

        elif total >=200:
            offers.add(10)

        elif quantity > 10:
                offers.add(5)

        elif quantity > 20:
            offers.add(10)

        return offers

def offers_applied(total, discount_name,discount_rate,cart):

    if discount_rate == 50:
        total = cart * (100 - 50) / 100
        discount_name = "50% off bulk discount"
    
    elif discount_rate == 10:
        total = cart * (100 - 10) / 100
        discount_name = "10% off prooduct discount"

    elif discount_rate == 5:
        total = cart * (100 - 5) / 100
        discount_name = "5% off product discount"
    
    else:
        print("Offers not applicable.")

    return total, discount_name

def gift_wrap(wrap, total_quantity):
    
    wrap = wrap * total_quantity
    print("Gift wrap fee: ",wrap)
    
    return wrap

def shipping(shipping_fee, total_quantity):
   
    shipping_fee = shipping_fee * total_quantity/10
    print("Shipping fee: ",shipping_fee)
    
    return shipping_fee

def total_amount(wrap,shipping_fee,total):
    
    overall_amount = wrap + shipping_fee + total
    print("Total amount to pay: ", overall_amount)
    
    return overall_amount

total_quantity = 0

cart = 0

offers = set()

product = {"Product": ["Product A", "Product B", "Prodcut C"],
           "Price": [20, 40, 50]}

while True:
    print("What would you like to buy?")
    print("input 'q' to checkout")
    purchase = input("Choice: ")

    if purchase == "q" or purchase == "Q":
        break

    purchase = int(purchase)

    if purchase == 0:
        print("Come again... Bye!")
        exit()

    elif purchase == 1:
        print(product["Product"][0])
        print("Price: ", product["Price"][0])
        n = 0
        quantity = input("quantity: ")
        try:
            quantity = int(quantity)
        except ValueError:
            print("Invalid value")
            continue
        add_to_cart = str(input("Add " + str(quantity) + " to cart, Y/N?\n"))

        if add_to_cart == 'Y' or add_to_cart == 'y':
            total_quantity += quantity
            total = quantity*int(product["Price"][n])
            cart += total
            offers = discount(quantity, total_quantity, total)
            print("Total amount: ",cart)
            print("Total items: ", total_quantity)
        
        elif add_to_cart == 'N' or add_to_cart == 'n':
            print("Taking you back to main page.")

        else: 
            print("invalid Choice")
    
    elif purchase == 2:
        print(product["Product"][1])
        print("Price: ", product["Price"][1])
        n = 1
        quantity = input("quantity: ")
        try:
            quantity = int(quantity)
        except ValueError:
            print("Invalid value")
            continue
            
        add_to_cart = str(input("Add " + str(quantity) + " to cart, Y/N?\n"))

        if add_to_cart == 'Y' or add_to_cart == 'y':
            total_quantity += quantity
            total = quantity*int(product["Price"][n])
            cart += total
            offers = discount(quantity, total_quantity, total)
            print("Total amount: ",cart)
            print("Total items: ", total_quantity)
        
        elif add_to_cart == 'N' or add_to_cart == 'n':
            print("Taking you back to main page.")

        else: 
            print("invalid Choice")
    
    elif purchase == 3:
        print(product["Product"][2])
        print("Price: ", product["Price"][2])
        n = 2
        quantity = input("quantity: ")
        try:
            quantity = int(quantity)
        except ValueError:
            print("Invalid value")
            continue
        add_to_cart = str(input("Add " + str(quantity) + " to cart, Y/N?\n"))

        if add_to_cart == 'Y' or add_to_cart == 'y':
            total_quantity += quantity
            total = quantity*int(product["Price"][n])
            cart += total
            offers = discount(quantity, total_quantity, total)
            print("Total amount: ",cart)
            print("Total items: ", total_quantity)
        
        elif add_to_cart == 'N' or add_to_cart == 'n':
            print("Taking you back to main page.")

        else: 
            print("invalid Choice")
        
    else:
        print("Product is not listed")

if offers:
    discount_rate=max(offers)
    print(discount_rate)
    discount_name = None
    total,discount_name = offers_applied(total, discount_name, discount_rate,cart)
    
    if discount_name:
        print("Offers applied: ", discount_name)
        print("Amount: ", total)
    
    wrap = 1
    wrap = gift_wrap(wrap, total_quantity)

    shipping_fee = 5
    shipping_fee = shipping(shipping_fee,total_quantity)

    overall_amount = total_amount(wrap,shipping_fee,total)
    print("Thank You for shopping, Bye!")

    



