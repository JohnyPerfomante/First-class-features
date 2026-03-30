# Створити функцію: def make_adder(n): ... Використати: add10 = make_adder(10), add10(5). Пояснити: що таке closure.
def make_adder(n):
    def adder(x):
        return x + n
    return adder

add10 = make_adder(10)
print(add10(5))  # 15

# Closure — це функція, яка створюється всередині іншої функції, використовує змінні з зовнішньої функції, зберігає ці змінні навіть після завершення зовнішньої функції.