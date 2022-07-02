# http://cs.mipt.ru/python/lessons/lab1.html
import numpy as np


def y(x):
    # Зачем флотить x?
    x = float(x)
    y = np.log(np.exp(1/(np.sin(x) + 1)) / (5/4 + 1/(x**1 * 5)))/np.log(1 + x**x)
    return y


A = [1, 10, 100]
print(list(map(y, A)))
