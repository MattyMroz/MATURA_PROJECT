number = 1
while number <= 5:
    print(number)
    number += 1

print()

# L = zakres domknięty, R = zakres otwarty
# range(stop) = 0 1 2 3 4
for number in range(1, 6):
    print(number)

print()

# end=" " - bez znaku nowej linii = 1 2 3 4 5
for number in range(1, 6):
    print(number, end=" ")

print()

# range(start, stop, step) = 1 3 5
for number in range(1, 6, 2):
    print(number, end=" ")

print()

# if - warunek = 2 4
for number in range(1, 6):
    if number % 2 == 0:
        print(number, end=" ")

print()

# continue - przerwanie iteracji = 1 2 4 5
for number in range(1, 6):
    if number == 3:
        continue
    print(number, end=" ")

print()

# break - przerwanie pętli = 1 2
for number in range(1, 6):
    if number == 3:
        break
    print(number, end=" ")
