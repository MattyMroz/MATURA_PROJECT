# Program sprawdzający czy punkt P nalerzy do wielokonta

# w2.txt
# 5 = ile razy
# 2 0
# 1 1
# 2 3
# 4 4
# 5 2

with open('./w2.txt', 'r') as f:
    ile = int(f.readline())
    w = []
    for line in f:
        for i in line.split():
            w.append(float(i))
print(w)

print(w)

def wyznacznik_macierzy(x1, y1, x2, y2, x3, y3):
    return (x3 - y1) * (x2 - x1) - (y2 - y1)*(x3 - x1)

xP = 1
yP = -1

w1 = wyznacznik_macierzy(w[0], w[1], w[2], w[3], xP, yP)

for i in range(1, ile):
    # print(w[i*2], w[i*2+1])
    w2 = wyznacznik_macierzy(w[i+1], w[i*2+1], w[i*2+2], w[i*2+3], xP, yP)


# czy punkt nalerzy do wielokonta wypukłego


# with open('./wielomiantxt.txt', 'r') as f:
#     s = int(f.readline())
#     arr = []
#     for line in f:
#         for i in line.split():
#             arr.append(float(i))
#     print(arr)
#     x = float(input("Podaj x: "))
#     get_w_hornel_2(arr, s, x)




# print(wyznacznik_macierzy(xA, yA, xB, yB, xP, yP))
# print(wyznacznik_macierzy(xB, yB, xC, yC, xP, yP))
# print(wyznacznik_macierzy(xC, yC, xA, yA, xP, yP))


# def czy_punkt_nalezy_do_trojkota():
#     w1 = wyznacznik_macierzy(xA, yA, xB, yB, xP, yP)
#     w2 = wyznacznik_macierzy(xB, yB, xC, yC, xP, yP)
#     if w1 * w2 < 0:
#         return False
#     w2 = wyznacznik_macierzy(xC, yC, xA, yA, xP, yP)
#     if w1 * w2 < 0:
#         return False
#     return True


# if czy_punkt_nalezy_do_trojkota():
#     print("Punkt należy do trójkąta")
# else:
#     print("Punkt nie należy do trójkąta")
