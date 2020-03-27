products = {
    'RB001111': {'name': 'Rayban Sunglasses', 'price': 112.98, 'models': ['black', 'tortoise']},
    'DWC0317': {'name': 'Drone with Cameras', 'price': 72.95, 'models': ['white', 'black']},
    'MTS0540': {'name': 'T-shirt', 'price': 2.95, 'models': ['small', 'medium', 'large']},
    'ECD2989': {'name': 'Echo Dot', 'price': 29.99, 'models': []}
}

print(f"{'ID':<6} {'Name':<17} {'Price':>8} {'Models':}")
print("-" * 60 )

#Loop through each dictionary in the products dictionary
for oneproduct in products.keys():
    # Get the ID of one of the products
    id = oneproduct
    # Get the name of one product
    name = products[oneproduct]['name']
    #Get the unit price of one product and formt with $
    unit_price = '$' + f"{products[oneproduct]['price']:,.2f}"
    #Create and empty string variable named models
    models = ' '
    #Loop through the models list
    for m in products[oneproduct]['models']:
        models += m + ','
    #If the models variable is more than 2 chars in length peel off the last 2 characters
    if len(models) > 2:
        models = models[:-1]
    else:
        models="<none>"
    #Print everything with nice f-string
    print(f"{id:<6} {name:<17} {unit_price:>8} {models}")