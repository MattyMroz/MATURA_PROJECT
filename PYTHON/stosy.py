# https://www.algorytm.edu.pl/struktury-danych/stos-kolejka-lifo.html
# https://www.algorytm.edu.pl/algorytmy-maturalne/onp


# Odwrotna Notacja Polska (ONP)
# 5 3 7 - 2 * 3 5 1 + * - * 3 -

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

ONP_str = "5 3 7 - 2 * 3 5 1 + * - * 3 -"
print(ONP_str)
print(ONP(ONP_str))


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

# algebra = "a*(a-b)/(a+b)"
algebra = "2*(2-1)/(2+1)"
print(algebraToONP(algebra))


print(ONP("2 2 1 - * 2 1 + /"))
