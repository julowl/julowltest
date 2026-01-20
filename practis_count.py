#Пользователь вводит число n.
# Нужно пройти все числа от 1 до n включительно и для каждого сделать следующее:
# Если число кратно 3, добавить его к сумме sum3 и увеличить счётчик count3 на 1
# Если число кратно 5, добавить его к сумме sum5 и увеличить счётчик count5 на 1
# Если число кратно и 3, и 5, добавить его к отдельной сумме sum15 и увеличить отдельный счётчик count15 на 1
# В конце вывести: sum3 и count3, sum5 и count5, sum15 и count15

n = int(input(">>>"))
count3 = 0
count5 = 0
count15 = 0
sum3 = 0
sum5 = 0
sum15 = 0
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 ==0:
        sum15 += i
        count15 += 1
    if i % 3 == 0:
        sum3 += i
        count3 += 1
    if i % 5 == 0:
        sum5 += i
        count5 +=1
print("sum3=", sum3, "count3=", count3)
print("sum5=", sum5, "count5=", count5)
print("sum15=", sum15, "count15=", count15)
