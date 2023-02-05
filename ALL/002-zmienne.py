# Inicjalizacja zmiennych
# Nazywanie zmiennych snake_case - czyli małe litery i podkreślenia

# Typy danych

# Typ tekstowy
text_type_str = "string"  # str " " - czyli tekst - można użyć apostrofu
text_type_str = 'string'  # str ' ' - czyli tekst - można użyć cudzysłowu
text_type_str = """string " " ' '

string"""  # str """ """ - czyli tekst - niweluje niektóre znaki specjalne

# Typ numeryczny
number_type_int = 1  # int - czyli liczba całkowita
number_type_float = 1.0  # float - czyli liczba zmiennoprzecinkowa
number_type_complex = 1j  # complex - czyli liczba zespolona

# Typ sekwencyjny
sequence_type_list = [1, 2, 3]  # list - czyli lista, która może być zmieniona
sequence_type_tuple = (1, 2, 3)  # tuple - czyli krotka, która nie może być zmieniona
sequence_type_list = 1, 2, 3  # tuple - czyli krotka, która nie może być zmieniona
sequence_type_range = range(1, 10)  # range - czyli zakres liczb

# Typ mapowania
# dict - czyli słownik, który ma klucze i wartości
mapping_type_dict = {1: "a", 2: "b", 3: "c"}

# Typ zbioru
# set - czyli lista, która nie może być zmieniona i nie ma duplikatów
set_type_set = {1, 2, 3}
# frozenset - czyli lista, która nie może być zmieniona i nie ma duplikatów
set_type_frozenset = frozenset({1, 2, 3})

# Typ logiczny
logical_type_bool = True  # bool - czyli wartość logiczna True lub False

# Typ binarny
binary_type_bytes = b"1"  # bytes - czyli ciąg bajtów
binary_type_bytearray = bytearray(1)  # bytearray - czyli tablica bajtów
# memoryview - czyli widok pamięci
binary_type_memoryview = memoryview(bytes(1))

# Typ specjalny
special_type_none = None  # NoneType - czyli brak wartości






# Listy i tablice w Pythonie

# W języku Python, lista i tablica różnią się między sobą następująco:

# Dynamiczność vs Statyczność: Listy są dynamiczne, co oznacza, że można łatwo dodawać lub usuwać elementy z listy w czasie działania programu. Natomiast tablice są statyczne, co oznacza, że nie można łatwo zmieniać rozmiaru tablicy po jej utworzeniu.

# Typy danych: Listy w Pythonie mogą przechowywać elementy różnego typu danych, takie jak liczby, łańcuchy znaków, inne listy itp. Tablice w NumPy muszą przechowywać elementy tego samego typu danych.

# Wydajność: Tablice są bardziej wydajne niż listy, ponieważ dane są przechowywane w jednej płaskiej tablicy w pamięci, co umożliwia szybki dostęp do danych. Listy natomiast są implementowane jako sekwencje powiązanych list, co może powodować spowolnienie w przypadku dużych danych.

# Lista
my_list = [1, 2, 3, 4, 5]
my_list.append(6)  # Dodaj element 6 do listy
my_list[2] = 10  # Zmień wartość elementu o indeksie 2 na 10

# Tablica z NumPy
import numpy as np
my_array = np.array([1, 2, 3, 4, 5])
my_array = np.append(my_array, [6])  # Dodaj element 6 do tablicy
my_array[2] = 10  # Zmień wartość elementu o indeksie 2 na 10
