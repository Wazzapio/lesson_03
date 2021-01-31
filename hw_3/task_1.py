def calc():
    arg_1 = float(input("Введите первое число: "))
    arg_2 = float(input("Введите второе число: "))

    if arg_1 == 0.0 or arg_2 == 0.0:
        x = "Делить на 0 нельзя!"
        return x

    else:
        answer = arg_1 / arg_2
        return answer

print(calc())