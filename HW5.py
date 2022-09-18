# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# print(' '.join(filter(lambda x: not 'абв' in x, 'Эта задача неабв самая сложнаяабв простая из абв всего абвинтернета домашнего задания.'.split())))

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Человек против человека

# from random import randint

# def take_k (name):
#     x = int(input(f"{name}, введите количество конфет от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, неверно число. Введите количество конфет от 1 до 28: "))
#     return x

# def p_print(value):
#     print(f"На столе осталось {value} конфет.")

# player1 = input("Первый игрок: ")
# player2 = input("Второй игрок: ")
# value = int(input("Количество конфет на столе: ")) # по условию 2021, но добавила это, чтобы быстрее проверять работоспособность.
# flag = randint(0,2)
# if flag:
#     print(f"Первый ход у игрока {player1}")
# else:
#     print(f"Первый ход у игрока {player2}")

# count1 = 0 
# count2 = 0

# while value > 28:
#     if flag:
#         k = take_k (player1)
#         count1 += k
#         value -= k
#         flag = False
#         p_print(value)
#     else:
#         k = take_k (player2)
#         count2 += k
#         value -= k
#         flag = True
#         p_print(value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")


# Человек против бота

# from random import randint
# from re import X

# def take_p (name):
#     x = int(input(f"{name}, введите количество конфет от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, неверно число. Введите количество конфет от 1 до 28: "))
#     return x

# def take_b (x):
#     x = randint(1,29)
#     return x

# def p_print(name, k, valuelue):
#     print(f"{name} взял {k} конфет. На столе осталось {value} конфет.")

# player1 = input("Первый игрок: ")
# player2 = 'bot'
# print(f"Второй игрок {player2}")
# value = int(input("Количество конфет на столе: ")) # по условию 2021, но добавила это, чтобы быстрее проверять работоспособность.
# flag = randint(0,2)
# if flag:
#     print(f"Первый ход у игрока {player1}")
# else:
#     print(f"Первый ход у игрока {player2}")

# count1 = 0 
# count2 = 0

# while value > 28:
#     if flag:
#         k = take_p (player1)
#         count1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, value)
#     else:
#         k = take_b (player2)
#         count2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")


# Человек против бота с интеллектом

from random import randint
from re import X

def take_p (name):
    x = int(input(f"{name}, введите количество конфет от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, неверно число. Введите количество конфет от 1 до 28: "))
    return x

def take_b (x):
    x = value % 29
    return x

def p_print(name, k, valuelue):
    print(f"{name} взял {k} конфет. На столе осталось {value} конфет.")

player1 = input("Первый игрок: ")
player2 = 'bot'
print(f"Второй игрок {player2}")
value = int(input("Количество конфет на столе: ")) # по условию 2021, но добавила это, чтобы быстрее проверять работоспособность.
flag = randint(0,2)
if flag:
    print(f"Первый ход у игрока {player1}")
else:
    print(f"Первый ход у игрока {player2}")

count1 = 0 
count2 = 0

while value > 28:
    if flag:
        k = take_p (player1)
        count1 += k
        value -= k
        flag = False
        p_print(player1, k, value)
    else:
        k = take_b (player2)
        count2 += k
        value -= k
        flag = True
        p_print(player2, k, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")