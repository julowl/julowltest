#Дано дробное число x. Выведите вторую цифру после точки.

# x = float(input())
#Теперь x_str — это строка
#Мы можем работать с ней как с обычным текстом.
# x_str = str(x)
# #Если у числа есть десятичная часть, то в строке есть символ "."
# if '.' in x_str:
# #parts будет списком из двух элементов:
#     parts = x_str.split('.')
# #Берём дробную часть
#     decimal_part = parts[1]
# #Проверяем, достаточно ли символов в дробной части
#     if len(decimal_part) >= 2:
#         print(decimal_part[1]) #вторая цифра после точки
#     else:
#         print(0) #если цифры нет, выводим 0
# else:
#     print(0)

# Семья решила заняться оптимизацией своих денежных расходов и придумала следующую схему:
# 10 % доходов идут на отпуск
# 30 % доходов на пропитание и еду
# 5 % на коммунальные платежи
# 15 % на выходной досуг
# остальные 40% идут в накопления
#Напишите для семьи программу, которая будет принимать на вход месячный доход мужа и жены
# и расчитывать сколько им нужно отложить на каждую категорию.

husband_income = float(input())
wife_income = float(input())

# Переводим в копейки (целые числа) с округлением
husband_pennies = int(round(husband_income * 100))
wife_pennies = int(round(wife_income * 100))

total_pennies = husband_pennies + wife_pennies

vacation = total_pennies * 10 // 100    # 10%
food = total_pennies * 30 // 100        # 30%
utilities = total_pennies * 5 // 100    # 5%
leisure = total_pennies * 15 // 100     # 15%

spent = vacation + food + utilities + leisure
savings = total_pennies - spent          # что останется — в накопления

categories = [
    ("Отпуск", vacation),
    ("Пропитание и еда", food),
    ("Коммунальные платежи", utilities),
    ("Досуг", leisure),
    ("Накопления", savings)
]

for name, pennies in categories:
    rub = pennies // 100
    kop = pennies % 100
    print(f"{name}: {rub} руб. {kop} коп.")