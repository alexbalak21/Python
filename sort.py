def sort_by_age(users):
    filtered = [u for u in users if u["age"] > 30]
    sorted_users = sorted(filtered, key=lambda u: u["age"], reverse=True)
    return [u["name"] for u in sorted_users]


users = [
    {"id": 1, "name": "Alex", "age": 39},
    {"id": 2, "name": "Marie", "age": 28},
    {"id": 3, "name": "Tom", "age": 42},
]


print(sort_by_age(users))