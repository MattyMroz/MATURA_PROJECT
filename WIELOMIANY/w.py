# Wielomiany
# wykładnik = 3
# a3 = 1
# a2 = 2
# a1 = 3
# a0 = 4
# x = 2
# wynki = 26


# Zad 1
def get_w_naiwny():
    s = int(input("Podaaj stopień wielomianu: "))
    arr = []
    for i in range(s + 1):
        a = float(input("a" + str(i) + " = "))
        arr.append(a)
    print(arr)
    x = float(input("Podaj x: "))
    w = 0
    for i in range(0, s + 1):
        w += arr[i] * x**i
    print("W(x) = " + str(w))


get_w_naiwny()

# Zad 2


def get_w_hornel():
    s = int(input("Podaj stopień wielomianu: "))
    arr = []
    for i in range(s+1):
        a = float(input("a" + str(s-i) + " = "))
        arr.append(a)
    print(arr)
    x = float(input("Podaj x: "))
    w = arr[0]
    for i in range(1, s+1):
        w = w * x + arr[i]
        print("W(x) = " + str(w))
    print("W(x) = " + str(w))


get_w_hornel()


# Zad 3
def get_w_hornel_bin():
    s = input("Podaj stopień wielomianu w postaci binarnej: ")
    s = int(s, 2)
    print(s)
    arr = []
    for i in range(s+1):
        a = int(input("W postaci binarnej: a" + str(s-i) + " = "), 2)
        arr.append(a)
    print(arr)
    x = int(input("Podaj x w postaci binarnej: "), 2)
    print(x)
    w = arr[0]
    for i in range(1, s+1):
        w = w * x + arr[i]
        print("W(x) = " + str(w))
    print("W(x) = " + str(w))


get_w_hornel_bin()

# Zadanie 2 / 128


def get_w_hornel_2(arr, s, x):
    w = 0
    for i in range(s+1):
        w = w * x + arr[i]
    print("W(x) = " + str(w))
    return w


with open('./wielomiantxt.txt', 'r') as f:
    s = int(f.readline())
    arr = []
    for line in f:
        for i in line.split():
            arr.append(float(i))
    print(arr)
    x = float(input("Podaj x: "))
    get_w_hornel_2(arr, s, x)
