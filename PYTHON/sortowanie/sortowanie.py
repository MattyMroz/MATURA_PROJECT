# W Pythonie istnieją kilka sposobów na sortowanie:

# 2 podstawowe metody sortowania listy:
# arr.sort() - sortuje listę - zamienia listę na posortowaną
# sorted(arr) - zwraca posortowaną kopię listy

# atrybuty sortowania:
# key - funkcja, która określa klucz sortowania
# reverse - określa, czy sortowanie ma być w kolejności rosnącej (domyślnie) czy malejącej
# lembda - funkcja anonimowa, która określa klucz sortowania

# wartości dla kay i reverse:
# key = None - domyślnie sortuje według wartości elementów
# key = lembda x: x[0] - sortuje według pierwszego elementu w każdym elemencie listy (np. listy list)
# kay=len - sortuje według długości elementów
# kay=abs - sortuje według wartości bezwzględnej elementów
# reverse = False - domyślnie sortuje w kolejności rosnącej
# reverse = True - sortuje w kolejności malejącej


# sortowanie listy metodą sort(): jest to najprostszy i najszybszy sposób na sortowanie listy, np. list.sort(). Można także ustawić klucz sortowania za pomocą argumentu key, a także ustawić, czy sortowanie ma być w kolejności rosnącej czy malejącej, używając argumentu reverse.

# sortowanie listy funkcją sorted(): jest to bardziej uniwersalna metoda sortowania, która zwraca posortowaną kopię listy, np. sorted(list). Podobnie jak metoda sort(), można ustawić klucz sortowania oraz kolejność sortowania.

# sortowanie za pomocą funkcji sortującej w wyrażeniach lambda: jest to metoda sortowania z użyciem funkcji lambda, np. list.sort(key=lambda x: x[0]).

# sortowanie przy użyciu funkcji operator.itemgetter(): jest to sposób sortowania listy obiektów, np. listy słowników, według wybranego atrybutu, np. sorted(list, key=operator.itemgetter('name')).

# sortowanie przy użyciu funkcji sorted() i funkcji sortującej: jest to metoda polegająca na użyciu funkcji sortującej jako argumentu funkcji sorted(), np. sorted(list, key=sort_function).

# a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# sorted(a)
# [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# a.sort()
# print(a)
# [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# a = [(1, 2), (3, 1), (4, 4)]
# sorted(a, key=lambda x: x[1])
# [(3, 1), (1, 2), (4, 4)]

# a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
# sorted(a, reverse=True)
# [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]


list_1 = [24, 1, 8, 23, 17, 15, 5, 7, 14, 16, 4,
          6, 13, 20, 3, 18, 19, 10, 21, 12, 2, 11, 9, 22]
list_2 = ['alfa', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda',
          'mu', 'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega']


list_list = [['alfa', 1], ['beta', 2], ['gamma', 3], ['delta', 4], ['epsilon', 5], ['zeta', 6], ['eta', 7], ['theta', 8], ['iota', 9], ['kappa', 10], ['lambda', 11], [
    'mu', 12], ['nu', 13], ['xi', 14], ['omicron', 15], ['pi', 16], ['rho', 17], ['sigma', 18], ['tau', 19], ['upsilon', 20], ['phi', 21], ['chi', 22], ['psi', 23], ['omega', 24]]

list_tuple = [('alfa', 1), ('beta', 2), ('gamma', 3), ('delta', 4), ('epsilon', 5), ('zeta', 6), ('eta', 7), ('theta', 8), ('iota', 9), ('kappa', 10), ('lambda', 11), ('mu', 12),
              ('nu', 13), ('xi', 14), ('omicron', 15), ('pi', 16), ('rho', 17), ('sigma', 18), ('tau', 19), ('upsilon', 20), ('phi', 21), ('chi', 22), ('psi', 23), ('omega', 24)]


list_1.sort()
print(".sort(): ", list_1, '\n')

list_2.sort()
print(".sort(): ", list_2, '\n')

# sortowanie dłgości słów
list_2.sort(key=len)  # sortowanie w miejscu
print(".sort(key=len): ", list_2, '\n')
# sorted nie zmienia listy, tylko zwraca posortowaną listę
list_2 = sorted(list_2, reverse=True, key=len)
print("sorted(list_2, reverse=True, key=len): ", list_2, '\n')

# sortowanie tablicy dwuwymiarowej po pierwszej kolumnie
print("list_list: ", list_list, '\n')
print("sorted(list_list, key=lambda x: x[0]): ", sorted(
    list_list, key=lambda x: x[0]), '\n')

# sortowanie tablicy po liczbie jedności
list_3 = [12, 20, 3, 23, 50, 234, 64, 75]
print("Sortowanie po liczbie jesdności: sorted(list_3, key=lambda x: x % 10): ",
      sorted(list_3, key=lambda x: x % 10), '\n')

names = ['algorytm sortowania przez wybieranie', 'algorytm rekurencyjny', 'algorytm iteracyjny', 'algorytm sortowania przez wstawianie', 'algorytm sortowania przez prosta zamiane',
         'algorytm naiwny', 'algorytm obliczania silni iteracyjny', 'algorytm obliczania silni rekurencyjny', 'algorytm', 'algorytm obliczania silni']


print("names.sort(): ", sorted(names), '\n')
print("names.sort(key=len): ", sorted(names, key=len), '\n')
print("names.sort(key=len, reverse=True): ",
      sorted(names, key=len, reverse=True), '\n')

names.sort()
print("names.sort(): ", names, '\n')

names.sort(key=len)
print("names.sort(key=len): ", names, '\n')

names.sort(key=len, reverse=True)
print("names.sort(key=len, reverse=True): ", names, '\n')
