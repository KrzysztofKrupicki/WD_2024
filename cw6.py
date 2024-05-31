print(f'\n=== Zadanie 1 ===')


class RPGGame:
    def __init__(self, imie, zywotnosc, punkty_taktyki):
        self.imie = imie
        self.zywotnosc = zywotnosc
        self.punkty_taktyki = punkty_taktyki

    def __mul__(self, other):
        return self * other

    def zmiana_pkt_zycia(self, nowa_wartosc):
        if nowa_wartosc <= 0:
            self.zywotnosc = 0
        elif 0 < nowa_wartosc <= 100:
            self.zywotnosc = nowa_wartosc
        elif nowa_wartosc >= 100:
            self.zywotnosc = 100
        else:
            print('Niepoprawna wartość')


class Lucznik(RPGGame):
    def __init__(self, imie, zywotnosc, zrecznosc, punkty_taktyki):
        RPGGame.__init__(self, imie, zywotnosc, punkty_taktyki)
        self.zrecznosc = zrecznosc

    def moc_ataku(self):
        return self.zrecznosc * self.punkty_taktyki * self.zywotnosc


class Wojownik(RPGGame):
    def __init__(self, imie, zywotnosc, sila, punkty_taktyki):
        RPGGame.__init__(self, imie, zywotnosc, punkty_taktyki)
        self.sila = sila

    def moc_ataku(self):
        return self.sila * self.punkty_taktyki * self.zywotnosc

    def sprawdz_zywotnosc(self):
        if self.zywotnosc < 0:
            self.zywotnosc = 0
        if 0 < self.zywotnosc < 20:
            self.zywotnosc = 150
            print(f'Żywotność wojownika spadła poniżej 20% HP. '
                  f'Wojownik wpada w szał, jego HP wynosi teraz {self.zywotnosc}%')


lucznik1 = Lucznik('Adam', 100, 4, 6)
wojownik1 = Wojownik('Tomasz', 100, 7, 5)

print(f'Lucznik: {lucznik1.imie} ma {lucznik1.zywotnosc}% HP, {lucznik1.zrecznosc} pkt zręczności, '
      f'{lucznik1.punkty_taktyki} pkt taktyki. '
      f'Moc ataku: {lucznik1.moc_ataku()}')
print(f'Wojownik: {wojownik1.imie} ma {wojownik1.zywotnosc}% HP, {wojownik1.sila} pkt siły, '
      f'{wojownik1.punkty_taktyki} pkt taktyki. '
      f'Moc ataku: {wojownik1.moc_ataku()}')

wojownik1.zmiana_pkt_zycia(19)
print(f'Żywotność {wojownik1.imie} wynosi: {wojownik1.zywotnosc}% HP')
wojownik1.sprawdz_zywotnosc()
print(f'Żywotność {wojownik1.imie} wynosi: {wojownik1.zywotnosc}% HP')

print(f'\n=== Zadanie 2 ===')


class Vector:
    def __init__(self, wartosci):
        self.wartosci = wartosci

    def __getitem__(self, item):
        return self.wartosci[item]

    def __len__(self):
        return len(self.wartosci)

    def __add__(self, other):
        if len(self.wartosci) != len(other.wartosci):
            print('Dlugości wektorów są inne')
        else:
            return Vector([self.wartosci[i] + other.wartosci[i] for i in range(len(other.wartosci))])

    def __sub__(self, other):
        if len(self.wartosci) != len(other.wartosci):
            print('Dlugości wektorów są inne')
        else:
            return Vector([self.wartosci[i] - other.wartosci[i] for i in range(len(other.wartosci))])

    def __mul__(self, other):
        return Vector([i * other for i in self.wartosci])

    def __rmul__(self, other):
        return Vector([i * other for i in self.wartosci])

    def print(self):
        return self.wartosci


x1 = Vector([2, 6, -3])
x2 = Vector([1, -7, 5, 2])
x3 = Vector([5, 3, 9, -1])

x1 + x3
print((x2 + x3).print())
print((x3 - x2).print())
print((x1 * 2).print())
print((2 * x1).print())
print(f'\n=== Zadanie 3 ===')


class Polynomial(Vector):
    def degree(self):
        return len(self.wartosci) - 1

    def print(self):
        result = ""
        for i, wartosc in enumerate(self.wartosci):
            power = self.degree() - i
            if wartosc == 0:
                continue
            if power == 0:
                result += f'{"+" if wartosc > 0 else ""}{wartosc}'
            else:
                result += f'{"+" if wartosc > 0 else ""}{wartosc}x^{power}'
        print(result.lstrip("+"))

    def __add__(self, other):
        if isinstance(other, Polynomial):
            if self.degree() == other.degree():
                return Polynomial([self.wartosci[i] + other.wartosci[i] for i in range(len(self.wartosci))])

            self_len = len(self.wartosci)
            other_len = len(other.wartosci)
            max_len = max(self_len, other_len)
            min_len = min(self_len, other_len)
            tab = [0] * max_len
            if self_len > other_len:
                for i in range(max_len - min_len):
                    tab[i] = self.wartosci[i]
            else:
                for i in range(max_len - min_len):
                    tab[i] = other.wartosci[i]
            for i in range(min_len - 2, max_len):
                if self_len > other_len:
                    tab[i] = self.wartosci[i] + other.wartosci[i - max_len]
                    print(tab)
                else:
                    tab[i] = self.wartosci[i - max_len] + other.wartosci[i]
                    print(tab)
            return Polynomial(tab)

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            if self.degree() == other.degree():
                return Polynomial([self.wartosci[i] - other.wartosci[i] for i in range(len(self.wartosci))])

            self_len = len(self.wartosci)
            other_len = len(other.wartosci)
            max_len = max(self_len, other_len)
            min_len = min(self_len, other_len)
            tab = [0] * max_len
            if self_len > other_len:
                for i in range(max_len - min_len):
                    tab[i] = self.wartosci[i]
            else:
                for i in range(max_len - min_len):
                    tab[i] = other.wartosci[i]
            for i in range(min_len - 2, max_len):
                if self_len > other_len:
                    tab[i] = self.wartosci[i] - other.wartosci[i - max_len]
                else:
                    tab[i] = self.wartosci[i - max_len] - other.wartosci[i]
            return Polynomial(tab)

    def wartosc_dla_argumentu(self, argument):
        wartosc = 0
        for i in range(len(self.wartosci)):
            wartosc += self.wartosci[i] * (argument ** i)
        return wartosc


x = Polynomial([-2, 5, 8])
y = Polynomial([3, 3, -5, 7])
z = x + y  # 3 8 1
z.print()
z = y - x  # -13 -2 5
z.print()
a = Polynomial([1, -7, 0, -1])
a.print()

b = Polynomial([3, 2])  # 2x + 3  | x = 2 | = 7
c = b * 2
c.print()
print(f'Stopień wielomianu a: {a.degree()}')
print(f'Indeks 1 wielomianu a: {a[1]}')
print(f'Wartość wielomianu b dla x = 2: {b.wartosc_dla_argumentu(2)}')
