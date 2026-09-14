products = [
    {"name": "Laptop", "price": 1200, "stock": 5},
    {"name": "Mouse", "price": 25, "stock": 0},
    {"name": "Keyboard", "price": 45, "stock": 12},
    {"name": "Monitor", "price": 300, "stock": 3},
]


def in_stock(products):
    filtered = [p for p in products if p["stock"] > 0]
    sorted_products = sorted(filtered, key=lambda p : p["price"], reverse=False)
    return [(p["name"], p["price"]) for p in sorted_products]

print(in_stock(products))