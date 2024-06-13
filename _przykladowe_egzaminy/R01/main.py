import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

y1 = [48, 60, 65, 65, 60]
y2 = [52, 55, 48, 40, 46]
x = ['Olsztyn', 'Gdańsk', 'Toruń', 'Warszawa', 'Kraków']
c1 = ['darkviolet', 'darkviolet', 'royalblue', 'silver', 'rebeccapurple']
c2 = ['violet', 'sienna', 'forestgreen', 'saddlebrown', 'beige']
plt.bar(x, y1, color=c2)
plt.bar(x, y2, color=c1, bottom=y1)
plt.title("Wykres słupkowy pogrupowany")
plt.yticks(np.linspace(0, 150, 16))
plt.ylabel("Wartości")
plt.xticks(rotation=45)
plt.legend(['A', 'B'])
plt.tight_layout()
# plt.savefig("wykres1.webp")
plt.show()

df = pd.read_excel("parki01.xlsx")
lodzkie = df[df["Nazwa"] == "ŁÓDZKIE"]
slaskie = df[df["Nazwa"] == "ŚLĄSKIE"]
podkarpackie = df[df["Nazwa"] == "PODKARPACKIE"]
plt.plot(lodzkie['Rok'], lodzkie['Wartosc'], linestyle='dashed', linewidth=2, color='pink', label='łódzkie')
plt.plot(slaskie['Rok'], slaskie['Wartosc'], linestyle='dotted', linewidth=2, color='forestgreen', label='śląskie')
plt.plot(podkarpackie['Rok'], podkarpackie['Wartosc'], linestyle='dashdot', linewidth=2, color='sienna', label='podkarpackie')
plt.ylabel("Wartość")
plt.xlabel("Rok")
plt.xticks(np.arange(2015, 2018))
plt.title("Wykres wartości terenów zielonych w danych województwach")
plt.legend()
plt.grid()
plt.text(1, 1, "DD/MM/YYYY", transform=plt.gcf().transFigure, va='top', ha='right')
plt.tight_layout()
# plt.savefig("wykres2.svg")
plt.show()

df2 = pd.read_csv('medale01.csv', sep=';')
fig, ax = plt.subplots(1, 2)
letnie = df2[df2["Rodzaj"] == 'Letnie']
zimowe = df2[df2["Rodzaj"] == 'Zimowe']
ax[0].pie(letnie["Brązowe"], autopct="%1.0f%%", labels=letnie["Rok"])
ax[1].pie(zimowe["Brązowe"], autopct="%1.0f%%", labels=zimowe["Rok"])
ax[0].set_title("Olimpiady letnie")
ax[1].set_title("Olimpiady zimowe")
plt.suptitle("Brązowe medale za olimpiady", fontsize=18)
plt.tight_layout()
# plt.savefig("wykres3.png")
plt.show()
