# expense = {"amount": 500, "category": "food", "description": "amala"}
# print(expense)

expenses = [
    {"amount": 600, "category": "food", "description": "rice"},
    {"amount": 1500, "category": "transport", "description": "car"},
    {"amount": 400, "category": "food", "description": "amala"},
    # {"amount": 1000, "category": "food", "description": "bread"}
]

total = 0
food_total = 0
for expense in expenses:
    total += expense["amount"]
    if expense["category"] == "food":
        food_total += expense["amount"]
category_totals = {
    "food": 600
}
category_totals["food"] += 400
print(category_totals)
print(f"{total}\n{food_total}")
