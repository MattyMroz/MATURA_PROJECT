# Dzielniki liczby
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# def rozklad(n):
#     rozklad = []
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             if is_prime(i):
#                 rozklad.append(i)
#             if is_prime(n // i):
#                 rozklad.append(n // i)
#     rozklad.sort()
#     return rozklad


import random

# Zadanie 1
# Napisz optymalną funkcję rozklad(n) rozkładu liczby naturalnej n na czynniki pierwsze.
# Wypisz wszystkie rozpatrywane czynniki podczas wykonywania funkcji oraz co zostanie zwrócone dla:
# • rozklad(21)
# • rozklad(16)


def rozklad(n):
    rozklad = []
    licznik = 0
    for i in range(2, int(n**0.5)+1):
        while n % i == 0:
            rozklad.append(i)
            n //= i
        licznik += 1
    if n > 1:
        rozklad.append(n)
    return rozklad


print(rozklad(21))
print(rozklad(16))


# Napisz funkcję sortującą 30 losowych czterocyfrowych liczb naturalnych wg dwóch ostatnich cyfr dziesiątek
# i jedności. Sortowanie powinno być stabilne tzn. liczby z takimi samymi cyframi dziesiątek jedności powinny
# zachować kolejność występowania w posortowanym ciągu.
# Np. dla liczb 3123, 1712, 2431, 1531, 1111, 4621 posortowane elementy 1111, 1712, 4621, 3123, 2431,
# 1531


nums = [random.randint(1000, 9999) for _ in range(30)]
print(nums)


def sort_dz_jed(nums):
    nums.sort(key=lambda x: (x % 100))
    return nums


print(sort_dz_jed(nums))


# Trójką pitagorejską nazywamy trzy liczby całkowite dodatnie a, b, c spełniające równanie
# Pitagorasa:
# a
# 2
# +b
# 2=c
# 2
# a b c
# 3 4 5
# 5 12 13
# 6 8 10
# 7 24 25
# 8 15 17
# 13 84 85
# Trójkę nazywamy pierwotną, jeżeli a, b i c są względnie pierwsze.
# Jeżeli trójka a, b, c jest pitagorejska, to jest też nią trójka da, db, dc, dla dowolnej liczby całkowitej d.
# Wynika z tego, że każdą trójkę pitagorejską możemy uzyskać przez pomnożenie jej elementów przez
# dowolną, tą samą liczbę całkowitą dodatnią.
# Napisz algorytm, który wypisze wszystkie kombinacje trójek pitagorejskich dla pierwszej i drugiej liczby z
# zakresu od 1 do 1000 oraz oznaczy wszystkie trójki pierwotne, wypisując przy nich słowo pierwotne


def dzielniki(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    divisors.sort()
    return divisors


def pitagoras_pierwotny(a, b, c):
    for i in range(2, 10000):
        if a % i == 0 and b % i == 0 and c % i == 0:
            return False
    return True


def pitagoras_względnie_pierwszy():

    for a in range(1, 1000):
        for b in range(1, 1000):
            c = (a**2 + b**2)**0.5
            if c.is_integer():
                if pitagoras_pierwotny(a, b, c):
                    print(a, b, int(c), end=" Pierwotne \n")


pitagoras_względnie_pierwszy()


# Napisz program zamieniający wyrażanie algebraiczne zapisane w odwrotnej notacji polskiej na wyrażenie
# zapisane w notacji tradycyjnej. Wyrażenie może składać się z argumentów jednoznakowych (liter albo cyfr),
# nawiasów okrągłych oraz dwuargumentowych działań arytmetycznych: dodawania (+), odejmowania (-) ,
# mnożenia (*) , wyznaczania części całkowitej z dzielenia (/), potęgowania (^).
# Np. ab-a1+/6ab+^* wyrażenie zapisane w ONP,
#  (a-b)/(a+1)*6^(a+b) wyrażenie zapisane w notacji tradycyjnej.


def ONPtoAlgebra(ONP_str):
    ONP_str = ONP_str.split()
    stos = []
    for i in ONP_str:
        if i.isalnum():
            stos.append(i)
        else:
            b = stos.pop()
            c = stos.pop()
            stos.append("("+c+i+b+")")

    return stos.pop()


print("Zamiana wyrażenia ONP na algebraiczne:")
ONP_str = "a b - a 1 + / 6 a b + ^ *"
print(ONPtoAlgebra(ONP_str))
