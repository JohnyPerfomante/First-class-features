# Завдання 8. Таблиця операцій
# Умова: operations = { "+": ..., "-": ..., "*": ..., "/": ... }. Виклик: operations["+"](2,3)
operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

print(operations["+"](2, 3))  # 5