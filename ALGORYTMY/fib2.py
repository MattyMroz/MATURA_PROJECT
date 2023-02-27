n = 0


def rek(x, p, k, T):
    global n
    n += 1
    if p < k:
        s = (p+k) // 2
        if T[s] >= x:
            print(x, s, p, k)
            return rek(x, p, s, T)
        else:
            print(T[s], x, s, p, k)
            return rek(x, s+1, k, T)
    else:
        if T[p] == x:
            return p
        else:
            return -1


print(rek(37, 1, 11, [1, 5, 8, 10, 12, 14, 19, 20, 23, 30, 38]))
print(n)

# logarytmiczna złożoność obliczeniowa bo sykona się 4 razy dla 11 elementów w tablicy, gdzie liniowa była by 11 razy. kwadratowa 121 razy, a sześcienna 1771561 razy