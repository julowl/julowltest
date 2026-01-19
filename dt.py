

#print('Привет;','мне;','нравится;','программирование',sep="")
#print()
#print('но','писать','код','что-то','не','очень',sep=" ", end=".")
#print('Может','поможешь', sep=" ", end="?")

#print('hello \n \nworld')
#print('hello', end= "\n" * 3)
#print('world')

#print('красный\tоранжевый\tжелтый\tзеленый')

#print("Текст внутри \"двойных\" кавычек")
#print('Текст внутри \'одинарных\' кавычек')

#print('Иван сказал: "Ты зачем выделил все свои слова одинарными кавычками?".')
#print("Антон ответил: \"'Если' 'бы' 'я' 'знал'\".")


#print(type(print))

#s1 = "first"
#s2 = "second"
#s1, s2 = s2, s1 = s1, s2
#print(s1, s2)

#a = input()
#b = input()
#print(a,b)

#name = input("Ваше имя:")
#age = input("Ваш возраст:")
#print(name, age)

#number = input()
#string = input()
#print("Это число:",number)
#print("Это строка:", string)

#print((1245**13+20**5**3-40)*400)

#a = int(input())
#b = int(input())
#c = int(input())
#print((a**c+b**c)**(a*b))

#a = 14 // -4
#print(a)

#m = int(input())
#hours = m // 60
#rest_m = m % 60
#print(hours, "часов", rest_m , "минут")

#time_mins = int(input())
#start_hours = int(input())
#start_mins = int(input())

#start_all_mins = start_hours * 60 + start_mins
#end_all_mins = start_all_mins + time_mins
#end_hours = end_all_mins// 60
#end_mins = end_all_mins % 60
#end_hours = end_hours % 24
#print(end_hours, end_mins)


#a = int(input()) #минут в день
#b = int(input()) #секунд в день
#n = int(input()) #кол-во дней

#day = a *60 +b
#all_seconds = day * n
#hours = all_seconds // 3600
#minutes = (all_seconds % 3600) // 60
#seconds = all_seconds % 60
#print(hours,minutes, seconds)


#a = 5
#a += a
#a *= a
#print(a)

a = int(input())# стоимость квартиры
y = int(input())# процент годовых
x = int(input())# первоначальный взнос
b = int(input())# выплата каждыцй год

summ = a - x
for i in range(3):
    summ -= b
    summ = int(summ  * (1 + y / 100))
    print(summ)
