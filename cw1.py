import math

print(f'\n=== Zadanie 6a ===')


def zadanie_6a(n):
    if 0 < n < 100:
        for i in range(n):
            print(f'{i} * {n} = {i * n}')
    else:
        print('n is too large')


zadanie_6a(7)
zadanie_6a(101)

print(f'\n=== Zadanie 6b ===')


def zadanie_6b(a, b):
    return f'{a}/{b} = {int(a / math.gcd(a, b))}/{int(b / math.gcd(a, b))}'


print(zadanie_6b(64, 256))

print(f'\n=== Zadanie 6c ===')


def zadanie_6c(n):
    n = int(n)
    e1 = (1 + (1 / n)) ** n
    e2 = 0
    for i in range(n):
        x = 1 / math.factorial(i)
        e2 += x
    return e1, e2


print(f'e1(5) = {zadanie_6c(5)[0]}')
print(f'e2(5) = {zadanie_6c(5)[1]}')
print(f'e1(15) = {zadanie_6c(15)[0]}')
print(f'e2(15) = {zadanie_6c(15)[1]}')
print(f'math.e = {math.e}')
print(f'e1(10) - math.e = {zadanie_6c(10)[0] - math.e}')
print(f'e2(10) - math.e = {zadanie_6c(10)[1] - math.e}')
print(f'|e1(10) - math.e| = {abs(zadanie_6c(10)[0] - math.e)}')
print(f'|e2(10) - math.e| = {abs(zadanie_6c(10)[1] - math.e)}')

print(f'\n=== Zadanie 6d ===')


def nwd(x, y):
    while y:
        x, y = y, x % y
    return x


print(nwd(24, 100))
