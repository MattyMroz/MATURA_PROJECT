def bucket_sort(arr):
    max_val = max(arr)
    size = max_val/len(arr)

    buckets = [[] for _ in range(len(arr))]
    for i in range(len(arr)):
        j = int(arr[i]/size)
        if j != len(arr):
            buckets[j].append(arr[i])
        else:
            buckets[len(arr) - 1].append(arr[i])

    for i in range(len(arr)):
        buckets[i] = sorted(buckets[i])

    result = []
    for i in range(len(arr)):
        result = result + buckets[i]

    return result


arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print("Posortowana tablica: ", bucket_sort(arr))


def sortowanie_przez_kubelki(tablica):
    max_wart = max(tablica) # znajdujemy największą wartość w tablicy
    rozmiar = max_wart / len(tablica) # określamy rozmiar kubelka

    kubelki = [] # tworzymy pustą tablicę kubelków
    for i in range(len(tablica)): # dla każdego kubelka
        kubelki.append([]) # dodajemy pustą listę

    for i in range(len(tablica)): # dla każdego elementu w tablicy
        j = int(tablica[i] / rozmiar) # określamy indeks kubelka
        if j != len(tablica): # jeżeli indeks nie jest równy długości tablicy
            kubelki[j].append(tablica[i]) # dodajemy element do kubelka
        else:
            kubelki[len(tablica) - 1].append(tablica[i]) # dodajemy element do ostatniego kubelka

    for i in range(len(tablica)): # dla każdego kubelka
        kubelki[i] = sorted(kubelki[i]) # sortujemy kubelki

    wynik = []
    for i in range(len(tablica)): # dla każdego kubelka
        wynik += kubelki[i] # dodajemy elementy do wyniku

    return wynik

tablica = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
print("Posortowana tablica: ", sortowanie_przez_kubelki(tablica))


def sortowanie_przez_kubelki(tablica):
    max_wart = max(tablica)
    rozmiar = max_wart / len(tablica)

    kubelki = []
    for i in range(len(tablica)):
        kubelki.append([])

    for i in range(len(tablica)):
        j = int(tablica[i] / rozmiar)
        if j != len(tablica):
            kubelki[j].append(tablica[i])
        else:
            kubelki[len(tablica) - 1].append(tablica[i])

    for i in range(len(tablica)):
        kubelki[i] = sorted(kubelki[i])

    wynik = []
    for i in range(len(tablica)):
        wynik += kubelki[i]

    return wynik

tablica = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]


print("Posortowana tablica: ", sortowanie_przez_kubelki(tablica))


tablica2 = ['kot',  'kapa', 'klacz', 'kopytko', 'kret', 'kilt', 'kogut', 'komputer', 'kara']
print("Posortowana tablica: ", sortowanie_przez_kubelki(tablica2))
