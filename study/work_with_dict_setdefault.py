d = {}
str1 = 'прием Хьюстон Хьюстон как слышно прием меня слышно прием хьюстон Хьюстон у нас проблема'.split()
for a in str1:
    d[a] = d.setdefault(a,0) + 1
    print(d[a], end = ' ')
