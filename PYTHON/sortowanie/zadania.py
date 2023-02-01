import random
# n = int(input("Podaj liczbę elementów tablicy: "))
n = 10
tab = [-1, 1, -1, 4, 2, 6, -1, 8, 9, 10]
# for i in range(n):
#     tab.append(random.randint(-9, 9))
# tab = [random.randint(-9, 9) for _ in range(n)]
print("Tablica: ", tab)

# Sortowanie bezwzględne
# for i in range(n):
#     for j in range(n):
#         if abs(tab[i]) < abs(tab[j]):
#             tab[i], tab[j] = tab[j], tab[i]
# print("Posortowana tablica: ", tab)

# Sortowanie bezwzględne napiszane po ludzku
for i in range(n):
    for j in range(n):
        if abs(tab[i]) < abs(tab[j]):
            temp = tab[i]
            tab[i] = tab[j]
            tab[j] = temp
print("Posortowana tablica: ", tab)