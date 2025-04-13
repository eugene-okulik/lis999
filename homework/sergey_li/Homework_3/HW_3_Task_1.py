def calculation(a, b):
    num_sum = a + b
    num_dif_1 = a - b
    num_dif_2 = b - a
    num_mult = a * b
    return (f"Сумма чисел: {num_sum}\n"
            f"Разность чисел: {num_dif_1} и {num_dif_2}\n"
            f"Прозведение чисел: {num_mult}")


result = calculation(5, 10)
print(result)
