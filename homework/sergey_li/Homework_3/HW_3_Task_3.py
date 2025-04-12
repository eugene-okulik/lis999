import math

def calculate_average(num_1, num_2):
    calculation_1 = round(((num_1 + num_2) / 2), 1)
    if num_1 < 0 or num_2 < 0:
        return "Calculation Error. Numbers have to be positive"
    calculation_2 = round(math.sqrt(num_1 * num_2), 1)
    return (f"Среднее арифметическое: {calculation_1} \n"
            f"Среднее геометрическое: {calculation_2}")


result = calculate_average(5, 10)
print(result)
