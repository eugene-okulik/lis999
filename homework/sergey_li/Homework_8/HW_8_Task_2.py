import sys

sys.set_int_max_str_digits(1000000)


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


targets = [5, 200, 1000, 100000]
gen = fibonacci_generator()
results = {}

for i in range(1, max(targets) + 1):
    num = next(gen)
    if i in targets:
        results[i] = num

for index in targets:
    print(f"{index}-е число фибоначчи: {results[index]}")
