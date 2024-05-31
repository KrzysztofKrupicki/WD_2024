import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Zadanie 1
x = np.linspace(-4, 4, 100)
y = np.sin(2 * x)
y1 = 2 * np.sin(x)
y2 = np.sin(x)
plt.plot(x, y2, 'blue', linestyle='-', label='sin(x)')
plt.plot(x, y1, 'red', linestyle=':', label='2sin(x)')
plt.plot(x, y, 'green', linestyle='--', label='sin(2x)')
plt.legend(title='Wykres')
plt.show()

# Zadanie 2.1
x = np.linspace(-10, 10, 100)
y = 1 / (1 + x ** 2)
plt.plot(x, y, 'green', linestyle='-', label='1/(1+x^2)')
plt.legend(title='Wykres')
plt.show()

# Zadanie 2.2
x = np.linspace(0, 3, 100)
y1 = np.power(x, 2)
y2 = np.power(np.e, x)
y3 = np.power(x, x)
plt.plot(x, y1, 'green', linestyle='--', label='x^2')
plt.plot(x, y2, 'red', linestyle=':', label='e^x')
plt.plot(x, y3, 'blue', linestyle='-', label='x^x')
plt.legend(title='Wykres')
plt.show()

x = np.linspace(0, 4, 100)
y1 = np.power(x, 2)
y2 = np.power(np.e, x)
y3 = np.power(x, x)
plt.plot(x, y1, 'green', linestyle='--', label='x^2')
plt.plot(x, y2, 'red', linestyle=':', label='e^x')
plt.plot(x, y3, 'blue', linestyle='-', label='x^x')
plt.legend(title='Wykres')
plt.show()

# Zadanie 2.3
x = np.linspace(0, 4, 100)
fig, ax = plt.subplots(3, 1)
y1 = np.power(x, 2)
y2 = np.power(np.e, x)
y3 = np.power(x, x)
ax[0].plot(x, y1, 'green', linestyle='--', label='x^2')
ax[1].plot(x, y2, 'red', linestyle=':', label='e^x')
ax[2].plot(x, y3, 'blue', linestyle='-', label='x^x')
fig.legend(title='Wykres', loc='upper center')
plt.show()

x = np.linspace(0, 3, 100)
fig, ax = plt.subplots(3, 1)
y1 = np.power(x, 2)
y2 = np.power(np.e, x)
y3 = np.power(x, x)
ax[0].plot(x, y1, 'green', linestyle='--', label='x^2')
ax[0].set_ylim(0, 20)
ax[1].plot(x, y2, 'red', linestyle=':', label='e^x')
ax[1].set_ylim(0, 20)
ax[2].plot(x, y3, 'blue', linestyle='-', label='x^x')
ax[2].set_ylim(0, 20)
fig.legend(title='Wykres', loc='upper center')
plt.show()


# Zadanie 3

def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 5):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)


sns.set_style('whitegrid')
sns.set_palette('husl')
sinplot()
print(sns.axes_style())
plt.show()
# zmienil sie tyl wykresu i paleta barw, na konsoli wyswietlilo aktualne ustawienia stylizacji

# Zadanie 3.1
x1 = np.linspace(-2, 2, 100)
y1 = x1
y2 = x1 ** 2
y3 = x1 ** 3
x2 = np.linspace(0, 2)
y4 = x2 ** (1 / 2)
y5 = x2 ** (1 / 3)
sns.lineplot(x=x1, y=y1, color='blue', label='x')
sns.lineplot(x=x1, y=y2, color='orange', label='x^2')
sns.lineplot(x=x1, y=y3, color='green', label='x^3')
sns.lineplot(x=x2, y=y4, color='red', label='sqrt(x)')
sns.lineplot(x=x2, y=y5, color='purple', label='x^(1/3)')
plt.legend(title='Wykres')
plt.grid(color='white')
plt.gca().set_facecolor('lavender')
plt.show()

# Zadanie 4
data = sns.load_dataset('glue')
sns.catplot(data=data, x='Year', y='Score', col='Model', hue='Encoder', kind='violin', palette=['orange', 'green'],
            height=4, aspect=0.5)
plt.show()
