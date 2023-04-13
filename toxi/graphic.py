import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('при 500 м2.xls')
val = df.values[:,1:].T
val[val < 1e-3] = 0.01
plt.figure(figsize=(10,10))
plt.imshow(val, cmap='jet', interpolation = 'bicubic', vmax=0.1)
X, Y = np.meshgrid(range(df.shape[1]), range(df.shape[0]-1))
Z = val
plt.colorbar()
plt.contour(X, Y, Z, sorted([2**(-n) for n in range(10)]))
plt.show()


