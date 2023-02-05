import itertools # podwójna pętla for
import random # losowanie liczb

# Najlepsze rozwiązanie zadania
def zad_1_1():
    n = int(input("Podaj liczbę elementów tablicy: "))
    num = [random.randint(-9, 9) for _ in range(n)]
    print("Tablica: ", num)
    # sorted
    print("Posortowana tablica: ", sorted(num, key=abs))
    print("Posortowana tablica: ", sorted(num, key=abs, reverse=True))
    # Sortowanie bąbelkowe
    for i, j in itertools.product(range(n), range(n)):
        if abs(num[i]) < abs(num[j]):  # > - malejąco
            num[i], num[j] = num[j], num[i]
    print("Posortowana tablica: ", num)

# Prostrze wersje sortowania bezwzględnego


def zad_1_2():
    n = 9
    tab = [-6, 5, -1, 2, 1, -1, -5, 6, 2]
    # tab = []
    # for i in range(n):
    #     tab.append(random.randint(-9, 9))

    print("Tablica: ", tab)
    print("Posortowana tablica: ", sorted(tab, key=abs))

    # 1 - wersja podstawowa
    tab = [-6, 5, -1, 2, 1, -1, -5, 6, 2]
    for i in range(n):
        for j in range(n):
            if abs(tab[i]) < abs(tab[j]):  # > - malejąco
                temp = tab[i]
                tab[i] = tab[j]
                tab[j] = temp
    print("Posortowana tablica: ", tab)

    # 2 - brak zmiennej pomocniczej
    tab = [-6, 5, -1, 2, 1, -1, -5, 6, 2]
    for i in range(n):
        for j in range(n):
            if abs(tab[i]) < abs(tab[j]):  # > - malejąco
                tab[i], tab[j] = tab[j], tab[i]
    print("Posortowana tablica: ", tab)

    # 3 - itertools - czyli podwójna pętla for - import itertools
    # tab = [-6, 5, -1, 2, 1, -1, -5, 6, 2]
    for i, j in itertools.product(range(n), range(n)):
        if abs(tab[i]) < abs(tab[j]):  # > - malejąco
            tab[i], tab[j] = tab[j], tab[i]
    print("Posortowana tablica: ", tab)



def zad_2():
    print("lol")






def main():
    # print("Zadanie 1.1")
    # zad_1_1()
    # print("Zadanie 1.2")
    # zad_1_2()
    print("Zadanie 2")
    zad_2()


if __name__ == '__main__':
    main()


# Psełdocosie *_*

# import biblioteki random
# funkcja zad_1_1()
#     wczytaj n
#     num = []
#     dla i w zakresie od 0 do n wykonaj
#         do num dodaj losową liczbę całkowitą z zakresu od -9 do 9

#         alternatywnie
#         na końcu num dodaj random.randint(-9, 9)

#     wyświetl: wbydowoną funkcję sorted z parametrem num i kluczem = abs

#     alternatywnie

#     dla i, j w zakresie od 0 do n wykonaj
#         jeżeli abs(num[i]) < abs(num[j])
#             to num[i], num[j] = num[j], num[i]
#     wyświetl num

# wykonaj zad_1_1()