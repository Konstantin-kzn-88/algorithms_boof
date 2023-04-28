n = int(input("Введите количество друзей: "))
friends = []

for i in range(n):
    friends.append({'Name': input('Имя:'), 'Age': int(input('Возраст:'))})
    print('*'*20)

min_age = min([int(list(i.values())[-1]) for i in friends])

for i in friends:
    name, age = i.items()
    if age[-1] == min_age:
        print(name[-1])

if __name__ == '__main__':
    pass
