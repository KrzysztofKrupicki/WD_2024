import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x1 = [11, 12, 13, 15, 36, 40]
y1 = [30, 12, 3, 5, 7, 28]
x2 = [11, 12, 13, 15, 36, 40]
y2 = [25, 48, 42, 26, 39, 32]
plt.scatter(x1, y1, color='red', marker='p', label='pięciokąty', s=100)
plt.scatter(x2, y2, color='blue', marker='x', label='krzyżyki', s=100)
plt.title("Wykres punktowy - 2 x 6 punktów")
plt.xticks(np.arange(10, 45, 5))
plt.yticks(np.arange(0, 50, 10))
plt.ylim(1, 50)
plt.grid()
plt.legend()
plt.tight_layout()
# plt.savefig("wykres1.tiff")
plt.show()

df = pd.read_excel("sprzedaz03.xlsx")
jablka = df[df["Produkt"] == "Jabłka"]
gruszki = df[df["Produkt"] == "Gruszki"]
morele = df[df["Produkt"] == "Morele"]
plt.bar(jablka['Rok'] - 0.25, jablka['Sprzedaż'], color='forestgreen', label='jabłka', width=0.25)
plt.bar(gruszki['Rok'], gruszki['Sprzedaż'], color='violet', label='gruszki', width=0.25)
plt.bar(morele['Rok'] + 0.25, morele['Sprzedaż'], color='khaki', label='morele', width=0.25)
plt.title("Ilość sprzedanych owoców w latach 2015-2017")
plt.xticks(np.arange(2015, 2018))
plt.xlabel("Rok")
plt.ylabel("Ilość")
plt.legend()
plt.grid()
plt.annotate("", xy=(2015.25, 0), xytext=(2015.5, 500), arrowprops=dict(facecolor='pink'))
plt.tight_layout()
# plt.savefig("wykres2.pdf")
plt.show()

data = pd.read_excel("sady03.xlsx", header=None).T
data[1] = data[1].astype(int)
data[3] = data[3].astype(int)
dane = data[3]
rok = data[1]
explode = [0.2, 0, 0, 0, 0, 0]
plt.pie(dane, explode=explode, startangle=125, colors=['grey', 'orange', 'lime', 'pink', 'aqua', 'firebrick'], pctdistance=0.85, autopct="%1.1f%%")
circle = plt.Circle((0,0), 0.75, color='white')
p = plt.gcf()
p.gca().add_artist(circle)
plt.title("Wykres pierścieniowy")
plt.legend(rok, title="Rok", bbox_to_anchor=(0, .5), loc="right")
plt.tight_layout()
# plt.savefig("wykres3.png")
plt.show()