import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x1 = [-45, -40, -50, -30, -25, -50]
x2 = [10, 2, 25, 40, 37, 26]
y = ['Czerwiec', 'Maj', 'Kwiecień', 'Marzec', 'Luty', 'Styczeń']
c = ['darkturquoise']
plt.barh(y[::-1], x2[::-1], color='violet', label='A')
plt.barh(y[::-1], x1[::-1], color='darkturquoise', label='B')
plt.title("Wykres zmian A i B")
plt.legend()
plt.yticks(rotation=30)
plt.tight_layout()
# plt.savefig("wykres1.tiff")
plt.show()

df = pd.read_excel("linieautobusowe4.xlsx")
rok = df["Rok"]
wartosci = df["Wartosc"]
plt.pie(wartosci, colors=['pink', 'grey', 'forestgreen', 'cyan', 'firebrick'], autopct="%1.1f%%",
        explode=[0.2, 0, 0, 0, 0], pctdistance=1.2)
circle = plt.Circle((0, 0), 0.7, color='white')
p = plt.gcf()
p.gca().add_artist(circle)
plt.title("Wykres pierścieniowy")
plt.annotate("", xy=(0.75, 0.75), xytext=(1, 1.25), arrowprops=dict(facecolor="violet"))
plt.legend(rok, loc='right', bbox_to_anchor=(-0.05, 0.5))
plt.tight_layout()
# plt.savefig("wykres2.jpg")
plt.show()

data = pd.read_csv('hotele4.csv', sep='#')
data = data.melt(["Nazwa"], var_name="Rok", value_name="Liczba")
pomorskie = data[data["Nazwa"] == "POMORSKIE"]
kujawsko_pomorskie = data[data["Nazwa"] == "KUJAWSKO-POMORSKIE"]
lubelskie = data[data["Nazwa"] == "LUBELSKIE"]
lubuskie = data[data["Nazwa"] == "LUBUSKIE"]
lodzkie = data[data["Nazwa"] == "ŁÓDZKIE"]
plt.scatter(pomorskie["Rok"], pomorskie["Liczba"], marker='p', color='violet', label='pomorskie')
plt.scatter(kujawsko_pomorskie["Rok"], kujawsko_pomorskie["Liczba"], marker='^', color='orange', label='kujawsko-pomorskie')
plt.scatter(lubelskie["Rok"], lubelskie["Liczba"], marker='P', color='forestgreen', label='lubelskie')
plt.scatter(lubuskie["Rok"], lubuskie["Liczba"], marker='x', color='cyan', label='lubuskie')
plt.scatter(lodzkie["Rok"], lodzkie["Liczba"], marker='<', color='grey', label='łódzkie')
plt.legend(title="Wojewodztwo")
plt.title("Wykres ilości hoteli w wybranych województwach")
plt.xlabel("Rok")
plt.ylabel("Liczba")
plt.tight_layout()
# plt.savefig("wykres3.png")
plt.show()

