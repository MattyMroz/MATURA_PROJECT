# Triki i funkcje zmiennych

# Triki i funkcje typ tekstowy
string = "Ala ma kota"  # inicjalizacja zmiennej
print(string)  # print - czyli wypisanie tekstu # Ala ma kota
print(type(string))  # type - czyli sprawdzenie typu zmiennej
print(len(string))  # len - czyli długość tekstu
print(string[0])  # [0] - czyli pierwszy znak
print(string[:3])  # [:3] - czyli pierwsze 3 znaki
print(string[3:])  # [3:] - czyli od 3 znaku do końca
print(string[-3:])  # [-3:] - czyli od końca 3 znaki
print(string[:-3])  # [-3:] - czyli od końca 3 znaki
print(string[:3:2])  # [:3:2] - czyli pierwsze 3 znaki co drugi
print(string[::2])  # [::2] - czyli co drugi znak
print(string[::-1])  # [::-1] - czyli odwrócenie tekstu
print(string + string)  # + - czyli konkatenacja
print(string + " " + string)  # + - czyli konkatenacja>>>
print(string * 3)  # * - czyli powtórzenie tekstu
print(string.upper())  # upper - czyli zamiana na wielkie litery
print(string.lower())  # lower - czyli zamiana na małe litery
# title - czyli zamiana na wielkie litery na początku każdego słowa
print(string.title())
# capitalize - czyli zamiana na wielką literę na początku tekstu
print(string.capitalize())
print(string.replace("Ala", "Ola"))  # replace - czyli zamiana tekstu
string = "Ala ma kota, Ala ma psa, Ala ma rybki"
# replace - czyli zamiana tekstu - tylko 1 raz
print(string.replace("Ala", "Ola"))
# replace 2 - czyli zamiana tekstu - tylko 2 razy
print(string.replace("Ala", "Ola", 2))
# split - czyli podział tekstu na listę tam gdzie jest spacja
print(string.split(" "))
# split - czyli podział tekstu na listę i wybranie pierwszego elementu
print(string.split(" ")[0])
# split - czyli podział tekstu na listę i wybranie drugiego elementu
print(string.split(" ")[1])

string = "Ala ma kota"
print(string.find("Ala"))  # find - czyli wyszukanie tekstu
print(string.find("Ala", 5))  # find - czyli wyszukanie tekstu od 5 znaku
# find - czyli wyszukanie tekstu od 5 do 10 znaku
print(string.find("Ala", 0, 11))
# find - czyli wyszukanie tekstu od 5 do 10 znaku i sprawdzenie czy znaleziono
print(string.find("Ala", 0, 11) != -1)
print("Ala" in string)  # in - czyli sprawdzenie czy tekst jest w tekście
# not in - czyli sprawdzenie czy tekst nie jest w tekście
print("Ala" not in string)
# startswith - czyli sprawdzenie czy tekst zaczyna się od tekstu
print(string.startswith("Ala"))
# endswith - czyli sprawdzenie czy tekst kończy się na tekst
print(string.endswith("Ala"))
# isalpha - czyli sprawdzenie czy tekst składa się tylko z liter
print(string.isalpha())
# isdigit - czyli sprawdzenie czy tekst składa się tylko z cyfr
print(string.isdigit())
# isalnum - czyli sprawdzenie czy tekst składa się tylko z liter i cyfr
print(string.isalnum())
# islower - czyli sprawdzenie czy tekst składa się tylko z małych liter
print(string.islower())
# isupper - czyli sprawdzenie czy tekst składa się tylko z wielkich liter
print(string.isupper())
# istitle - czyli sprawdzenie czy tekst składa się tylko z wielkich liter na początku słów
print(string.istitle())
# isspace - czyli sprawdzenie czy tekst składa się tylko z białych znaków
print(string.isspace())
# isdecimal - czyli sprawdzenie czy tekst składa się tylko z cyfr
print(string.isdecimal())
# isnumeric - czyli sprawdzenie czy tekst składa się tylko z cyfr
print(string.isnumeric())
# isidentifier - czyli sprawdzenie czy tekst jest poprawnym identyfikatorem
print(string.isidentifier())
# isprintable - czyli sprawdzenie czy tekst jest drukowalny
print(string.isprintable())
print(string.isascii())  # isascii - czyli sprawdzenie czy tekst jest ASCII

print(string.count("Ala"))  # count - czyli zliczenie wystąpień tekstu
# count - czyli zliczenie wystąpień tekstu od 1 do 10 znaku
print(string.count("Ala", 0, 11))
print(string.index("Ala"))  # index - czyli pierwsze wystąpienie tekstu
# index - czyli wyszukanie tekstu od 1 do 10 znaku
print(string.index("Ala", 0, 11))
print(string.rindex("Ala"))  # rindex - czyli wyszukanie tekstu od końca

# zfill - czyli wypełnienie tekstu zerami z lewej strony do 20 znaków
print(string.zfill(20))
# center - czyli wypełnienie tekstu spacjami z lewej i prawej strony do 20 znaków
print(string.center(20))

# ljust - czyli wypełnienie tekstu spacjami z lewej strony
print(string.ljust(20))
# rjust - czyli wypełnienie tekstu spacjami z prawej strony
print(string.rjust(20))

# strip - czyli usunięcie białych znaków z lewej i prawej strony
string = " Ala ma kota "
print(string.strip())
print(string.lstrip())  # lstrip - czyli usunięcie białych znaków z lewej strony
print(string.rstrip())  # rstrip - czyli usunięcie białych znaków z prawej strony
# strip - czyli usunięcie tekstu z lewej i prawej strony
print(string.strip(" Ala"))

string = "Ala ma kota"
# expandtabs - czyli zamiana tabulatorów na spacje
print(string.expandtabs(20))
print(string.encode())  # encode - czyli zamiana tekstu na bajty
print(string.encode().decode())  # decode - czyli zamiana bajtów na tekst


# join - czyli połączenie tekstu z listy
join_string = " ".join(["Ala", "ma", "kota"])
print(join_string)
join_string = "-"
# join - czyli połączenie tekstu z listy
print(join_string.join(["Ala", "ma", "kota"]))

string = "Ala "
string2 = "ma kota"
print(string + string2)  # + - czyli konkatenacja tekstu
print(" ".join([string, string2]))  # join - czyli połączenie tekstu z listy


# Triki i funkcje typy numeryczne
# Operatory arytmetyczne
a = 4
b = 3
print(a + b)  # dodawanie 4 + 3 = 7
print(a - b)  # odejmowanie 4 - 3 = 1
print(a * b)  # mnożenie 4 * 3 = 12
print(a / b)  # dzielenie 4 / 3 = 1.3333333333333333
print(a // b)  # dzielenie całkowite 4 // 3 = 1
print(a % b)  # reszta z dzielenia 4 % 3 = 1
print(a ** b)  # potęgowanie 4 ** 3 = 64
print(a ** 0.5)  # pierwiastkowanie 4 ** 0.5 = 2.0
print(a ** (1/2))  # pierwiastkowanie 4 ** (1/2) = 2.0
print(a ** (1/b))  # pierwiastkowanie 4 ** (1/3) = 1.5874010519681994

# Operatory inkrementacji i dekrementacji
print(a)  # 4
print(a + 1)  # 5
print(a)  # 4
a += 1  # a = a + 1 = 5
a -= 1  # a = a - 1 = 4
a *= 2  # a = a * 2 = 8
a /= 2  # a = a / 2 = 4.0
a = 4
a //= 2  # a = a // 2 = 2
a %= 2  # a = a % 2 = 0

a = 4
a **= 2  # a = a ** 2 = 16
a <<= 2  # a = a << 2 = 64
a >>= 2  # a = a >> 2 = 16
a &= 2  # a = a & 2 = 0
a |= 2  # a = a | 2 = 2
a ^= 2  # a = a ^ 2 = 0

# Kolejność działań
print(a + b * 2)  # kolejność działań 4 + 3 * 2 = 10
print((a + b) * 2)  # kolejność działań (4 + 3) * 2 = 14

# Operatory przypisania
print(a << b)  # przesunięcie bitowe w lewo 4 << 3 = 32
print(a >> b)  # przesunięcie bitowe w prawo 4 >> 3 = 0
print(a & b)  # operacja bitowa AND 4 & 3 = 0
print(a | b)  # operacja bitowa OR 4 | 3 = 7
print(a ^ b)  # operacja bitowa XOR 4 ^ 3 = 7
print(~a)  # operacja bitowa NOT ~4 = -5

# Operatory porównania
print(a == b)  # równość 4 == 3 = False
print(a != b)  # nierówność 4 != 3 = True
print(a < b)  # mniejsze 4 < 3 = False
print(a > b)  # większe 4 > 3 = True
print(a <= b)  # mniejsze lub równe 4 <= 3 = False
print(a >= b)  # większe lub równe 4 >= 3 = True

# Operatory tożsamości - sprawdzają identyczność obiektów w pamięci - sprawdz w www
# Nie zaleca się ich stosowania w normalnym kodzie
print(a is b)  # identyczność
print(a is not b)  # nierówność identyczności

# Ładniejsze wyświetlanie liczb w kodzie
a = 1_000_000  # podkreślenia w liczbach jako separator - czytelność
print(a)

# Triki i funkcje typy logiczne
a = True
b = False
print(a and b)  # operacja logiczna AND 1 and 0 = 0
print(a or b)  # operacja logiczna OR 1 or 0 = 1
print(not a)  # operacja logiczna NOT not 1 = 0
print(a)  # operacja logiczna NOT not 1 = 0
print(a is b)  # identyczność 1 is 0 = False
print(a is not b)  # nierówność identyczności 1 is not 0 = True

# Konwersja typów
a = 1
b = 2.0
c = "3"
print(a + int(c))  # konwersja na int - 1 + 3 = 4
print(a + float(c))  # konwersja na float - 1 + 3.0 = 4.0
print(str(a) + c)  # konwersja na string - "1" + "3" = "13"


# Konwersja systemów liczbowych
a = 10
print(bin(a))  # konwersja na binarny - 0b1010
print(oct(a))  # konwersja na ósemkowy - 0o12
print(hex(a))  # konwersja na szesnastkowy - 0xa

print(int("0b1010", 2))  # konwersja z binarnego na dziesiętny - 10
print(int("0o12", 8))  # konwersja z ósemkowego na dziesiętny - 10
print(int("0xa", 16))  # konwersja z szesnastkowego na dziesiętny - 10
