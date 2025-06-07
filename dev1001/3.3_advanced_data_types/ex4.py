# Dictionaries Exercise

product_info = {
    "name": "Laptop",
    "price": 1200.00,
    "stock": 15
}

# 1. The price increased by $50. Update it.
# 2. Add a new key-value pair: "brand": "TechCo".
# 3. Check if "warranty_years" is a key. If not, add it with a value of 2.
#           Use .get() for checking initially.
# 4. Someone bought a laptop. Decrease stock by 1.
# 5. Change the name to "ASUS Laptop" **without** using [] or =.
# 6. Print all key-value pairs neatly.

product_info["price"] = 1250.00
print(product_info["price"])
product_info["brand"] = "TechCo"
print(product_info)
print("warranty" in product_info)
print({product_info.get("warranty")})
product_info["warranty"] = 2
print(product_info)
product_info["stock"] = 14
print(product_info)
product_info.update(name="ASUS Laptop")
print(product_info)

for key, value in product_info.items():
    print(f"{key}: {value}")
