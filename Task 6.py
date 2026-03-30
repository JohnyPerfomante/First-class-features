# Реалізувати: def multiplier(n): ... Використати: times3 = multiplier(3), times3(5)
def multiplier(n):
    def inner(x):
        return x * n
    return inner

times3 = multiplier(3)
print(times3(5))  # 15