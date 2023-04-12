'''
p.17

7 -> 13
8 -> 21
'''

n = int(input('Введите число: '))
f = [0, 1]
while len(f) <= n:
    f.append(f[-1] + f[-2])
print(f[n])

if __name__ == '__main__':
    pass
