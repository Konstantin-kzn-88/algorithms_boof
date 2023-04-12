'''
p.18

1 2
2 1 -> 2

1 1
11 21 -> 30
'''

start_point = (int(input('x_start = ')), int(input('y_start = ')))
end_point = (int(input('x_end = ')), int(input('y_end = ')))

dx = abs(start_point[0] - end_point[0])
dy = abs(start_point[1] - end_point[1])

print(dx + dy)

if __name__ == '__main__':
    pass
