# append = «добавь в конец списка»

# nums = [3, 7, 2, 8, 5, 10, 1]
# for n in nums:
#     if n % 2 ==0:
#         print("even")
#     else:
#         print(n)

# nums = [3, 7, 2, 8, 5, 10, 1]
# result = []
#
# for n in nums:
#     if n % 2 == 0:
#         result.append("e")
#     else:
#         result.append(n)
#
# print(result)

# Найти первое чётное число
# и прекратить цикл, когда оно найдено.
# вывести это число
# если чётных нет — вывести "no even"

# nums = [7, 11, 4, 9, 10, 3]
# for n in nums:
#     if n % 2 ==0:
#         print(n)
#         break
# if not found:
#     print("no even")

# Есть список чисел.
# Нужно: пройтись по списку
# найти первое число, которое делится и на 2, и на 3
# если нашли — вывести это число и остановиться
# если такого числа нет — вывести "not found"

# nums = [7, 11, 4, 9, 10, 3]
# found = False
# for n in nums:
#     if n % 2 ==0 and n % 3 ==0:
#         print(n)
#         found = True
#         break
# if not found:
#     print("no even")
# print("END")

# Есть список чисел.
# Нужно написать функцию, которая:
# проходит по списку, считает:
# сколько чётных, сколько нечётных
# возвращает кортеж из двух чисел

# nums =[1,8,10,5,6,0,11,2,7]
# def found_num(nums : int):
#     count_chet = 0
#     count_nechet = 0
#     for n in nums:
#         if n % 2 ==0:
#             count_chet +=1
#         if n % 3 ==0:
#             count_nechet +=1
#     return count_chet, count_nechet
# print(found_num(nums))

# Написать функцию, которая: принимает список чисел
# возвращает новый список, где:
# если число делится на 2 → "even"
# если делится на 3 → "three"
# если делится на 2 и 3 → "even_three"
# иначе → само число

# numb = [1,8,10,5,6,0,11,2,7]
# new_numb = []
# def new_list(numb : int):
#     for n in numb:
#         if n % 2 ==0:
#             new_numb.append("even")
#         elif n % 3 ==0:
#             new_numb.append("three")
#         elif n % 2 ==0 and n % 3 ==0:
#             new_numb.append("even_three")
#         else:
#             new_numb.append(n)
# new_list(numb)
# print(new_numb)


# Напиши функцию, которая:
# принимает список чисел
# возвращает словарь: even — сколько чётных
# three — сколько кратных 3

# def schet_numb(nub: list) -> dict:
#     numb = {
#         "even": 0,
#         "three": 0
#     }
#     nub = [2, 8, 5, 6, 9, 3, 12, 14, 15, 20, 27, 22]
#     for n in nub:
#         if n % 2 ==0:
#             numb["even"] +=1
#         if n % 3 ==0:
#             numb["three"] +=1
# schet_numb(nub)
# print(numb)

# есть список чисел
# есть словарь с двумя пустыми списками
# заполни их


# nums = [2, 8, 5, 6, 9, 3, 12, 14, 15, 20, 27, 22]
# result = {
#     "even": [],
#     "three": [],
#     "both":[]
# }
# for n in nums:
#     if n % 2 ==0:
#         result["even"].append(n)
#     if n % 3 ==0:
#         result["three"].append(n)
#     if n % 2 ==0 and n % 3 ==0:
#         result["both"].append(n)
# print(result)

# Есть список чисел.
# Нужно посчитать, сколько чисел:
# чётных, нечётных
# Результат вернуть в виде словаря.

def res_slov(nums :list) -> dict:
    result = {
        "chet": [],
        "not_chet": []
    }
    for n in nums:
        if n % 2 ==0:
            result["chet"].append(n)
        else:
            result["not_chet"].append(n)
    return result

nums = [2, 8, 5, 6, 9, 3, 12, 14, 15, 20, 27, 22]
res = res_slov(nums)
print(res)