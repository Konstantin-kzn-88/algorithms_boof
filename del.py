def search_max(s):
    'Поик наибольшего слова'
    ans = ''
    for i in s:
        if len(i) > len(ans):
            ans = i
    return ans


def search_min(s):
    'Поик наименьшего слова'
    ans = ''
    for i in s:
        if len(i) <= max(map(len, s)):
            ans = i
    return ans


s = tuple(i for i in input().split())
print('max: ', search_max(s))
print('min: ', search_min(s))
