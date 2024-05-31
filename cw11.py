import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('penguins.csv')

print('=== 1.1 ===')
print(data.groupby(['sex', 'species'])['body_mass_g'].mean())

print('=== 1.2 ===')
print('Max waga:')
print(data[data['body_mass_g'] == data['body_mass_g'].max()])
print('Min waga:')
print(data[data['body_mass_g'] == data['body_mass_g'].min()])

print('=== 1.3 ===')
print(data.groupby(['island', 'species']).size())

print('=== 1.4 ===')
print(data[data['species'] == 'Adelie'].groupby(['species', 'island']).size())

print('=== 1.5 ===')
nazwy_wysp = data.groupby(['island']).size().index.tolist()
ilosc_pingwinow = data.groupby(['island']).size().tolist()
plt.bar(nazwy_wysp, ilosc_pingwinow)
plt.show()

print('=== 1.6 ===')
szerokosci_dzioba = data['bill_depth_mm']
dlugosci_dzioba = data['bill_length_mm']
plt.scatter(dlugosci_dzioba, szerokosci_dzioba)
plt.xlabel('bill_length_mm')
plt.ylabel('bill_depth_mm')
plt.show()

print('=== 1.7 ===')
kolory = np.where(data['sex'] == 'MALE', 'b', 'r').tolist()
waga_rozmiar = np.where(data['body_mass_g'].isna(), 0, ((data['body_mass_g'] / 2000) ** 5).astype(float)).tolist()
symbol = ['<', 's', 'o']
gatunki = np.copy(data['species']).tolist()
unikalne_gatunki_symbole = dict(zip(np.unique(gatunki), symbol))
for i in range(len(gatunki)):
    gatunki[i] = unikalne_gatunki_symbole[gatunki[i]]
for i in range(len(waga_rozmiar)):
    plt.scatter(data['bill_length_mm'][i], data['bill_depth_mm'][i], c=kolory[i], s=waga_rozmiar[i], marker=gatunki[i])
plt.xlabel('bill_length_mm')
plt.ylabel('bill_depth_mm')
plt.show()

print('=== 2 ===')
penguins = sns.load_dataset('penguins')
sns.relplot(data=penguins, x='bill_length_mm', y='bill_depth_mm', hue='sex', size='body_mass_g', markers='species')
plt.show()

print('=== 3.1 ===')
iris = sns.load_dataset('iris')
sns.catplot(iris, x='species', y='sepal_length', hue='species')
plt.title('Sepal Length')
plt.tight_layout()
plt.show()
sns.catplot(iris, x='species', y='petal_width', hue='species')
plt.title('Petal Width')
plt.tight_layout()
plt.show()

print('=== 3.2 ===')
sns.pairplot(iris, hue='species')
plt.show()
