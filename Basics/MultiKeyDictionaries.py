employee = {
    'name': 'Haru Tanaka',
    'year_hired': 2005,
    'dob': '11/23/1987',
    'has_laptop': False
}

product = {
    'name': "Ray-Ban Wayfarer Sunglasses",
    'unit_price': 112.99,
    'taxable': True,
    "in_stock": 10,
    'models': ['Black', 'Tortoise']
}

# Populating a new dictionary with data from another dict and update one of the values
DWC001 = dict.fromkeys(product.keys())
print(DWC001)
DWC001['taxable'] = False
print(DWC001)

