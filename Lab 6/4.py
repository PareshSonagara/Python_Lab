food_prices = [("Pizza", 9),("Burger", 5),("Pasta", 7),("Salad", 4),("Sushi", 13)]

n = len(food_prices)
for i in range(n):
    for j in range(0, n - i - 1):
        if food_prices[j][1] < food_prices[j + 1][1]:
            food_prices[j], food_prices[j + 1] = food_prices[j + 1], food_prices[j]

print(food_prices)