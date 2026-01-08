#пройти по всем числам от 2-5000 и найти все простые
#сначала найти что P простое
#потом (p**2)-1
#проверить что полученое число простое

def is_prime2(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def prime_ch(n: int) -> list:
    prime_numbers = []
    for p in range(2, n):
        if is_prime2(p):
            prime_numbers.append(p)
    return prime_numbers

for i in prime_ch(5000):
    i = (i**2)-1
    if not is_prime2(i):# первое число для которого не выполняется все условия
        print(i)
        break




