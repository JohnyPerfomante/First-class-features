# Завдання 10. Побудова pipeline
# Умова: Реалізувати def pipeline(data, steps): ... Використання: pipeline([1,2,3,4], [lambda x: [i for i in x if i % 2 == 0], lambda x: [i*i for i in x] ] )
def pipeline(data, steps):
    result = data
    for step in steps:
        result = step(result)
    return result

result = pipeline(
    [1, 2, 3, 4],
    [
        lambda x: [i for i in x if i % 2 == 0],
        lambda x: [i * i for i in x]
    ]
)

print(result)  # [4, 16]