import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-10,10,0.1)
plt.plot(x,eval(input()))
plt.grid(True)
plt.show()