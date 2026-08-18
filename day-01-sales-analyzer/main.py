sales = [
    {"product": "Edamame", "quantity": 120, "price": 80},
    {"product": "Mango", "quantity": 50, "price": 120},
    {"product": "Edamame", "quantity": 80, "price": 80},
    {"product": "Banana", "quantity": 150, "price": 35},
    {"product": "Mango", "quantity": 30, "price": 120},
]

total_revenue = 0

for sale in sales:
    total_revenue += sale['price'] * sale['quantity']

print(f"Total Revenue: {total_revenue:,.0f}")

print("Revenue by Product")
print("------------------")
revenue_by_product = {}

for sale in sales:
    product = sale["product"]

    # calculate revenue

    if product not in revenue_by_product:
        revenue_by_product[product] = 0
    
    # aggregate revenue
    revenue_by_product[product] += sale['price'] * sale['quantity']
maxproduct = ""
maxrevenu = 0
for rproductkey, rproductvalue in revenue_by_product.items():
    print(f"{rproductkey} :  {rproductvalue:,.0f}")

largest_key = max(revenue_by_product, key=revenue_by_product.get)
print(f"Top product: {largest_key}")
print(f"Revenue: {revenue_by_product[largest_key]:,.0f}")
