def calc():
    global new_x

    x = float(input("Введите первое число(положительное): "))

    while x <= 0.0:
        x = float(input("Число должно быть положительным!\nВведите первое число(отрицательное): "))

    y = float(input("Введите второе число(отрицательное): "))

    while y >= 0.0:
        y = float(input("Число должно быть отрицательным!\nВведите второе число(отрицательное): "))

    new_x = x
    new_y = y

    while new_y < -1:
        new_x = new_x * x
        new_y += 1

    else:
        answer = 1 / new_x

        return (f'{x} в степени {y} = {answer}')

print(calc())