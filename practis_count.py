#Пользователь вводит число n.
# Нужно пройти все числа от 1 до n включительно и для каждого сделать следующее:
# Если число кратно 3, добавить его к сумме sum3 и увеличить счётчик count3 на 1
# Если число кратно 5, добавить его к сумме sum5 и увеличить счётчик count5 на 1
# Если число кратно и 3, и 5, добавить его к отдельной сумме sum15 и увеличить отдельный счётчик count15 на 1
# В конце вывести: sum3 и count3, sum5 и count5, sum15 и count15


# n = int(input(">>>"))
# count3 = 0
# count5 = 0
# count15 = 0
# sum3 = 0
# sum5 = 0
# sum15 = 0
# for i in range(1, n+1):
#     if i % 3 == 0 and i % 5 ==0:
#         sum15 += i
#         count15 += 1
#     if i % 3 == 0:
#         sum3 += i
#         count3 += 1
#     if i % 5 == 0:
#         sum5 += i
#         count5 +=1
# print("sum3=", sum3, "count3=", count3)
# print("sum5=", sum5, "count5=", count5)
# print("sum15=", sum15, "count15=", count15)

#Пользователь вводит одну строку.
#Нужно пройти по каждому символу строки и посчитать:
# сколько букв, сколько цифр, сколько пробелов
# сколько остальных символов (знаки, спецсимволы и т.п.)
# В конце вывести 4 числа:

# text = input()
# count_num = 0
# count_let = 0
# count_sing = 0
# count_spase = 0
# for ch in text:
#     if ch.isalpha():
#         count_let += 1
#     elif ch.isdigit():
#         count_num += 1
#     elif ch == " ":
#         count_spase += 1
#     else:
#         count_sing +=1
# print(count_let, count_num, count_spase, count_sing)

# Пользователь вводит строку
# Строка состоит из слов, разделённых пробелами
# Нужно пройти по всем словам и:
# посчитать, сколько слов: длина меньше 4, длина от 4 до 7 включительно
# длина больше 7, В конце вывести три числа через пробел:

# text = input()
# count_1 = count_2 = count_3 = 0
# for word in text.split():
#     if len(word) > 3 and len(word) < 8:
#         count_1 += 1
#     elif len(word) < 4:
#         count_2 += 1
#     else:
#         count_3 += 1
# print(count_1, count_2, count_3)

#Пользователь вводит строку. Нужно пройтись по строке в цикле for
# Для каждого символа: если это буква → вывести letter
# если это цифра → вывести digit, если это пробел → вывести space
# иначе → вывести symbol
# Выводить по одному слову на строку, в том порядке, как символы идут в строке.

text = input()
for ch in text:
    if ch.isalpha():
        print("letter")
    elif ch.isdigit():
        print("digit")
    elif ch == " ":
        print("space")
    else:
        print("symbol")