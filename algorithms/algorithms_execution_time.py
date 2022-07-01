import matplotlib.pyplot as plt
import numpy as np
from algorithms_test import main_sort
import timeit


def main():
    elms = int(1e4)
    T = np.zeros(elms)
    N = np.zeros(elms)
    numb = 1
    for i in range(0,elms):
        N[i] = numb
        numb = numb + 1
        t0 = 1e3*timeit.default_timer()
        main_sort(N[i])
       # payload()
        T[i] = 1e3*timeit.default_timer() - t0

        if i % 1000 == 0:
            print(f'In process...{i}')
    plt.plot(N,T)
    plt.show()

def payload():
    k = 1
    for i in range(0,int(1e4)):
        k = k + 1


if __name__ == '__main__':
    main()