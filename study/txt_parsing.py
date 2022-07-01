import os
import codecs

os.chdir(r'C:\Users\Администратор\Desktop')
with codecs.open('message.txt','r','utf_8') as data:
    lst = []
    for line in data:
        lst = lst + list(line.split(' '))