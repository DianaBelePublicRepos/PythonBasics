#New lines for strings in sequence

user1 = "Alberto"
user2 = "Babs"
user3 = "Carlos"

output=f"{user1} \n{user2} \n{user3}"
print(output)

#New lines using triple quotes

unit_price = 49.95
quantity = 32
sales_tax_rate = 0.065
subtotal = quantity * unit_price
sales_tax = sales_tax_rate * subtotal
total = subtotal + sales_tax
output = f""" 
Subtotal  =    ${subtotal:,.2f}
Sales Tax =    ${sales_tax:,.2f}
Total:    =    ${total:,.2f}
"""

print(output)

output2 = f""" 
Subtotal  =    ${subtotal:>9,.2f}
Sales Tax =    ${sales_tax:>9,.2f}
Total:    =    ${total:>9,.2f}
"""

print(output2)