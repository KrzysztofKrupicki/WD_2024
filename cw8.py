import numpy as np

"""
Zadanie 2
"""

print('=== 1.0 ===')
my_array = np.arange(10, 39, 2)
print(my_array)

print('=== 1.1 ===')
print(f'shape: {my_array.shape}')

print('=== 1.2 ===')
new1 = np.resize(my_array, (6, 2))
print(f'new1 shape: {new1.shape}')
print(new1)
new2 = np.reshape(my_array, (3, 5))
print(f'new2 shape: {new2.shape}')
print(new2)

print('=== 1.3 ===')
print(f'my_array + 3: {my_array + 3}')

print('=== 1.4 ===')
print(f'my_array * 2: {my_array * 2}')

print('=== 1.5 ===')
my_array[my_array % 6 == 2] = 0
print(f'my_array % 6 == 2 -> 0: {my_array}')

print('=== 1.6 ===')


def change(A, x):
    new_array = np.copy(A)
    new_array[new_array == 0] = x
    return new_array


test = np.array([0, 2, 54, 9, 2, 0, 1])
print(change(test, 13))
print(test)

"""
Zadanie 2
"""

print('=== 2.1 ===')
A = np.array([[1, 1, 2], [2, 1, 0], [4, 1, 2]])
B = np.array([[2, 5, 7], [2, 8, 0], [4, 3, 1]])
print(f'A: \n{A}')
print(f'B: \n{B}')
print(f'A + B = \n{A + B}')
print(f'A dot B = \n{np.dot(A, B)}')  # iloczyn macierzowy
print(f'A @ B = \n{A @ B}')  # iloczyn macierzowy
print(f'A multiply B = \n{np.multiply(A, B)}')  # iloczyn po-elementowy
print(f'A * B = \n{A * B}')  # iloczyn po-elementowy
print(f'A^T = \n{A.T}')
print(f'A^-1 = \n{np.linalg.inv(A)}')
print(f'A^5 = \n{np.linalg.matrix_power(A, 5)}')
print(f'elementy A do ^5 = \n{A ** 5}')
print(f'det B = {np.linalg.det(B)}')
print(f'B^-3 = \n{np.linalg.matrix_power(B, -3)}')

print('=== 2.2 ===')
C = np.array([[1], [2], [4]])
D = np.array([[2, 5, 7]])
print(f'C: \n{C}')
print(f'D: \n{D}')
print(f'C @ D: \n{C @ D}')
print(f'D @ C: \n{D @ C}')
print(f'C * D: \n{C * D}')  # wynik to C @ D - iloczyn macierzowy
print(f'C + D: \n{C + D}')  # nie da sie, ale zadzialał broadcasting

print('=== 2.3 ===')
E = np.array([[1, 5], [2, 1]])
F = np.array([[2, 1], [2, 8]])
print(f'E: \n{E}')
print(f'F: \n{F}')
print(f'E / F: \n{E / F}')
print(f'E // F: \n{E // F}')
print(f'E % F: \n{E % F}')

"""
Zadanie 3
"""

panstwa = np.array(["China", "Japan", "Germany", "USA", "South Korea", "India", "Brazil", "Mexico", "Spain", "Russia"])
rok1999 = np.array([0.56, 8.1, 5.3, 5.63, 2.36, 0.53, 1.1, 0.99, 2.28, 0.94])
rok2014 = np.array([19.91, 8.27, 5.6, 4.25, 4.12, 3.15, 2.31, 1.91, 1.89, 1.69])

print('=== 3.1 ===')
wzrost = np.around((rok2014 - rok1999) / rok1999 * 100, 2)
print(f'Procent wzrostu produkcji:\n{np.column_stack([panstwa, wzrost])}')

print('=== 3.2 ===')
print(f'Min 1999: {panstwa[np.argmin(rok1999)]}')
print(f'Max 1999: {panstwa[np.argmax(rok1999)]}')
print(f'Min 2014: {panstwa[np.argmin(rok2014)]}')
print(f'Max 2014: {panstwa[np.argmax(rok2014)]}')

print('=== 3.3 ===')
print(f'W 2014 mniej niż w 1999: {panstwa[rok2014 < rok1999]}')

"""
Zadanie 4
"""

imiona = np.array(["Anna", "Zofia", "Sylwia", "Katarzyna", "Teresa", "Tomasz", "Cezary", "Zenon", "Filip", "Adrian"])
wiek = np.array([21, 40, 13, 31, 34, 14, 13, 28, 20, 15])
plec = np.array(["K", "K", "K", "K", "K", "M", "M", "M", "M", "M"])
waga = np.array([65, 80, 64, 69, 74, 61, 66, 61, 69, 77])
wzrost = np.array([179, 179, 151, 177, 170, 157, 151, 513, 160, 160])
okulary = np.array(["NIE", "TAK", "NIE", "TAK", "NIE", "TAK", "NIE", "TAK", "NIE", "TAK"])

print('=== 4.1 ===')
print(f'Posortowane imiona:\n{np.sort(imiona)}')

print('=== 4.2 ===')
nosza_okulary = okulary == "TAK"
print(f'Noszą okulary:\n{imiona[nosza_okulary]}')

print('=== 4.3 ===')
czy_kobieta = plec == "K"
imiona_20_30_lat = np.logical_and(wiek >= 20, wiek <= 30)
print(f'Imiona kobiet w wieku [20, 30]:\n{imiona[np.logical_and(czy_kobieta, imiona_20_30_lat)]}')

print('=== 4.4 ===')
waga_60_80 = np.logical_and(waga >= 60, waga <= 80)
wzrost_160_180 = np.logical_and(wzrost >= 160, wzrost <= 180)
okulary_nie = okulary == "NIE"
print(f'Imiona osób o wadze [60, 80] i wzroście [160, 180] nienoszących okularów:\n'
      f'{imiona[np.logical_and.reduce((waga_60_80, wzrost_160_180, okulary_nie))]}')

print('=== 4.5 ===')
bmi = np.around(waga / wzrost ** 2 * 10000, decimals=2)
print(f'Bmi:\n{bmi}')

print('=== 4.6 ===')
avg_wiek = np.mean(wiek)
imie_bliskie_avg_wiek = np.argmin(np.abs(wiek - avg_wiek))
print(f'Średni wiek {avg_wiek}, imie osoby najbliżej średniej {imiona[imie_bliskie_avg_wiek]}')

"""
Zadanie 5
"""

height = np.array(
    [153, 154, 154, 155, 158, 159, 160, 161, 163, 164, 165, 165, 165, 166, 167, 167, 168, 168, 170, 170, 170, 171, 173,
     174, 174, 174, 175, 175, 176, 177, 178, 178, 178, 179, 179, 179, 180, 180, 183, 185])
shoe_size = np.array(
    [5, 6, 6, 6, 5, 7, 6, 5, 6, 7, 7, 6, 7, 10, 9.5, 10, 10, 9, 10.5, 9.5, 8.5, 9, 10, 8, 10, 9, 12, 11, 9, 10, 11, 11,
     12, 10.5, 11.5, 11, 13, 12, 12.5, 13])

print('=== 5.1 ===')
avg_shoe_size = np.mean(shoe_size)
print(f'Średni rozmiar buta: {avg_shoe_size}')

print('=== 5.2 ===')
max_shoe_size = np.max(shoe_size)
print(f'Maksymalny rozmiar buta: {max_shoe_size}')

print('=== 5.3 ===')
max_shoe_size_students = np.where(shoe_size == max_shoe_size)
avg_height_of_max_shoe_size = np.mean(height[max_shoe_size_students])
print(f'Średni wzrost osób z maksymalnym rozmiarem buta: {avg_height_of_max_shoe_size}')

print('=== 5.4 ===')
min_height_of_max_shoe_size = np.min(height[max_shoe_size_students])
print(f'Najmniejszy wzrost osób z maksymalnym rozmiarem buta: {min_height_of_max_shoe_size}')

print('=== 5.5 ===')
unique_heights = np.unique(height)
for hh in unique_heights:
    avg_shoe_size = np.mean(shoe_size[height == hh])
    print(f'{hh} cm - {avg_shoe_size:.2f}')

print('=== 5.6 ===')
for hh in unique_heights:
    avg_height = np.mean(height[height == hh])
    print(f'{hh} cm - {avg_height:.2f}')

print('=== 5.7 ===')
min_shoe_size_10 = np.min(height[shoe_size == 10])
max_shoe_size_10 = np.max(height[shoe_size == 10])
print(f'Min: {min_shoe_size_10}')
print(f'Max: {max_shoe_size_10}')

print('=== 5.8 ===')
european_shoe_size = np.copy(shoe_size + 33)
print(f'Europejskie rozmiary butów:\n{european_shoe_size}')