import math

def triangle_info(a, b):
    hypotenuse = math.sqrt(a**2 + b**2)
    area = 0.5 * a * b
    return (f"Гипотенуза: {round(hypotenuse, 2)}\n"
            f"Площадь: {round(area, 2)}")


result = triangle_info(5, 10)
print(result)
