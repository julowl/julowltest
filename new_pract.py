from decimal import Decimal, getcontext

getcontext().prec = 60

a = Decimal(input())
b = Decimal(input())

print(a.sqrt() + b)

