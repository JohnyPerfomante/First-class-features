# Реалізувати: def map_custom(func, data): ... Перевірити: map_custom(lambda x: x*x, [1,2,3])
def map_custom(func, data):
    result = []
    for x in data:
        result.append(func(x))
    return result

print(map_custom(lambda x: x*x, [1, 2, 3]))  # [1, 4, 9]