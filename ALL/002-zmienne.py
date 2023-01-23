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
sequence_type_tuple = (1, 2, 3)  # tuple - czyli lista, która nie moż
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