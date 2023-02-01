list_1 = [24, 1, 8, 23, 17, 15, 5, 7, 14, 16, 4, 6, 13, 20, 3, 18, 19, 10, 21, 12, 2, 11, 9, 22]
list_2 = ['alfa', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta', 'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi', 'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi', 'chi', 'psi', 'omega']


list_list = [['alfa', 1], ['beta', 2], ['gamma', 3], ['delta', 4], ['epsilon', 5], ['zeta', 6], ['eta', 7], ['theta', 8], ['iota', 9], ['kappa', 10], ['lambda', 11], ['mu', 12], ['nu', 13], ['xi', 14], ['omicron', 15], ['pi', 16], ['rho', 17], ['sigma', 18], ['tau', 19], ['upsilon', 20], ['phi', 21], ['chi', 22], ['psi', 23], ['omega', 24]]

list_tuple = [('alfa', 1), ('beta', 2), ('gamma', 3), ('delta', 4), ('epsilon', 5), ('zeta', 6), ('eta', 7), ('theta', 8), ('iota', 9), ('kappa', 10), ('lambda', 11), ('mu', 12), ('nu', 13), ('xi', 14), ('omicron', 15), ('pi', 16), ('rho', 17), ('sigma', 18), ('tau', 19), ('upsilon', 20), ('phi', 21), ('chi', 22), ('psi', 23), ('omega', 24)]


list_1.sort()
print(".sort(): ", list_1, '\n')

list_2.sort()
print(".sort(): ", list_2, '\n')

# sortowanie dłgości słów
list_2.sort(key=len) # sortowanie w miejscu
print(".sort(key=len): ", list_2, '\n')
list_2 = sorted(list_2, reverse=True, key=len) # sorted nie zmienia listy, tylko zwraca posortowaną listę
print("sorted(list_2, reverse=True, key=len): ", list_2, '\n')

# sortowanie tablicy dwuwymiarowej po pierwszej kolumnie
print("list_list: ", list_list, '\n')
print("sorted(list_list, key=lambda x: x[0]): ", sorted(list_list, key=lambda x: x[0]), '\n')
