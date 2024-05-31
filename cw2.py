import math

print(f'\n=== Zadanie 1a ===')
print(f'Math.ceil: {math.ceil(math.pi)}')
print(f'Math.floor: {math.floor(math.pi)}')
print(f'Round: {round(math.pi)}')


def x_mod_y(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a % b
    if isinstance(a, float) or isinstance(b, float):
        return math.fmod(a, b)


print(x_mod_y(6, 2))
print(x_mod_y(6.5, 2))
print(x_mod_y(6, 2.5))


def logarytm(a, n):
    for k in range(2, n):
        print(f'{math.log(a, k)}', end=' | ')


logarytm(16, 6)


def potega_liczby(a):
    print(f'\nmath.exp(a): {math.exp(a)}')
    print(f'math.e**a: {math.e ** a}')
    print(f'math.pow(math.e, a): {math.pow(math.e, a)}')


potega_liczby(7)

print(f'\n=== Zadanie 1b ===')
print(f'math.pow oraz **')
print(math.pow(11, 17))
print(11 ** 17)
print(f'\nmath.remainder oraz %')
print(math.remainder(23, 4))
print(23 % 4)
print(f'\ncosh oraz sinh')
x = 2
cosh = ((math.e ** x) + math.e ** (-x)) / 2
sinh = ((math.e ** x) - math.e ** (-x)) / 2
print(f'cosh: {cosh}\nmath.cosh: {math.cosh(x)}\n{math.isclose(cosh, math.cosh(x))}')
print(f'sinh: {sinh}\nmath.cosh: {math.sinh(x)}\n{math.isclose(sinh, math.sinh(x))}')

print(f'\n=== Zadanie 2a ===')
test_string = "longstoryshortbreak"
print(test_string[12])
print(test_string + test_string)
print(test_string * 3)
print(len(test_string))
print(test_string.capitalize())
print(test_string.split("r"))
print(test_string[::-1])

test_string = "longstoryshort"

print(f'\n=== Zadanie 2b ===')


def parzyste_znaki(string):
    return string[::2]


print(parzyste_znaki(test_string))
print("*")


def ostatnie_znaki(string, n=1):
    return string[-n:]


print(ostatnie_znaki(test_string, 4))
print("*")


def odwroc_string(string):
    return string[::-1]


print(odwroc_string(test_string))
print("*")


def czy_palindrom(string):
    return string == string[::-1]


print(czy_palindrom(test_string))
print(czy_palindrom("kajak"))
print("*")


def ktory_dluzszy(string1, string2):
    if len(string1) > len(string2):
        return string1
    return string2


print(ktory_dluzszy("kajak", test_string))
print("*")


def formatowanie(imie, data_urodzenia):
    return "My name is {0}. My date of birth is {1}.".format(imie.capitalize(), data_urodzenia)


print(formatowanie("jan", "01.01.1970"))

test_string = ("W Roku Pańskim 1345, władca Henryk 12, na rzecz swoich 143209 poddanych uchwalił dekret o 20 "
               "procentowej zniżce podatków.")


def znajdz_sume_liczb(string):
    suma = 0
    liczba = 0
    for letter in string:
        if letter.isdigit():
            liczba = liczba * 10 + int(letter)
        else:
            suma += liczba
            liczba = 0
    return suma


print(znajdz_sume_liczb(test_string))
print(1345 + 12 + 143209 + 20)
