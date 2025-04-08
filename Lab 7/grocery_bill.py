prices = {'apple': 50, 'banana': 20, 'milk': 30, 'bread': 40}
quantity = {'apple': 2, 'banana': 5, 'milk': 1, 'bread': 2}

total_bill = sum(prices[item] * quantity[item] for item in prices if item in quantity)
print("Total Bill:", total_bill)