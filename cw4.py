print(f'\n=== Zadanie 1 ===')
names = ["michał", "nela", "ola", "przemek"]
print(f'Powiększanie pierwszych liter: {[i.capitalize() for i in names]}')
print(f'Imiona z literą "l": {[i for i in names if "l" in i]}')
print(f'Żeńskie imiona: {tuple([i for i in names if i.endswith("a")])}')
print(f'Sumaryczna długość: {sum([len(i) for i in names])}')

print(f'\n=== Zadanie 2 ===')


def zamiana_cyfr_na_slowa(string):
    slownik = {"0": "zero",
               "1": "jeden",
               "2": "dwa",
               "3": "trzy",
               "4": "cztery",
               "5": "pięć",
               "6": "sześć",
               "7": "siedem",
               "8": "osiem",
               "9": "dziewięć"}

    wynik = ""
    for i in string:
        if i in slownik.keys():
            wynik += f'{slownik.get(i)} '
    return wynik


print(zamiana_cyfr_na_slowa("45j2"))
print(zamiana_cyfr_na_slowa("5736fj281"))

print(f'\n=== Zadanie 3 ===')


def product(*nums):
    result = 1
    for i in nums:
        result *= i
    return result


print(f'Iloczyn: {product(5, 4)}')
print(f'Iloczyn: {product(5, 4, 3, 2)}')


def sum_power_n(n, *nums):
    return sum([i ** n for i in nums])


print(f'Suma n-tych poteg: {sum_power_n(2, 2, 3)}')
print(f'Suma n-tych poteg: {sum_power_n(2, 3, 4, 5)}')


def mean(*nums):
    if len(nums) == 0:
        return None
    return sum(nums) / len(nums)


print(f'Średnia: {mean()}')
print(f'Średnia: {mean(5, 15)}')
print(f'Średnia: {mean(5, 4, 3)}')


def gmean(*nums):
    if len(nums) == 0:
        return None
    return product(*nums) ** (1 / len(nums))


print(f'Średnia geometryczna: {gmean()}')
print(f'Średnia geometryczna: {gmean(8, 2)}')
print(f'Średnia geometryczna: {gmean(5, 4, 3, 2)}')


def sum_string_length(*strings):
    return sum([len(i) for i in strings])


print(f'Suma długości stringów: {sum_string_length()}')
print(f'Suma długości stringów: {sum_string_length("kajak")}')
print(f'Suma długości stringów: {sum_string_length("monitor", "kalambury", "komputer")}')


def max_min_value(*args):
    return max(args), min(args)


print(f'Maksymalna, minimalna wartość: {max_min_value(5, 3, 7, 2)}')

print(f'\n=== Zadanie 4 ===')


def dict_name_phone(**name_phone):
    for name, phone in name_phone.items():
        print(f'{name} ma numer {phone}')


first_test = {"Jan Kowalski": 574637285,
              "Anna Nowak": 431684736}
second_test = {"Adam Małysz": 684937591,
               "Robert Lewandowski": 777582491}
dict_name_phone(**first_test)
dict_name_phone(**second_test)


def percentage_earning_increase(**sallary):
    sallary_list = list(sallary.values())
    avg_sallary = sum(sallary_list) / len(sallary_list)
    return avg_sallary


first_test = {"styczeń": 2000,
              "luty": 3000}
second_test = {"styczeń": 2800,
               "luty": 3200,
               "marzec": 3400,
               "kwiecień": 3400,
               "maj": 3800}
print(f'Średnia arytmetyczna zarobków: {percentage_earning_increase(**first_test)}')
print(f'Średnia arytmetyczna zarobków: {percentage_earning_increase(**second_test)}')

print(f'\n=== Zadanie 5 ===')


def pesel_check(pesel):
    if len(pesel) != 11 or pesel.isdigit() is False:
        print('Błędny format')
        return False

    wagi_cyfr = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    suma = sum([wagi_cyfr[i] * int(pesel[i]) for i in range(10)])
    cyfra_kontrolna = 10 - (suma % 10)
    if suma % 10 == 0:
        cyfra_kontrolna = 0
    if cyfra_kontrolna != int(pesel[10]):
        print('Niepoprawny PESEL')
        return False

    yyyy = int(pesel[:2])
    mm = int(pesel[2:4])
    dd = int(pesel[4:6])
    plec = int(pesel[9])

    if plec % 2 == 0:
        plec = 'kobieta'
    else:
        plec = 'mężczyzna'

    if 81 <= mm <= 92:
        yyyy += 1800
        mm -= 80
    elif 1 <= mm <= 12:
        yyyy += 1900
    elif 21 <= mm <= 32:
        mm -= 20
        yyyy += 2000
    elif 41 <= mm <= 52:
        mm -= 40
        yyyy += 2100
    elif 61 <= mm <= 72:
        mm -= 60
        yyyy += 2200

    print(f'Data urodzenia {dd: 02d}.{mm: 02d}.{yyyy}, płeć: {plec}')
    return True


print(pesel_check("55030101230"))
print(pesel_check("55030101195"))
print(pesel_check("550301d1194"))
print(pesel_check(input("Podaj PESEL: ")))
