lines = [
    "результат операции: 42",
    "результат операции: 514",
    "результат работы программы: 9",
]

for sentence in lines:
    find_index = sentence.index(":")
    number = int(sentence[find_index + 1:].strip())
    print(number + 10)
