#1.Пользователь вводит число.Нужно вывести:"even", если число чётное, "odd", если нечётное
#number = int(input())
#if number % 2 == 0:
#    print("even")
#else:
#    print("odd")

#2.Пользователь вводит два числа.Нужно:вывести "first", если первое больше второго
#вывести "second", если второе больше первого, вывести "equal", если они равны

#number1 = int(input())
#number2 = int(input())
#if number1 > number2:
#    print("first")
#elif number2 > number1:
#    print("second")
#else:
#    print("equal")

#3.Пользователь вводит одно число.Нужно:если число положительное и чётное → вывести "good"
# если положительное и нечётное → "bad", если число меньше или равно 0 → "zero or negative"

#new_numb = int(input())
#if new_numb > 0:
#    if new_numb % 2 == 0:
#        print("good")
#    else:
#        print("bad")
#else:
#    print("zero or negative")

#4.Пользователь вводит строку. Если длина строки: меньше 5 → вывести "short"
# от 5 до 10 включительно → "medium", больше 10 → "long"

#text = input()
#if len(text) < 5:
#    print("short")
#elif len(text) > 10:
#    print("long")
#else:
#    print("medium")

#5.  пустая строка
new_text = input()#strip - метод убирает проблелы по краям строки
if len(new_text.strip()) == 0: #if text == "": or if not text:
    print("empty")
else:
    print("not empty")