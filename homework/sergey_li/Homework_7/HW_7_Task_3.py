def process(some_str):
    print(int(some_str.split(":")[-1]) + 10)


strings = [
    "результат операции: 42",
    "результат операции: 54",
    "результат работы программы: 209",
    "результат: 2",
]

for sentence in strings:
    process(sentence)
