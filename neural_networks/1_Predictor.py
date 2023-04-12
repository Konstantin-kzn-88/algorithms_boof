"Подбор параметра"

data = ((0, 100),  # km
        (0, 62.37))  # milles
# Ошибка
eps = 0.1

while True:
    # Параметр
    c = float(input('Введите корректировочный параметр: '))
    ans1 = c * data[0][0]
    ans2 = c * data[0][1]
    if abs(ans1-data[1][0])<eps and abs(ans2-data[1][1])<eps:
        print(f'Параметр найден c={c}')
        break
    else:
        print('Параметра не достаточно')
        continue


if __name__ == '__main__':
    pass
