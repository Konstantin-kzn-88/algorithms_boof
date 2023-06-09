'''
Найти минимальное произведение двух элементов массива
р.25

1 2 3 4 5 -> 2
-1 2 3 4 5  -> -5
'''

a = list(map(int, input('Ввдедите массив чисел: ').split()))
a.sort()

ans_1 = a[0] * a[1] # случай когда все элементы положительны
ans_2 = a[0] * a[-1] # случай когда элементы положительны и отрицательны
ans_3 = a[-1] * a[-2] # случай когда все элементы отрицательны

print(min(ans_1, ans_2, ans_3))


if __name__ == '__main__':
    pass
