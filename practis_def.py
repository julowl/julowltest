# Напиши функцию print_hi
# Она ничего не принимает
# Она печатает строку

# def print_hi():
#     print("Hi!")
# print_hi()

# Напиши функцию print_word
# Она принимает одно слово
# Печатает: "слово"

# def print_word(word: str):
#     print("You entered:", word)
#
# print_word("cat")
# print_word("dog")

# функция add_one принимает число
# возвращает число + 1

# def add_one(num: int):
#     return num + 1
# print(add_one(3))
# print(add_one(10))

#Функция принимает число и возвращает его удвоенным

# def add_num(num: int):
#     return num * num
# print(add_num(2))
# print(add_num(3))

#Функция принимает число и:
# если число чётное → возвращает "even"
# если нечётное → возвращает "odd"

# def is_chet(num:int):
#     if num % 2 ==0:
#         return "even"
#     else:
#         return "odd"
# print(is_chet(2))
# print(is_chet(5))

# Функция принимает число n и:
# считает, сколько чисел от 1 до n чётные
# возвращает это количество

# def count_chet(num: int):
#     count = 0
#     for i in range(2,num):
#         if i % 2 == 0:
#             count += 1
#     return count
# print(count_chet(4))
# print(count_chet(11))

# Написать функцию, которая: принимает число n
# считает сколько чисел от 1 до n кратны 3
# возвращает это количество

# def count_num(num: int):
#     count = 0
#     for i in range(1, num):
#         if i % 3 == 0:
#             count += 1
#     return count
# print(count_num(10))
# print(count_num(7))

# Написать функцию, которая: принимает число n
# возвращает сумму всех чётных чисел от 1 до n

# def sum_chet(num: int):
#     summ = 0
#     for i in range(1, num+1):
#         if i % 2 == 0:
#             summ += i
#     return summ
# print(sum_chet(4))
# print(sum_chet(10))

# Функция принимает число n и возвращает сразу два значения:
# сумму чётных чисел, количество чётных чисел

# def sum_count_chet(num: int):
#     summ = 0
#     count = 0
#     for i in range(1, num+1):
#         if i % 2 == 0:
#             summ += i
#             count +=1
#     return summ, count
# print(sum_count_chet(6))
# print(sum_count_chet(12))

# Функция принимает n и возвращает сумму только тех чисел, которые:
# чётные, и больше 5

def sum_numb(num: int):
    summ = 0
    for i in range(2, num+1):
        if i % 2 == 0:
            if i > 5 :
                summ += i
    return summ
print(sum_numb(2))
print(sum_numb(8))
print(sum_numb(10))
