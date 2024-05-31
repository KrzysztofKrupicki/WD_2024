# Krupicki Krzysztof, 175036, Wariant 1

print('\n=== Zadanie 1 ===')
a = (3, 2, 5, 3)


def func_1(krotka):
    for item in set(krotka):
        print(item)


func_1(a)

print('\n=== Zadanie 2 ===')
string = 'przykladowy tekst'
string = string.replace(" ", "")
print(string[::3][::-1])

print('\n=== Zadanie 3 ===')


def func_3(*args):
    if len(args) == 0:
        return None
    result = 1
    for i in args:
        result *= i
    return result


print(func_3(5, 2, 7))  # 70

print('\n=== Zadanie 4 ===')
lista_slow = ['apple', 'pear', 'watermelon', 'melon', 'cherry', 'strawberry']  # apple (5), # watermelon (10)
print([len(item) for item in lista_slow if 'l' in item and 'a' in item])

print('\n=== Zadanie 5 ===')


def zad5(zdanie):
    zdanie = zdanie.lower()
    znaki = [' ', '?', '.']
    for i in znaki:
        zdanie = zdanie.replace(i, "")
    return zdanie == zdanie[::-1]


print(zad5('A to kawony sama da Ada? Ma synowa kota.'))  # True

print('\n=== Zadanie 6 ===')


def func_2(n):
    if n < 0:
        return 'Błędny argument'
    el = [1, 1, 1]
    for i in range(3, n + 1):
        el.append(2 * el[i - 1] + el[i - 2] - el[i - 3])
    return el[n]


print(func_2(19))  # 744685
print(func_2(-1))  # 744685

print('\n=== Zadanie 7 ===')


class Frac:
    def __init__(self, licznik, mianownik):
        def nwd(x, y):
            while y:
                x, y = y, x % y
            return x

        self.licznik = int(licznik / nwd(licznik, mianownik))
        self.mianownik = int(mianownik / nwd(licznik, mianownik))

    def __str__(self):
        return f'{self.licznik}/{self.mianownik}'

    def __add__(self, other):
        if isinstance(other, Frac):
            if self.mianownik == other.mianownik:
                return Frac(self.licznik + other.mianownik, self.mianownik)
            return Frac(self.licznik * other.mianownik + other.licznik * self.mianownik,
                        self.mianownik * other.mianownik)
        return Frac(self.licznik + other * self.mianownik, self.mianownik)

    def __radd__(self, other):
        if isinstance(other, Frac):
            if self.mianownik == other.mianownik:
                return Frac(self.licznik + other.mianownik, self.mianownik)
            return Frac(self.licznik * other.mianownik + other.licznik * self.mianownik,
                        self.mianownik * other.mianownik)
        return Frac(other * self.mianownik + self.licznik, self.mianownik)

    def __mul__(self, other):
        if isinstance(other, Frac):
            return Frac(self.licznik * other.licznik, self.mianownik * other.mianownik)
        return Frac(self.licznik * other, self.mianownik)

    def __rmul__(self, other):
        if isinstance(other, Frac):
            return Frac(self.licznik * other.licznik, self.mianownik * other.mianownik)
        return Frac(self.licznik * other, self.mianownik)

    def __gt__(self, other):
        if isinstance(other, Frac):
            if self.mianownik == other.mianownik:
                return self.licznik > other.licznik
            return self.licznik * other.mianownik > other.licznik * self.mianownik
        return self.licznik > other * self.mianownik


print(Frac(2, 6))  # 2/6 = 1/3
print(Frac(2, 6) + Frac(1, 5))  # 2/6 + 1/5 = 10/30 + 6/30 = 16/30 = 8/15
print(2 + Frac(2, 6))  # 2 + 2/6 = 12/6 + 2/6 = 14/6 = 7/3
print(Frac(2, 6) * Frac(1, 5))  # 2/6 * 1/5 = 2/30 = 1/15
print(2 * Frac(2, 6))  # 2 * 2/6 = 4/6 = 2/3
print(Frac(3, 6) > Frac(1, 3))  # 3/6 > 1/3 -> 9/18 > 6/18 -> True
print(Frac(3, 6) > 1.5)  # 3/6 > 9/6 -> False
