# Умова: rules = [ lambda x: x + 10, lambda x: x * 2, lambda x: x - 5 ]. Реалізувати: def apply_rules(value, rules): ...
rules = [
    lambda x: x + 10,
    lambda x: x * 2,
    lambda x: x - 5
]

def apply_rules(value, rules):
    result = value
    for rule in rules:
        result = rule(result)
    return result

# Приклад
print(apply_rules(5, rules))  # ((5 + 10) * 2) - 5 = 25