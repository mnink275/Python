values = input('Введите числа через запятую: ')
list_with_str = values.split(',')
a = map(int,list_with_str)
lst = list(a)
tpl = tuple(lst)
print('List: ', lst)
print('Tuple: ', tpl)
