
import matplotlib.pyplot as plt
import numpy as np


with plt.xkcd():
    plt.pie([70, 10, 10, 10], labels=('В комментариях', 'В Ираке', 'В Сирии', 'В Афганистане'))
    plt.title('Где ведутся самые ожесточенные бои')
    plt.show()
