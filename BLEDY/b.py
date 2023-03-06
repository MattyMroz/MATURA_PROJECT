# x = 0
# while x < 1:
#     print(f'{x:.10f}')
#     x += 0.1

# print()
# x = 0
# d = 0.1
# while abs(x - 1) > d:
#     x += d
#     print(f'{x:.10f}')


# waga = float(input("Waga w kg: "))
# wzrost = float(input("Wzrost w m: "))
# BMI = waga/wzrost**2
# print("Twoje BMI wynosi %f" % BMI)
# print("Twoje BMI wynosi {:f}".format(BMI))
# print("Twoje BMI wynosi", round(BMI, 10))
# print("Twoje BMI wynosi: {:.2f}".format(BMI))


import math
a, b, c = 0.1, -6, 4

# Wyznacz pierwiastki równania kwadratowego z wykorzystaniem delty. Program powinien być uniwersalny.
if a == 0 and b == 0 and c == 0:
    print("Równanie ma nieskończenie wiele rozwiązań")
elif a == 0 and b == 0 and c != 0:
    print("Równanie nie ma rozwiązań")
elif a == 0 and b != 0 and c != 0:
    x = -c / b
    print("Równanie liniowe ma jedno rozwiązanie: x = ", x)
elif a != 0 and b != 0 and c != 0:
    delta = b**2 - 4 * a * c
    if delta < 0:
        print("Równanie nie ma rozwiązań")
    elif delta == 0:
        x = -b / (2 * a)
        print("Równanie ma jedno rozwiązanie: x = ", x)
    elif delta > 0:
        # z delty
        x1 = (-b - delta**0.5) / (2 * a)
        x2 = (-b + delta**0.5) / (2 * a)
        print("Równanie ma dwa rozwiązania: x1 =", x1)
        print("Równanie ma dwa rozwiązania: x2 =", x2)

        # Wzory viete'a
        # Wyznacz pierwiastki równania kwadratowego z wykorzystaniem wzoru  Viète’a na iloczyn pierwiastków z dokładnością do 0.000001. Program powinien być uniwersalny.
        # x1 + x2 = -b/a
        # x1 * x2 = c/a

        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = c / (a * x1)
        print("Równanie ma dwa rozwiązania: x1 =", x1)
        print("Równanie ma dwa rozwiązania: x2 =", x2)
        print("Iloczyn pierwiastków równania kwadratowego to: ",
              "{0:.6f}".format(x1 * x2))

        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = c / (a * x1)
        print("Równanie ma dwa rozwiązania: x1 =", x1)
        print("Równanie ma dwa rozwiązania: x2 =", x2)
        print("Iloczyn pierwiastków równania kwadratowego to: ",
              "{0:.6f}".format(x1 * x2))

        x1 = (-b - math.sqrt(delta)) / (2 * a)
        if abs(x1) > 0.000001:
            x2 = c / (a * x1)
            print("Iloczyn pierwiastków równania kwadratowego to: ",
                  " {0:.6f}".format(x1 * x2))
        else:
            x2 = 0
            print("Iloczyn pierwiastków równania kwadratowego to: ",
                  " {0:.6f}".format(x1 * x2))



