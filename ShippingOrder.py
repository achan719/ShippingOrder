#%%
order = 0
shipping = 0

destination = input("Shipping Destination\nUSA or Canada?")

if destination.upper() == "USA" or destination.upper() == "CANADA":
    order = int(input("Enter Order Amount: "))
    if order > 0 and order < 10000:
        if destination == "USA": 
            if order < 50: 
                shipping = 6
            elif order < 100:
                shipping = 9
            elif order < 150:
                shipping = 12
            else: 
                shipping = 0
        else: 
            if order < 50: 
                shipping = 8
            elif order < 100:
                shipping = 12
            elif order < 150:
                shipping = 15
            else: 
                shipping = 0
        print("Order: $", format(order,'.2f'), "\nShipping: $", format(shipping, '.2f'))
        print("Destination: ", destination.upper(), "\nTotal: $", format(order+shipping, '.2f'))
    else:
        print("Error! Invalid Entry")
else: 
    print("ERROR - Invalid Shipping Destination")

# %%
