N = 15

# TODO print True if the n is prime, print False otherwise
# is_prime = True
# for i in range(2, n):
#     if n % i == 0:
#         is_prime = False
#         break
#
# print(is_prime)

def is_prime(n: int) -> bool:
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

is_prime(3)

def prime(a: int) -> int:
    for i in range(2, a):
        if a % i == 0:
            return i
    return a

print(prime(13 * 17))

## TODO 1 найти все простые число до 5000, используя функцию is_prime


## TODO 2 напишем функцию, которая считает для числа n n ^ 3 - 2

## TODO 3* напиши функцию, которая принимает квадратное уравнение в виде ax^2 + bx + c = 0 и находит корни (или 1 любой)


