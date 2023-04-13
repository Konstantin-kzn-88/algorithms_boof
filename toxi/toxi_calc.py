import numpy as np
import pandas as pd
from scipy.interpolate import LinearNDInterpolator
from scipy.spatial import Delaunay
import matplotlib.pyplot as plt
import matplotlib

xls_names = 'при 3000м2.xls', 'при 1000 м2.xls', 'при 500 м2.xls'
area = [3000, 1000, 500]
res = []

for Z, name in zip(area, xls_names):
    WS = pd.read_excel(name, header=None)
    WS_np = np.array(WS)
    X = np.float32(WS_np[1:, 0])
    Y = np.float32(WS_np[0, 1:])
    print(name, np.min(X), np.max(X), np.min(Y), np.max(Y))
    Y, X = np.meshgrid(Y, X)
    V = np.float32(WS_np[1:, 1:])
    Z = np.full_like(V, Z)
    res.append(np.vstack((X.flat, Y.flat, Z.flat, V.flat)).T)
data = np.concatenate(res, axis=0)

values = data[:, 3]

# создание интерполятора, долго, но его можно подсчитать один раз,
# сереализировать (pikle) и сохранить в файл, а в дальнейшем читать его из файла.
tri = Delaunay(data[:, 0:3])
interp = LinearNDInterpolator(tri, values)

point = np.array([[43.5, -7, 500], [43.5, -7, 700]])  # 0.50166
print(interp(point))
# расчет сечений для z=500, 1000, 1500, 2000, 2500 м2
# время расчета для 5 сечений ~ 40 сек
x = np.arange(-5, 49.5, 5)
y = np.arange(-19.5, 19.5, 5)
z = np.arange(500, 3000, 500)
X, Y, Z = np.meshgrid(x, y, z)

V = interp(X, Y, Z)

plt.figure(figsize=(10,10))
plt.imshow(V[1], cmap='jet', interpolation = 'bicubic', vmax=0.1)
plt.show()