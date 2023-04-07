# Рекурсивно (мой вариант)
# F1 = 0
# F2 = 1
# n = 20
#
# def fib(n:int)->int:
#    if n == 0:
#        return F1
#    elif n == 1:
#        return F2
#    else:
#        return fib(n-1) + fib(n-2)
#
# print(fib(n))

n = int(input('Введите число: '))
f = [0, 1]
while len(f) <= n:
    f.append(f[-1] + f[-2])
print(f[n])

if __name__ == '__main__':
    pass
