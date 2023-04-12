from collections import *
'''
1 3 2 -> OK
2 3 4 -> BAD
'''
a = list(map(int, input().split()))
cnt = Counter(a)
ans = (max(a) == len(a) and max(cnt.values()) == 1)
print('OK' if ans else 'BAD')