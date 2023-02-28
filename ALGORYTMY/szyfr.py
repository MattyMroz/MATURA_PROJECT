# M A _ F O Y K
# A R Z N R T I
# T U _ I M A _

# tablica 2 wymiarowa


# print(arr)


# Dane:
# k – klucz, liczba całkowita większa od 0
# n – liczba znaków w tekście zaszyfrowanym, n jest wielokrotnością k
# S[1..n] – ciąg znaków (tekst do odszyfrowania)
# Wynik:
# T[1..n] – ciąg znaków (tekst odszyfrowany)

# Pn/k;
# W0;zP;
# dla i=1, …, P wykonuj
# WW+1;
# dla j=1 … k wykonuj
#  TT+S[W]; WW+z;
# WW-z;
# zz*(-1);


def odszyfruj(k, n, S):
    P = int(n / k)
    W = -1
    Z = P
    T = []
    for i in range(1, P + 1):
        W += 1
        for j in range(1, k + 1):
            T.append(S[W])
            W += Z
        W -= Z
        Z *= -1
    print(T)


arr = ["M", "A", "_", "F", "O", "Y", "K",
       "A", "R", "Z", "N", "R", "T", "I",
       "T", "U", "_", "I", "M", "A", "_"]
odszyfruj(3, 21, arr)
