print(f'\n=== Zadanie 1 ===')


class Car:
    def __init__(self, marka, rok):
        self.marka = marka
        self.rok = rok


car1 = Car("Opel", 2001)
car2 = Car("Volkswagen", 2014)
print(f'Marka: {car1.marka}, rok: {car1.rok}')
print(f'Marka: {car2.marka}, rok: {car2.rok}')
car1 = car2
print(f'Marka: {car1.marka}, rok: {car1.rok}')
print(f'Marka: {car2.marka}, rok: {car2.rok}')

print(f'\n=== Zadanie 2 ===')


class Fruit:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight

    def isfresh(self):
        if self.color in ['brown', 'black']:
            return False
        return True

    def greater(self, other):
        return self.weight > other.weight

    def __gt__(self, other):
        return self.weight > other.weight


# dziedziczenie klasy i rozszerzanie o nowe metody
class Vegetable(Fruit):
    def isfresh(self):
        if self.color in ['brown', 'black', 'blue']:
            return False
        return True

    def __init__(self, weight, color='green', shape='rounded'):
        Fruit.__init__(self, color, weight)
        self.shape = shape


Apple = Fruit("green", 12)
Banana = Fruit("brown", 7)
Orange = Fruit("orange", 4)
print(Apple.color)
print(Orange.weight)
print(Banana.isfresh())
print(Orange.isfresh())
print(Orange.greater(Apple))
print(Apple > Orange)

print(f'\n=== Zadanie 3 ===')


class Account:
    def __init__(self, login, saldo_poczatkowe):
        self.login = login
        self.saldo = saldo_poczatkowe

    def pokaz_saldo(self):
        print(f'Twoje saldo wynosi {self.saldo} zł.')

    def wplata(self, kwota):
        self.saldo += kwota
        print(f'Saldo po operacji wynosi {self.saldo} zł')

    def wyplata(self, kwota):
        if kwota <= 0:
            print("Brak wystarczających środków na koncie lub nieprawidłowa kwota.")
            return
        if kwota <= self.saldo:
            print(f'Saldo po operacji wynosi {self.saldo} zł.')
            self.saldo -= kwota
            self.saldo = self.saldo - kwota
            return

    def przelew(self, odbiorca, kwota, tytul_przelewu):
        if kwota <= 0:
            print("Brak wystarczających środków na koncie lub nieprawidłowa kwota.")
            return
        if self.saldo >= kwota > 0:
            odbiorca.saldo += kwota
            print(
                f'Przelew o tytule "{tytul_przelewu}" do {odbiorca.login}, kwota przelewu {kwota} zł został wykonany. '
                f'Saldo po operacji wynosi {self.saldo} zł.')
            return


jan = Account("janek235", 1253)
adam = Account("adam97", 958)
robert = Account("bobert03", 293)
jan.przelew(adam, 269, "klawiatura")
adam.wyplata(500)
robert.wplata(-50)
jan.pokaz_saldo()


class PrivateAccount(Account):
    def przelew_wynagrodzenia(self, kwota):
        self.saldo += kwota
        print(f'Otrzymano przelew wynagrodzenia w wysokości {kwota} zł')


class FirmAccount(Account):
    def przelew_podatkowy(self, kwota):
        if kwota <= 0:
            print("Brak wystarczających środków na koncie lub nieprawidłowa kwota.")
            return
        if self.saldo >= kwota:
            self.saldo -= kwota
            print(f'Wykonano przelew do Urzędu Skarbowego w wysokości {kwota} zł')
            return

    def przelew_zus(self, kwota):
        if kwota <= 0:
            print("Brak wystarczających środków na koncie lub nieprawidłowa kwota.")
            return
        if self.saldo >= kwota:
            self.saldo -= kwota
            print(f'Wykonano przelew do Zakładu Ubezpieczeń Społecznych w wysokości {kwota} zł')
            return


class Romanian:
    def __init__(self, liczba):
        self.liczba = liczba

    def __len__(self):
        return len(self.liczba)

    def __add__(self, other):
        return arabic_to_romanian(romanian_to_arabic(self.liczba) + romanian_to_arabic(other.liczba))

    def __sub__(self, other):
        return arabic_to_romanian(romanian_to_arabic(self.liczba) - romanian_to_arabic(other.liczba))

    def __mul__(self, other):
        return arabic_to_romanian(romanian_to_arabic(self.liczba) * romanian_to_arabic(other.liczba))

    def print(self):
        print(self.liczba)

    def __getitem__(self, item):
        return self.liczba[item]



def romanian_to_arabic(rzymskie):
    rzym = {"M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1}

    arabskie = 0
    for i in range(len(rzymskie) - 1):
        if rzym[rzymskie[i]] < rzym[rzymskie[i + 1]]:
            arabskie -= rzym[rzymskie[i]]
        else:
            arabskie += rzym[rzymskie[i]]
    arabskie += rzym[rzymskie[-1]]
    return arabskie


def arabic_to_romanian(arabskie):
    arab = {1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"}

    rzymskie = ""
    for i in arab:
        while arabskie >= i:
            rzymskie += arab[i]
            arabskie -= i
    return rzymskie


x = Romanian("XXIX")  # 29
y = Romanian("XIV")  # 14

print(f'{x.liczba} ({romanian_to_arabic(x.liczba)}) + {y.liczba} ({romanian_to_arabic(y.liczba)}) '
      f'= {x + y} ({romanian_to_arabic(x + y)})')
print(f'{x.liczba} ({romanian_to_arabic(x.liczba)}) - {y.liczba} ({romanian_to_arabic(y.liczba)}) '
      f'= {x - y} ({romanian_to_arabic(x - y)})')
print(f'{x.liczba} ({romanian_to_arabic(x.liczba)}) * {y.liczba} ({romanian_to_arabic(y.liczba)}) '
      f'= {x * y} ({romanian_to_arabic(x * y)})')
x.print()
print(len(y))
print(y[2])

print('====')
for i in x:
    print(i)