import numpy as np


def merge_sort(A,p,r):
    if p < r:
        q = int((p + r) / 2)
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
    return A

def merge(A,p,q,r):
    n1 = q - p + 1
    n2 = r - q
    L = np.zeros(n1+1)
    R = np.zeros(n2+1)
    for i in range(0,n1):
        L[i] = A[p + i]
    for j in range(0,n2):
        R[j] = A[q + j + 1]
    L[-1] = 1e4
    R[-1] = 1e4
    i = 0
    j = 0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A

def main_sort():
    A = abs((100*np.random.randn(100))).astype(int)
    print('Array before sorting: A = ', A)
    p = 0
    r = len(A) - 1
    print('Array after sorting: A = ', merge_sort(A,p,r))

if __name__ == '__main__':
    main_sort()