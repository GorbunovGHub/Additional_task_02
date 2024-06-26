first_field = int(input('Введите число от 3 до 20: '))
if first_field < 3 or first_field > 20:
    first_field = int(input('Вы ввели не то число!: '))


def second_field(first_field):
    password = ''
    for i in range(1, first_field):
        for j in range(i + 1, first_field):
            if first_field % (i + j) == 0:
                password += str(i) + str(j)
    return password


result = second_field(first_field)
print(result)
