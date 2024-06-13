import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x1 = [10.80, 32.22, 29.99, 17.19, 9.80]
x2 = [13.5, 23.7, 28.8, 23.1, 10.9]
label = ['a', 'b', 'c', 'd', 'e']
c = ['grey', 'saddlebrown', 'cyan', 'mediumorchid', 'orange']
fig, ax = plt.subplots(2, 1)
ax[0].pie(x1, labels=label, colors=c, explode=[0, 0, 0.2, 0, 0], startangle=40, autopct="%1.2f%%")
ax[1].pie(x2, labels=label, colors=c, explode=[0, 0, 0.2, 0, 0.05], startangle=30, autopct="%1.1f%%")
plt.tight_layout()
# plt.savefig("wykres1.webp")
plt.show()

df = pd.read_excel('ceny5.xlsx')
pstrag = df[df["Rodzaje produktów"] == "pstrąg świeży niepatroszony - za 1 kg"]
morszczuk = df[df["Rodzaje produktów"] == "filety z morszczuka mrożone - za 1kg"]
sledz = df[df["Rodzaje produktów"] == "śledź solony, niepatroszony - za 1kg"]
plt.scatter(pstrag["Rok"], pstrag["Wartosc"], marker='x', color='pink', label='pstrąg świeży niepatroszony', s=100)
plt.scatter(morszczuk["Rok"], morszczuk["Wartosc"], marker='p', color='cyan', label='filety z morszczuka mrożone',
            s=125)
plt.scatter(sledz["Rok"], sledz["Wartosc"], marker='>', color='forestgreen', label='śledź solony, niepatroszony', s=75)
plt.title("Wykres cenowy wybranych ryb za 1kg")
plt.xlabel("Rok")
plt.ylabel("Wartość")
plt.grid()
plt.text(1, 1, "XXXXXX", transform=plt.gcf().transFigure, ha='right', va='top')
plt.legend()
plt.tight_layout()
# plt.savefig("wykres2.png")
plt.show()

data = pd.read_csv('cechy5.csv', sep=';')
data = data.replace(',', '.', regex=True)
data["Cecha1"] = data["Cecha1"].astype(float)
data["Cecha2"] = data["Cecha2"].astype(float)
plt.hist(data["Cecha1"], bins=6, edgecolor='black', alpha=0.75)
plt.title("Histogram pierwszej cechy podzielonej na 6 koszyków")
plt.xlabel("Wartość cechy")
plt.ylabel("Liczba obserwacji")
plt.grid()
plt.legend(['Pierwsza cecha'])
plt.tight_layout()
# plt.savefig('wykres3.jpg')
plt.show()
