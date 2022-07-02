import turtle as tr
from random import *


tr.shape("turtle")
tr.speed("fastest")
tr.pencolor('red')


for i in range(1000):
    tr.fd(50*random())
    tr.left(360*random())
    
