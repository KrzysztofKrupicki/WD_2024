import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x1 = [27.2, 8.8, 28.1, 21.1, 14.9]
x2 = [25.7, 21.2, 13.4, 12.8, 26.8]
labels = ['A', 'B', 'C', 'D', 'E']
c1 = ['grey', 'oldlace', 'palegoldenrod', 'firebrick', 'khaki']
c2 = ['turquoise', 'orange', 'goldenrod', 'forestgreen', 'firebrick']
fig, ax = plt.subplots(2, 1)
ax[0].pie(x1, labels=labels, colors=c1, explode=[0, 0.05, 0, 0, 0], autopct="%1.1f%%", startangle=30, shadow=True)
ax[0].set_title("Tytuł 1")
ax[1].pie(x2, labels=labels, colors=c2, explode=[0, 0.1, 0, 0, 0], autopct="%1.1f%%", startangle=30, shadow=True)
ax[1].set_title("Tytuł 2")
ax[0].axis('equal')
ax[1].axis('equal')
plt.tight_layout()
# plt.savefig("wykres1.svg")
plt.show()

df = pd.read_excel("ceny02.xlsx")
jablka = df[df["Rodzaje towarów i usług"] == "jabłka - za 1kg"]
cytryny = df[df["Rodzaje towarów i usług"] == "cytryny - za 1 kg"]
plt.plot(jablka["Miesiące"], jablka["Wartosc"], linestyle='dashed', linewidth=3, label="jabłka")
plt.plot(cytryny["Miesiące"], cytryny["Wartosc"], linestyle='dotted', linewidth=2, label="cytryny")
plt.title("Wykres liniowy zmienności cen jabłek i cytryn")
plt.xlabel("Miesiące")
plt.ylabel("Cena")
plt.xticks(rotation=45)
plt.annotate("Najwyższy punkt", xy=("sierpień", 14), xytext=(4, 8), arrowprops=dict(facecolor='blue'))
plt.legend()
plt.tight_layout()
# plt.savefig("wykres2.webp")
plt.show()

data = pd.read_excel("samochody02.xlsx", header=None).T
data[1] = data[1].astype(int)
data[2] = data[2].astype(int)
pogroup = data.groupby([0, 1])[2].sum().unstack()
print(pogroup)
pogroup.plot(kind='bar')
plt.xticks(rotation=45)
plt.xlabel("Typ pojazdu")
plt.ylabel("Ilość")
plt.legend(title="Rok")
plt.title("Wykres słupkowy ilości pojazdów w latach 2017 i 2018")
plt.tight_layout()
# plt.savefig("wykres3.png")
plt.show()
