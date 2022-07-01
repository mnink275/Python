object = []


def foo(x):
    print('foo', x)


def bar(a, b):
    return a + b

def create_object(name):
    object.append('object[' + name + ']')

def print_objects():
    print('Все добавленные объекты: ')
    for obj in object:
        print(obj)



if __name__ == '__main__':
    print('Library executed separately.')
    print("Let's test itself.")
    if bar(2, 2) == 4:
        print('Ok')
    else:
        print('Fail') 