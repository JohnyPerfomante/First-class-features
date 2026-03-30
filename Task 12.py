# Умова: transactions = [100, 200, 300]. Створити: функцію застосування податку, функцію застосування знижки. Передавати їх як параметри
transactions = [100, 200, 300]

def apply_tax(rate):
    return lambda x: x * (1 + rate)

def apply_discount(rate):
    return lambda x: x * (1 - rate)

def process(data, func):
    return [func(x) for x in data]

# Приклад
taxed = process(transactions, apply_tax(0.2))        # +20% податок
discounted = process(transactions, apply_discount(0.1))  # -10% знижка

print(taxed)       # [120.0, 240.0, 360.0]
print(discounted)  # [90.0, 180.0, 270.0]