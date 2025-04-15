result_1 = "результат операции: 42"
result_2 = "результат операции: 514"
result_3 = "результат работы программы: 9"


def change_result(result):
    words = result.split(" ")
    return int(words[-1]) + 10


print(change_result(result_1))
print(change_result(result_2))
print(change_result(result_3))
