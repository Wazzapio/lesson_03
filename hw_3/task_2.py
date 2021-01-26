def info(**kwargs):
    user_info = dict(Имя='name', Фамилия='surname', Год_рождения='year_of_birth', Город='city',
                     Почта='email', Телефон='mobile')
    user_info['Имя'] = input("Введите имя: ")
    user_info['Фамилия'] = input("Введите фамилию: ")
    user_info['Год_рождения'] = input("Введите год рождения: ")
    user_info['Город'] = input("Введите город проживания: ")
    user_info['Почта'] = input("Введите e-mail адрес: ")
    user_info['Телефон'] = input("Введите номер телефона: ")

    list_info = []
    char = []
    pos = 0
    answer = dict()

    for el in user_info.keys():
        char.append(el)

    for el in user_info.values():
        list_info.append(el)

    for el in list_info:
        answer.update({char[pos]: list_info[pos]})
        pos += 1

    return answer

print(f'User info: {info()}')