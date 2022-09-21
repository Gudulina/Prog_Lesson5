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

# ---Человек против человека---

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


# ---Человек против бота---

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


# ---Человек против бота "с интеллектом"---

# from random import randint
# from re import X

# def take_p (name):
#     x = int(input(f"{name}, введите количество конфет от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, неверно число. Введите количество конфет от 1 до 28: "))
#     return x

# def take_b (x):
#     x = value % 29
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




# 3. Создайте программу для игры в ""Крестики-нолики"".

# field = list (range(1,10))

# def draw_field(field):
#     print ("-" * 13)
#     for i in range(3):
#         print ("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
#         print ("-" * 13)

# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Введите число от 1 до 9, куда поставить " + player_token + ": ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print ("Некорректный ввод. Введите число от 1 до 9.")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(field[player_answer-1]) not in "XO"):
#                 field[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print ("Клетка занята.")
#         else:
#             print ("Введите число от 1 до 9.")

# def who_win(field):
#     win_variants = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for each in win_variants:
#         if field[each[0]] == field[each[1]] == field[each[2]]:
#             return field[each[0]]            
#     return False

# def game (field):
#     draw_field(field)
#     counter = 0
#     win = False
#     while not win:        
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
        
#         if counter > 4:            
#             who_win(field)
#             if who_win:
#                 draw_field(field)
#                 print ("Вы победили!")
#                 win = True
#                 break
#         if counter == 9:
#             draw_field(field)
#             print ("Ничья!")
#             break
#         else:
#             draw_field(field)
# game (field)



# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Сжатие данных
def rle_compression(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char: 
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else: 
        encoding += str(count) + prev_char
        return encoding

# Восстановление данных

def recovery(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

a = rle_compression('eeeeeeeeellllllllllllllllleeeeeeeeennnnnnaaaaaaaaa')
print(a)

b = recovery('9e17l9e6n9a')
print(b)