import random


def compensation(salary, bonus):
    if bonus:
        salary += random.randint(0, 5000)
    return f"${salary}"


salary_input = int(input("Enter your salary: "))
bonus_flag = random.choice([True, False])
result = compensation(salary_input, bonus_flag)
print(f"{salary_input}, {bonus_flag} - {result}")
