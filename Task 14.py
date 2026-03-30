# Реалізувати систему: engine = { "add": ..., "mul": ..., "square": ... }. Виклик: engine
def add(a, b): return a + b
def mul(a, b): return a * b
def square(x): return x * x

engine = {
    "add": add,
    "mul": mul,
    "square": square
}

# Приклад
print(engine["add"](2, 3))     # 5
print(engine["mul"](2, 3))     # 6
print(engine)     # 16