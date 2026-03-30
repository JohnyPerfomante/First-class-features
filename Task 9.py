# Завдання 9. Динамічний вибір алгоритму
# Умова: def sort_asc(data): ... def sort_desc(data): ... Обрати функцію через словник: strategies = {...}
def sort_asc(data):
    return sorted(data)

def sort_desc(data):
    return sorted(data, reverse=True)

strategies = {
    "asc": sort_asc,
    "desc": sort_desc
}

data = [5, 2, 9, 1]

print(strategies["asc"](data))   # [1, 2, 5, 9]
print(strategies["desc"](data))  # [9, 5, 2, 1]