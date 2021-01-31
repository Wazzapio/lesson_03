final_list = []
space = str(' ')
def my_func():
    global numbers
    my_list = []
    numbers = []
    for el in my_string:

        for num in my_list:
            if num is space:
                my_list.remove(num)
                my_list.clear()

        if el is space:
            numbers.append(int(''.join((str(i) for i in my_list))))

        elif el == 'q':
            break

        my_list.append(el)

    numbers.append(int(''.join((str(i) for i in my_list))))
    my_list.clear()

    numbers = list(map(int, numbers))
    numbers = sum(numbers)
    final_list.append(numbers)

    return numbers

my_string = input("Введите несколько чисел через пробел: ")

print(f'Сумма чисел = {my_func()}')

while my_string != 'q':

    my_string = input('Введите еще неколько чисел через пробел. \nЕсли хотите завершить нажмите "q": ')

    if my_string == 'q':
        answer = sum(final_list)
        print(f'Сумма чисел = {answer}')
        break
    else:
        my_func()
        answer = sum(final_list)
        print(f'Сумма всех чисел = {answer}')