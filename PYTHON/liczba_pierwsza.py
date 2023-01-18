# Liczby pierwsze
import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

x = time.time()
count = 0
with open("./liczby_h.txt", "r") as file:
    for line in file:
        if is_prime(int(line, 16)):
            count += 1
print(count)
print(time.time() - x)