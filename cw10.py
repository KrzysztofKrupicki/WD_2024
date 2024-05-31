import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

print('=== 1 ===')
# f = open('tekst1.txt', 'r+')
# s = f.read()
# print(s)
# print(type(s))
# f.close()

# with open('tekst1.txt', 'a', encoding='utf-8') as f:
#     s = f.read()
#     f.write('\ndopisek3')  # dopis mozliwy w r+ (dopis i zapis), w (nadpis), x (nowy plik i zapis), a (dopis na koncu)
#     print(s)
#     f.close()

print('=== 2.1 ===')
data = np.genfromtxt('jajka2024.csv', delimiter=';', dtype='|U16', encoding='utf8')
data[data == ''] = np.nan
miasta = data[0, 1:]
sklepy = data[1:, 0]
ceny = data[1:, 1:].astype(float)
print(f'Średnia cena: {np.nanmean(ceny)}')

print('=== 2.2 ===')
najtansze = np.unravel_index(np.nanargmin(ceny), ceny.shape)
najdrozsze = np.unravel_index(np.nanargmax(ceny), ceny.shape)
wynik_najtansze = [miasta[najtansze[1]], sklepy[najtansze[0]]]
wynik_najdrozsze = [miasta[najdrozsze[1]], sklepy[najdrozsze[0]]]
print(f'Najtańsze: {wynik_najtansze}')
print(f'Najdroższe: {wynik_najdrozsze}')

print('=== 3 ===')
data = pd.read_csv('jajka2024.csv', sep=';', index_col=0, encoding='utf-8')
print(f'data:\n{data}')
data2 = data.stack()
print(f'\ndata2:\n{data2}')
data3 = data2.replace(',', '.').astype(float)
print(f'\ndata3:\n{data3}')
srednia = data3.mean()
minCena = data3.min()
maxCena = data3.max()
print(srednia)
print(data3[data3 == minCena])
print(data3[data3 == maxCena])

df = pd.DataFrame(data)
sklepy = df.index.values.tolist()
miasta = df.columns.values.tolist()

plt.figure(figsize=(10, 10))
data.boxplot(column=miasta, grid=False)
plt.title('Miasta')
plt.xlabel('Miasto')
plt.ylabel('Cena')

plt.figure(figsize=(10, 10))
data.T.boxplot(column=sklepy, grid=False)
plt.title('Sklepy')
plt.xlabel('Sklep')
plt.ylabel('Cena')
plt.xticks(rotation=45)
plt.show()
