# Wypisywanie tekstu
print("Hello World!")
print("Hello", "World!")
print("Hello", "World!", sep="\t")
print("Hello", "World!", sep="\n")

a = input("Podaj liczbę: ")
print(a)
a = int(input("Podaj liczbę: "))
print(a)
a = float(input("Podaj liczbę: "))
print(a)
a = str(input("Podaj liczbę: "))  # niepotrzebne
print(a)
# eval() - wykona kod w stringu jako kod pythona
a = eval(input("Podaj liczbę: "))
print(a)
a = complex(input("Podaj liczbę: "))  # zespolona
print(a)
a = bool(input("Podaj liczbę: "))  # bool - True lub False
