# Реалізувати: def apply(func, x): ... Використати square, double.
def square(x): return x * x
def double(x): return x * 2

def apply(func, x):
    return func(x)

print(apply(square, 5))  # 25
print(apply(double, 5))  # 10