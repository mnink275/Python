#1
# x и y - формальные параметры.
def f(x,y):
    return x + y

#2
# y:int - интерпритация типов (способ оставить комментарий), -> int - должен получиться int.
def f(x:int, y:int) -> int:
    return x + y

#3
# Пишем комментарий для человека.
def f(x:int, y:int) -> int:
    """
    Объясни
    Что делает
    Эта функция
    """
    return x + y