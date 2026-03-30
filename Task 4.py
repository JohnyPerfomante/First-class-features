# Створити: def calculate(operation, a, b): ... Використати додавання, множення, віднімання
def add(a, b): return a + b
def multiply(a, b): return a * b
def subtract(a, b): return a - b

def calculate(operation, a, b):
    return operation(a, b)

print(calculate(add, 5, 3))       # 8
print(calculate(multiply, 5, 3))  # 15
print(calculate(subtract, 5, 3))  # 2