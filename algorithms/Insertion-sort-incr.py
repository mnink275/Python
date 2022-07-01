import numpy as np
a = np.array([31, 41, 59, 26, 41, 58])
for j in range (1, a.size):
    key = a[j]
    i = j - 1
    while i >= 0 and a[i] > key:
        a[i+1]=a[i]
        i = i - 1
    a[i+1] = key
print(a)

