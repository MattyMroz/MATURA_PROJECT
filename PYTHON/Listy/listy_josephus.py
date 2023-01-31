# n = 9
# k = 2
# # 4
# # 6
# # 8
# # 1
# # 5
# # 9
# # 7
# # 3

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
        return (josephus_list(items[:-1], k) + k - 1) % len(items) + 1

# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# items[3] = 4  items[3 -1] = 3
print("Pozycja Józefa Flawiusza: ", items[josephus_list(items, k) - 1])