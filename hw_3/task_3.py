def my_func():
    arg_1 = float(input("Введите первое число: "))
    arg_2 = float(input("Введите второе число: "))
    arg_3 = float(input("Введите третье число: "))
    list_args = [arg_1, arg_2, arg_3]

    list_args.sort()
    list_args.pop(0)

    return sum(list_args)

print(f'Сумма двух наибольших чисел = {my_func()}')

