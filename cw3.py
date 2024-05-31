import math

print(f'\n=== Zadanie 1a ===')
nazwiska = ["Adamczyk", "Nowak", "Kowalski", "Lewandowski", "Bodnar", "Ząbek", "Orzechowski"]
print(nazwiska)
nazwiska.append("Sokół")  # dodaje na koncu listy
print(nazwiska)
nazwiska.extend(["Sowa", "Wiśniewski"])  # rozszerza liste o nowe elementy z listy x
print(nazwiska)
nazwiska.insert(3, "Klawiatur")  # wstawia na pozycji n nowy element x
print(nazwiska)
nazwiska.remove("Sowa")  # usuwa z listy element x
print(nazwiska)
nazwiska.pop()  # usuwa ostatni element na liscie
print(nazwiska)
print(nazwiska.index("Kowalski"))  # pokazuje index elementu x
nazwiska.sort()  # sortuje liste A-Z
print(nazwiska)
nazwiska.reverse()  # sortuje liste Z-A
print(nazwiska)
nazwiska_kopia = nazwiska.copy()  # tworzy kopie listy
print(nazwiska_kopia)
nazwiska.clear()  # czysci liste
print(nazwiska)

print([i for i in range(14)])

print(f'\n=== Zadanie 1b ===')
print([i ** 5 for i in range(14)])
print([math.factorial(i) for i in range(20)])
print([math.e ** i for i in range(20)])
nazwiska = ["Adamczyk", "Nowak", "Kowalski", "Bober", "Kamiński", "Lewandowski", "Bodnar", "Ząbek", "Orzechowski"]
print([len(nazwisko) for nazwisko in nazwiska])

print(f'\n=== Zadanie 1c ===')
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(list1 + list2)  # nowa lista o sumie elementow list1 i list2
print([list1[i] + list2[i] for i in range(len(list1))])


def numer_miesiaca(nazwa_miesiaca):
    miesiace = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czerwiec", "lipiec", "sierpień", "wrzesień",
                "październik",
                "listopad", "grudzień"]
    if nazwa_miesiaca in miesiace:
        return miesiace.index(nazwa_miesiaca) + 1
    return -1


print(f'Nr miesiaca dla maja: {numer_miesiaca("maj")}')

pomieszane_miesiace = ['marzec', 'wrzesień', 'kwiecień', 'październik', 'czerwiec', 'listopad', 'luty', 'lipiec', 'maj',
                       'sierpień', 'grudzień', 'styczeń']
pomieszane_miesiace.sort(key=numer_miesiaca)
print(pomieszane_miesiace)


def nazwiska_z_litera_pozniejsza(lista_nazwisk, litera):
    return [nazwisko for nazwisko in lista_nazwisk if ord(nazwisko[0]) > ord(litera)]


print(nazwiska_z_litera_pozniejsza(nazwiska, "N"))


def nazwisko_dluzsze_niz6(lista_nazwisk):
    return [nazwisko for nazwisko in lista_nazwisk if len(nazwisko) > 6]


print(nazwisko_dluzsze_niz6(nazwiska))


def czy_posortowane_dlugoscia_max_min(lista):
    for i in range(1, len(lista)):
        if lista[i - 1] < lista[i]:
            return False
    return True


print(czy_posortowane_dlugoscia_max_min([4, 1, 2, 3]))
print(czy_posortowane_dlugoscia_max_min([4, 3, 2, 1]))


def potega_3(lista):
    return [i ** 3 for i in lista]


print(potega_3([4, 2, 3, 5]))
print(potega_3([1, -6, 10]))


def func(lista, n1, n2):
    for i in range(len(lista)):
        if lista[i] == n1:
            lista[i] = n2
    return lista


print(func([4.2, 2.5, 7.4, 1.3, 3.8, 9.1, 4.4, 6.8, 1.31], 1.3, 32.5))


def func2(lista, n1, n2):
    for i in range(len(lista)):
        if math.isclose(lista[i], n1):
            lista[i] = n2
    return lista


print(func2([4.2, 2.5, 7.4, 1.30000000008, 3.8, 9.1, 4.4, 6.8, 1.31], 1.3, 43.6))

print(f'\n=== Zadanie 2 ===')
panstwa = {"Polska", "Niemcy", "Czechy", "Słowacja", "Litwa"}
panstwa.add("Litwa")  # nic sie nie stalo, zbior posiada tylko unikatowe elementy
print(panstwa)
print("Polska" in panstwa)
panstwa.remove("Niemcy")
print(panstwa)
panstwa2 = {"Polska", "Holandia", "Niemcy", "USA"}
panstwa3 = {"Polska", "Szwecja", "Islandia", "USA"}
print(panstwa.union(panstwa2, panstwa3))
print(panstwa.intersection(panstwa2, panstwa3))
print(panstwa2.difference(panstwa3))
print(panstwa.issubset(panstwa2))

print(f'\n=== Zadanie 3a ===')
t = "Hello", 123, True, "world!", False, None, 34.54
# t[2] = "zmiana" # krotki nie umozliwiaja zmian
print(t[3])
print(t[3:6])
print(t[-3])

print(f'\n=== Zadanie 3b ===')


def dodanie_do_krotki(krotka, element):
    krotka = list(krotka)
    krotka.append(element)
    krotka = tuple(krotka)
    return krotka


print(dodanie_do_krotki(t, "nowy"))


def dodanie_do_krotki2(krotka, element):
    krotka += (element,)
    return krotka


print(dodanie_do_krotki2(t, "python"))


def usuniecie_z_krotki(krotka, element):
    krotka = list(krotka)
    krotka.remove(element)
    krotka = tuple(krotka)
    return krotka


print(usuniecie_z_krotki(t, 123))


def usuniecie_z_krotki2(krotka, element):
    indeks = krotka.index(element)
    del krotka[indeks]
    return krotka


print(usuniecie_z_krotki(t, "Hello"))


def unikalne_elementy_listy(lista):
    return list(set(lista))


print(unikalne_elementy_listy([1, 22, 54, 2, 1, 54, 76]))

print(f'\n=== Zadanie 4a ===')
numery_tel = {"Jan Kowalski": 347234567,
              "Anna Nowak": 573927521,
              "Janusz Adamczyk": 737194068}


def print_phone_numbers(phone_numbers):
    for osoba in phone_numbers:
        print(f'{osoba} ma numer {phone_numbers[osoba]}')


print(print_phone_numbers(numery_tel))
numery_tel["Maria Wesołowska"] = 564723523
numery_tel["Jan Kowalski"] = 123546123
del numery_tel["Janusz Adamczyk"]
print(print_phone_numbers(numery_tel))

print(f'\n=== Zadanie 4b ===')


def zamiana_dni_tygodnia_polskie_na_angielskie(lista):
    dni_tygodnia = {"poniedziałek": "Monday",
                    "wtorek": "Tuesday",
                    "środa": "Wednesday",
                    "czwartek": "Thursday",
                    "piątek": "Friday",
                    "sobota": "Saturday",
                    "niedziela": "Sunday"}
    return [dni_tygodnia[i] for i in lista]


print(zamiana_dni_tygodnia_polskie_na_angielskie(['piątek', 'poniedziałek']))


def sortowanie_nazwy_miesiecy(lista):
    miesiace = {"styczeń": 1,
                "luty": 2,
                "marzec": 3,
                "kwiecień": 4,
                "maj": 5,
                "czerwiec": 6,
                "lipiec": 7,
                "sierpień": 8,
                "wrzesień": 9,
                "październik": 10,
                "listopad": 11,
                "grudzień": 12}
    return sorted(lista, key=miesiace.get)


pomieszane_miesiace = ['listopad', 'lipiec', 'luty', 'czerwiec']
print(sortowanie_nazwy_miesiecy(pomieszane_miesiace))


def zamiana_rzymskich_na_arabskie(rzymskie):
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


def zamiana_arabskich_na_rzymskie(arabskie):
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


testy = [4, 9, 14, 27, 99, 990, 999]
testy2 = ["IV", "IX", "XIV", "XXVII", "IC", "XM", "IM",]

for i in testy:
    print(f'{i} = {zamiana_arabskich_na_rzymskie(i)}')
for j in testy2:
    print(f'{j} = {zamiana_rzymskich_na_arabskie(j)}')
