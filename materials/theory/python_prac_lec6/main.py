
import library as lib   


def printer():
    print(x)

def modifier(): 
    # Модифицирует глобальную переменную "x".
    global x # Указываем, что нужно поменять 'глобальную' переменную.
    x += 10
    print(x)
#printer() - выведет ошибку, т.к. не нашёл х.

print('Main module', __name__)
lib.foo(3)
lib.foo(4)
x = lib.bar(1, 5)
print(x)

lib.create_object('Круг1')
lib.create_object('Круг2')
lib.create_object('Круг3')
lib.print_objects()

#printer() - выведет 6, т.к. дотянулся до глобальной переменной.

for obj in lib.object:
    if 'Круг1' in obj:
        print('Найден круг 1!')
lib.object.pop()
lib.print_objects()

x = 10
modifier()