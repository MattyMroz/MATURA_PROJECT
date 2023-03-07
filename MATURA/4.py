# 4. Wiązka zadań Silniowy system pozycyjny
# ݊! = 1 ∙ 2 ∙ 3 ∙ … ∙ (݊n − 1) ∙ ݊n

def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)


# print(silnia(4))


def silniowy_system_pozycyjny(n):
    if n == 0:
        return 0
    else:
        sum = 0
        # 1200 = 1 * 4! + 2 * 3! + 0 * 2! + 0 * 1! = 40
        for i in range(len(n)):
            sum += int(n[i]) * silnia(len(n) - i)
        return sum


# print(silniowy_system_pozycyjny("1220"))
print("Dla 1220 wynik to: ", silniowy_system_pozycyjny("1220"))
print("Dla 310 wynik to: ", silniowy_system_pozycyjny("310"))
print("Dla 2011 wynik to: ", silniowy_system_pozycyjny("2011"))
print("Dla 54211 wynik to: ", silniowy_system_pozycyjny("54211"))


# 2. Podaj największy zapis w systemie silniowym, który można zapisać w systemie dziesiętnym za pomocą 5 cyfr.
# ݊! = 1 ∙ 2 ∙ 3 ∙ … ∙ (݊n − 1) ∙ ݊n

# Maksymalną liczbą 5-cyfrową zapisaną w silniowym systemie pozycyjnym jest (54321)! bo w systemie silniowym współczynnik xi, odpowiadający mnożnikowi i!, spełnia zależność 0 ≤ xi ≤ i

# Zamiana zapisu liczby w systemie dziesiętnym na zapis w systemie silniowym może przebiegać według następującego schematu: Szukamy największej liczby k, której silnia nie przekracza liczby x. Pierwsza jej cyfra to wynik dzielenia całkowitego x przez k!. Kolejne cyfry zapisu silniowego (zaczynając od cyfr najbardziej znaczących) otrzymujemy przez wyznaczanie
# wyników dzielenia liczby x przez (k – 1)!, (k –2)!, ..., 2!, 1!. Po wyznaczeniu cyfry xi, odpowiadającej współczynnikowi i!, zmniejszamy wartość x o liczbę odpowiadającą cyfrze xi,
# czyli xi⋅i!. Oznacza to, że x przyjmuje wartość x mod k!.


# https://zadania.dlamaturzysty.info/s/5159/81431-informatyka/5040154-zadania-z-informatyki-Analiza-algorytmow.htm?podstr=3
