# Створити функції: def add_one(x): return x + 1, def double(x): return x * 2, def square(x): return x * x. Створити список: operations = [...] Для числа 10 застосувати всі функції зі списку.
def add_one(x): return x + 1
def double(x): return x * 2
def square(x): return x * x

operations = [add_one, double, square]

x = 10

results = []

for op in operations:
    results.append(op(x))

print(results)  # [11, 20, 100]