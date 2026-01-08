#1 нужен массив 2-5000
#2 нужен пустой массив чтобы оттуда достать?
##второй цийл я тупо не поняла
a = list(range(2, 5000))
b = []
def is_prime(n: int) -> int:
    for i in range(2, n):
        if n % i == 0:
            return 0
    return n
for p in a:
    r = is_prime(p)
    if r != 0:
        b.append(r)
print(b)




