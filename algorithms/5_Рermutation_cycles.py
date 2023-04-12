'''
р.23

1 3 2 -> 2
2 3 4 1  -> 1
'''

perm = [i - 1 for i in map(int, input().split())]

visited = [False] * len(perm)

ans = 0

for start in range(len(perm)):
    if visited[start]:
        continue
    ans += 1
    current = start
    print(f'current_for = {current}')
    while True:
        visited[current] = True
        current = perm[current]
        print(f'current_while = {current}')
        if current == start:
            print('______')
            break

print(ans)

if __name__ == '__main__':
    pass
