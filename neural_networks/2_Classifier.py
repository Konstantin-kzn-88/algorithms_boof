# Простой классификатор
import matplotlib.pyplot as plt

data = [
    (3, 1, 'Божья коровка'),
    (1, 3, 'Гусенница')
]

width = [i[0] for i in data]  # ширина
length = [i[1] for i in data]  # длина
x = (0, 1, 2, 3, 4)

# plt.scatter(width, length)
# plt.ylabel('Длина')
# plt.xlabel('Ширина')
# plt.show()
# plt.close()

## Первая визуализация классификатора для линии y=0.25x
# j=0.25 # коэффициен наклона прямой
# plt.scatter(width, length)
# plt.plot(x, [i * j for i in x], color = 'g')
# plt.ylabel('Длина')
# plt.xlabel('Ширина')
# plt.show()
# plt.close()

# # Поиск ошибки
# j = 0.25  # коэффициен наклона прямой
# y = j * data[0][0]  # значение функции y=0.25x для х=3 (ширина первого экз.)
# # т.к. оно слишком низко 0,75 != 1, подберем целевое значение 1.1 чуть выше искомой 1
# eps = 1.1 - y
# print(f'eps={eps}')
#
# # t = (j+delta_j)*x
# # y = j*x
# # t-y = (j+delta_j)*x - j*x
# # т.к. eps = t-y, eps = delta_j * x
# # откуда delta_j = eps/x
#
# delta_j = eps / data[0][0]
# print(f'delta_j=delta_j={delta_j}')
#
# j = delta_j + j  # коэффициен наклона прямой
# plt.scatter(width, length)
# plt.plot(x, [i * j for i in x], color='g')
# plt.ylabel('Длина')
# plt.xlabel('Ширина')
# plt.show()
# plt.close()

# Обучение классификатора
l = 0.5 # скорость обучения
j = 0.25  # коэффициент наклона прямой
y = j * data[0][0]  # значение функции y=0.25x для х=3 (ширина первого экз.)
# т.к. оно слишком низко 0,75 != 1, подберем целевое значение 1.1 чуть выше искомой 1
eps = 1.1 - y
print(f'eps={eps}')

#  delta_j = l*(eps/x)

delta_j = l*(eps / data[0][0])
print(f'delta_j={delta_j}')

j = delta_j + j  # коэффициен наклона прямой
plt.scatter(width, length)
plt.plot(x, [i * j for i in x], color='g')
plt.ylabel('Длина')
plt.xlabel('Ширина')
plt.show()
plt.close()

# Обучение по второму набору данных
j_2 = j  # коэффициент наклона прямой (коэф. с учтом того что один набор прошел)
y = j * data[1][0]  # значение функции y=0.25x для х=1 (ширина второго экз.)
eps = 2.9 - y
print(f'eps={eps}')

#  delta_j = l*(eps/x)

delta_j = l*(eps / data[1][0])
print(f'delta_j={delta_j}')

j = delta_j + j  # коэффициен наклона прямой
plt.scatter(width, length)
plt.plot(x, [i * j for i in x], color='r')
plt.ylabel('Длина')
plt.xlabel('Ширина')
plt.show()
plt.close()

if __name__ == '__main__':
    pass
