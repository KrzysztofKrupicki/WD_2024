# Krzysztof Krupicki, 175036, Wariant 2

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

print('--- Ćwieczenie 2.1 ---')
nazwa_rzeki = np.array(
    ['Amazonka', 'Nil', 'Jangcy', 'Missisipi-Missouri', 'Huang He', 'Ob Irtysz', 'Kongo', 'Mekong', 'Amur', 'Lena',
     'Parana', 'Mackanzie', 'Niger', 'Jenisej', 'Wołga'])
kontynent = np.array(
    ['Ameryka Południowa', 'Afryka', 'Eurazja', 'Ameryka Północna', 'Eurazja', 'Eurazja', 'Afryka', 'Eurazja',
     'Eurazja', 'Eurazja', 'Ameryka Południowa', 'Ameryka Północna', 'Afryka', 'Eurazja', 'Eurazja'])
dlugosc_km = np.array([7040, 6695, 6300, 6020, 5464, 5410, 4700, 4500, 4440, 4400, 4380, 4240, 4160, 4102, 3530])
powierzchnia_dorzecza_tys_km2 = np.array(
    [7200, 2870, 1807, 3229, 752, 2972, 3690, 810, 1855, 2490, 3100, 1760, 2117, 2580, 1360])
liczba_panstw_przez_ktore_przeplywa = np.array([3, 7, 1, 1, 1, 3, 3, 6, 3, 1, 3, 1, 4, 2, 2])

print(f'Liczba rzek w tabelce: {nazwa_rzeki.size}')
print(f'Rzeki przepływające przez 3 państwa: {nazwa_rzeki[liczba_panstw_przez_ktore_przeplywa == 3]}')
print(f'Ile rzek ma długość mniej niż 5000 km: {nazwa_rzeki[dlugosc_km < 5000].size}')
print(f'Rzeki zaczynające się na literę M: {nazwa_rzeki[np.char.startswith(nazwa_rzeki, 'M')]}')

sort_powierzchnia_desc = np.argsort(powierzchnia_dorzecza_tys_km2)[::-1]
print(f'Nazwy rzek posortowane malejąco według powierzchni: {nazwa_rzeki[sort_powierzchnia_desc]}')

warunek = np.logical_and(powierzchnia_dorzecza_tys_km2 > 2000,
                         np.logical_or(kontynent == 'Ameryka Północna', kontynent == 'Ameryka Południowa'))
print(f'Nazwy rzek z powierzchnią większą niż 2000 tys. km^2 w Ameryce Południowej i Północnej: {nazwa_rzeki[warunek]}')

print('--- Ćwieczenie 2.2 ---')
x = np.linspace(-1, 3, 100)
y1 = np.power(np.e, x)
y2 = np.power(np.e, 2 * x) / 10
fig, ax = plt.subplots(2, 1)
ax[0].plot(x, y1, label='e^x', color='blue')
ax[1].plot(x, y2, label='e^(2x)/10', color='darkgreen', linestyle='--')
ax[0].set_yticks(np.linspace(0, 30, 7))
ax[0].set_ylim(0, 30)
ax[1].set_yticks(np.linspace(0, 30, 7))
ax[1].set_ylim(0, 30)
fig.legend(title='Wykres', loc='center')
plt.tight_layout()
plt.show()

print('--- Ćwieczenie 2.3 ---')
df = pd.read_csv('diamonds.csv')
srednia_cena_diamentow_premium = df.groupby('cut')['price'].mean()['Premium']
print(f'Średnia cena diamentów premium: {srednia_cena_diamentow_premium}')

kolor_diament_e = df[df['color'] == 'E']
najwiekszy_carat = kolor_diament_e[kolor_diament_e['carat'] == kolor_diament_e['carat'].max()]
print(f'Wszystkie informacje o największym carat diamentu koloru E: \n{najwiekszy_carat}')

srednia_cena_diamentow_typ = df.groupby('cut')['price'].mean()
srednia_cena_diamentow_typ.plot(kind='bar')
plt.title('Wykres zależności średniej ceny diamentu od typu')
plt.xlabel('Typ diamentu')
plt.ylabel('Średnia cena')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

d = df[df['color'] == 'D']
e = df[df['color'] == 'E']
f = df[df['color'] == 'F']
g = df[df['color'] == 'G']
h = df[df['color'] == 'H']
i = df[df['color'] == 'I']
j = df[df['color'] == 'J']
plt.scatter(d['carat'], d['price'], c='navy', label='D')
plt.scatter(e['carat'], e['price'], c='yellow', label='E')
plt.scatter(f['carat'], f['price'], c='purple', label='F')
plt.scatter(g['carat'], g['price'], c='green', label='G')
plt.scatter(h['carat'], h['price'], c='black', label='H')
plt.scatter(i['carat'], i['price'], c='orange', label='I')
plt.scatter(j['carat'], j['price'], c='red', label='J')
plt.xlabel('Rozmiar')
plt.ylabel('Cena')
plt.title('Wykres zależności ceny od rozmiaru diamentu')
plt.legend(title='Kolor')
plt.tight_layout()
plt.show()

print('--- Ćwieczenie 2.4 ---')
data = sns.load_dataset('attention')
sns.catplot(data=data, x='subject', y='score', hue='attention', palette='Blues', kind='boxen')
plt.show()
