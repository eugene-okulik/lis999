def re_calc(func):
    def wrapper(first, second, operation=None):
        if first < 0 or second < 0:
            operation = "*"
        elif first == second:
            operation = "+"
        elif first > second:
            operation = "-"
        else:
            operation = "/"
        return func(first, second, operation)

    return wrapper


@re_calc
def calc(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    elif operation == "*":
        return first * second
    elif operation == "/":
        if second == 0:
            return "Error: Division by zero"
        return first / second
    else:
        return "Invalid operation"


num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

result = calc(num1, num2)
print(result)
