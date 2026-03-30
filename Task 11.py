# Умова: numbers = [1,2,3,4,5]. Побудувати функцію: def process(data, func): ...
numbers = [1, 2, 3, 4, 5]

def process(data, func):
    return [func(x) for x in data]

# Приклади
print(process(numbers, lambda x: x * 2))   # [2, 4, 6, 8, 10]
print(process(numbers, lambda x: x ** 2))  # [1, 4, 9, 16, 25]