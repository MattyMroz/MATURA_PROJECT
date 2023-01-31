# n = 9
# k = 2
# 2
# 4
# 6
# 8
# 1
# 5
# 9
# 7
# 3

# algorytm Josephusa - iteracyjnie
def josephus_ite(n, k):
    res = 0
    for i in range(1, n+1):
        res = (res + k) % i
    return res + 1


print("Pozycja Józefa Flawiusza: ", josephus_ite(9, 2))

# algorytm Josephusa - rekurencyjnie


def josephus_rek(n, k):
    if n == 1:
        return 1
    else:
        return (josephus_rek(n - 1, k) + k-1) % n + 1


print("Pozycja Józefa Flawiusza: ", josephus_ite(9, 2))

# n = int(input("Podaj liczbę osób: "))
# k = int(input("Podaj liczbę co ile osoba zostaje usunięta: "))
n = 9
k = 2

items = [i + 1 for i in range(n)]
print(items)


def josephus_list(items, k):
    if len(items) == 1:
        return items[0]
    else:
        # return (josephus_list(n - 1, k) + k - 1) % n + 1
        # [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # ((josephus_list(items[:-1], k) + k - 1) % len(items) + 1) = 3
        # items[3] = 4  items[3 -1] = 3
        return items[((josephus_list(items[:-1], k) + k - 1) % len(items) + 1) - 1]


print("Pozycja Józefa Flawiusza: ", josephus_list(items, k))

n = 9
k = 2
items = [i + 1 for i in range(n)]
print(items)


def josephus_list_ite(items, k):
    for _ in range(len(items) - 1):
        for _ in range(k - 1):
            # przejdź do następnego elementu listy
            # usuwa item[0] i dodaje go na koniec listy
            items.append(items.pop(0))
        print(items[0])
        # usuń pierwszy element listy
        items.pop(0)
    print(items[0])


josephus_list_ite(items, k)





# dla i <- 1, 2, ..., n-1 wyjonuj
#     dla j <- 1, 2, ..., k-i wyjonuj
#         przejdz do nastepnego elementu
#     usuń bierzacy element z listy


# pseudokod
# funkcja josephus(n, k)
# jeżeli n = 1
    # to zwróć 1
# w przeciwnym wypadku
#     zwróć (josephus(n - 1, k) + k-1) % n + 1


# n = 9, k = 2
# items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# funkcja josephus_list_ite(items, k)
#     jeżeli długość items = 1
#         zwróć items[0]
#     w przeciwnym wypadku
#         zwróć items[((josephus_list_ite(items skrucone o ostatnie miejsce, k) + k - 1) % długość items + 1) - 1]