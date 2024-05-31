import numpy as np
import pandas as pd

"""
Zadanie 1
"""

print('=== 1a.1 ===')
calkowite = pd.Series([1, 2, 3, 4, 5])
print(calkowite)

print('=== 1a.2 ===')
stringi = pd.Series(['one', 'two', 'three', 'four', 'five'])
print(stringi)

print('=== 1a.3 ===')
lista = ['melon', 'cherry', 'apple', 'orange', 'banana']
seria_z_listy = pd.Series(lista)
print(seria_z_listy)

print('=== 1a.4 ===')
lista_z_serii = stringi.tolist()
print(lista_z_serii)

print('=== 1a.5 ===')
tab = np.array([3, 6, 1, 7, 4])
seria_z_tablicy = pd.Series(tab)
print(seria_z_tablicy)

print('=== 1a.6 ===')
tablica_z_serii = seria_z_tablicy.to_numpy()
print(tablica_z_serii)

print('=== 1a.7 ===')
seria_1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
seria_2 = pd.Series([4, 5, 6], index=['b', 'c', 'd'])
suma = seria_1.add(seria_2, fill_value=0)
roznica = seria_1.sub(seria_2, fill_value=0)
iloczyn = seria_1.mul(seria_2, fill_value=1)
iloraz = seria_1.div(seria_2, fill_value=1)
print(f'Suma:\n{suma}')
print(f'Różnica:\n{roznica}')
print(f'Iloczyn:\n{iloczyn}')
print(f'Iloraz:\n{iloraz}')

print('=== 1a.8 ===')
losowe = pd.Series(np.random.uniform(-10, 10, size=10))
losowe = np.round(losowe, decimals=1)
print(losowe)

print('=== 1b ===')
my_list = [1, 32, -37, 91, 12, 11, -5]
print(f'List my_list:\n{my_list}')

my_dict = {'a': [1, 3, 2], 'b': [2, 5, 7], 'c': [3, 4, 8], 'd': [4, 10, 12]}
print(f'Dict my_dict:\n{my_dict}')

my_array = np.array([[1, 2, 5], [-2, 3, 3], [5, 2, 6]])
print(f'Array my_array:\n{my_array}')

my_series = pd.Series([1, 32, -37, 91, 12, 11, -5], index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(f'Series my_series:\n{my_series}')

my_list = pd.DataFrame(my_list)
print(f'DataFrame my_list:\n{my_list}')

my_dict = pd.DataFrame(my_dict)
print(f'DataFrame my_dict:\n{my_dict}')

my_array = pd.DataFrame(my_array)
print(f'DataFrame my_array:\n{my_array}')

my_series = pd.DataFrame(my_series)
print(f'DataFrame my_series:\n{my_series}')

my_list = my_list.values.tolist()
print(f'List my_list:\n{my_list}')

my_dict = my_dict.to_dict('list')
print(f'Dict my_dict:\n{my_dict}')

my_array = pd.DataFrame.to_numpy(my_array)
print(f'Array my_array:\n{my_array}')

my_series = my_series.squeeze()
print(f'Series my_series:\n{my_series}')

print('=== 1c ===')
ramka = pd.DataFrame([[1, 2, 4, 5], [-3, 8, 0.5, 10], [2, -5, 7, 3]], index=['l1', 'l2', 'l3'],
                     columns=['a', 'b', 'c', 'd'])
print(ramka)

print(f'Sort po kolumnie a:\n{ramka.sort_values('a')}')
print(f'Element w polu [0,2]: {ramka.iat[0, 2]}')
print(f'Element w kolumnie c wierszu l3: {ramka.c['l3']}')
print(f'Element w wierszu l2 w kolumnie a: {ramka.at['l2', 'a']}')
print(f'Kolumna d:\n{ramka.d}')
print(f'Kolumna b i d:\n{ramka[['b', 'd']]}')
print(f'Wiersz l2:\n{ramka.loc['l2']}')
print(f'Wiersz l2 i l3:\n{ramka.loc[['l2', 'l3']]}')

"""
Zadanie 2
"""

df1 = pd.DataFrame([[2942, 9840, 2794, 8891, 8111, 2933, 8301, 9125],
                    ['Sylwia', 'Katarzyna', 'Teresa', 'Tomasz', 'Cezary', 'Zenon', 'Filip', 'Adrian'],
                    [13, 31, 34, 14, 13, 28, 20, 15]]).T
df1.columns = ['ID', 'Name', 'Age']
weight = [65, 80, 64, 69, 74, 61, 66, 61]
height = [179, 179, 151, 177, 170, 157, 151, 153]
glasses = [False, True, False, True, False, True, False, True]
df2 = pd.DataFrame([[2312, 2336, 2942, 9840, 2794, 8891, 8111, 2933],
                    ['Anna', 'Zofia', 'Sylwia', 'Katarzyna', 'Teresa', 'Tomasz', 'Cezary', 'Zenon'],
                    weight, height, glasses]).T
df2.columns = ['ID', 'Name', 'W', 'H', 'Gl']

print('=== 2.1 ===')
df0 = pd.merge(df1, df2, how='inner')  # polaczylo czesci wspolne
print(f'df1:\n{df1}')
print(f'df2:\n{df2}')
print(f'df0 inner(df1, df2):\n{df0}')
df0 = pd.merge(df1, df2, how='outer')  # polaczylo calossc, brakujace uzupelnilo NaN
print(f'df0 outer(df1, df2):\n{df0}')

print('=== 2.2 ===')
posortowane_imiona = df0.sort_values('Name')
print(f'Sort imiona AZ:\n{posortowane_imiona}')

print('=== 2.3 ===')
nosza_okulary = df0.loc[df0['Gl'] == True]
print(nosza_okulary)

print('=== 2.4 ===')
wiek_20_30 = df0[(df0['Age'] >= 20) & (df0['Age'] <= 30)]
print(wiek_20_30)

print('=== 2.5 ===')
df0['BMI'] = df0.apply(lambda row: round((row['W'] / (row['H'] * row['H']) * 10000), 2), axis=1)
print(df0)

print('=== 2.6 ===')
sredni_wiek = df0['Age'].mean()
print(f'Średni wiek: {sredni_wiek}')

print('=== 2.7 ===')
group_okulary_avg_bmi = df0.groupby('Gl')['BMI'].mean()
print(f'Średnie BMI osób, które noszą okulary: {group_okulary_avg_bmi[True]}')
print(f'Średnie BMI osób, które nie noszą okularów: {group_okulary_avg_bmi[False]}')

print('=== 2.8 ===')
group_okulary_avg_age = df0.groupby('Gl')['Age'].mean()
print(f'Średni wiek osób, które noszą okulary: {round(group_okulary_avg_age[True], 2)}')
print(f'Średni wiek osób, które nie noszą okularów: {group_okulary_avg_age[False]}')

print('=== 3 ===')
f = open('tekst1.txt', 'r+')
s = f.read()
print(s)
print(type(s))
f.close()

with open('tekst1.txt', 'r+') as f:
    s = f.read()
    print(s)
    print(type(s))
    f.close()
