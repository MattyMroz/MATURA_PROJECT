# https://www.algorytm.edu.pl/struktury-danych/stos-kolejka-lifo.html
# https://www.algorytm.edu.pl/algorytmy-maturalne/onp


# Odwrotna Notacja Polska (ONP)
# Oblicz wynik wyrażenia zapisanego w notacji ONP. Wykorzystaj stos w rozwiązaniu. Np. wprowadź wyrażenie 5 3 7 - 2 * 3 5 1 + * - * 3 -  Wynik -133

def ONP(ONP_str):
    ONP_str = ONP_str.split()
    stos = []
    for i in ONP_str:
        if i.isalnum():
            stos.append(int(i))
        else:
            b = stos.pop()
            c = stos.pop()
            if i == "+":
                stos.append(c+b)
            elif i == "-":
                stos.append(c-b)
            elif i == "*":
                stos.append(c*b)
            elif i == "/":
                stos.append(c/b)
            elif i == "^":
                stos.append(c**b)
    return stos.pop()

print("Obliczanie wyrażenia ONP:")
ONP_str = "5 3 7 - 2 * 3 5 1 + * - * 3 -"
print(ONP_str)
print(ONP(ONP_str))

# Zapisz wyrażenie algebraiczne zapisane w sposób tradycyjny np. a*(a-b)/(a+b), które wprowadzasz z klawiatury, na notację ONP.
def algebraToONP(algebra):
    stos = []
    ONP = []
    operatory = {'+':1, '-':1, '*':2, '/':2, '(':0}
    for i in algebra:
        if i.isalnum():
            ONP.append(i)
        elif i == '(':
            stos.append(i)
        elif i in operatory:
            while len(stos) > 0 and operatory[stos[-1]] >= operatory[i]:
                ONP.append(stos.pop())
            stos.append(i)
        elif i == ')':
            while stos[-1] != '(':
                ONP.append(stos.pop())
            stos.pop()
    while len(stos) > 0:
        ONP.append(stos.pop())
    return ' '.join(ONP)

print("Zamiana wyrażenia algebraicznego na ONP:")
algebra = "a*(a-b)/(a+b)"
print(algebraToONP(algebra))

algebra = "2*(2-1)/(2+1)"
print(algebraToONP(algebra))
print(ONP(algebraToONP(algebra)))


# Zamień wyrażenie podane w notacji ONP na wyrażenie algebraiczne zapisane w sposób tradycyjny. Wykorzystaj stos w rozwiązaniu.

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
ONP_str = "5 3 7 - 2 * 3 5 1 + * - * 3 -"
print(ONPtoAlgebra(ONP_str))