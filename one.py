import random

print('Hello, World!')

r = [1,3,5,4,6,2,9,7,8,6]
print(r[4])
print(r)
r.pop()
print(r)
r.append(23)
print(r)


for i in r:
    if i % 2 == 0:
        print(i ** 2)

def f(x: float) -> float:
    return x ** 2  - 6 * x - 2

x = 0
step = 0
while abs(f(x)) > 0.1:
    x = random.uniform(-40, 40)
    step += 1

print(x, step, f(x))





