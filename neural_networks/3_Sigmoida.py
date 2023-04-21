# importing the required libraries
from math import exp
from matplotlib import pyplot as plt


def sigmoida(x: int):
    return 1 / (1 + exp(-x))


x = [i for i in range(-10, 10, 1)]
y = [sigmoida(i) for i in x]

plt.plot(x, y)
plt.show()
plt.close()

if __name__ == '__main__':
    pass
