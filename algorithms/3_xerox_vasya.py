# этажи на котором раположен ксерокс (k,2k,3k...)
k = int(input('Введите число k = '))
# этаж на котором стоит Вася
n = int(input('Введите число n = '))

# решение книги
i = max(n//k,1)
ans1 = abs(n-k*i)
i+=1
ans2 = abs(n-k*i)
print(min(ans2, ans1))

if __name__ == '__main__':
    pass
