# sourcery skip: merge-nested-ifs, use-fstring-for-concatenation
A = [True] * 200_000
A[0] = False
for i in range(2, int(200_000**0.5) + 1):
    if A[i]:
        j = 2
        while i * j < 200_000:
            A[i * j] = False
            j += 1

for i in range(2, 200_000):
    if A[i]:
        print(i)

n = 200_000
for i in range(2, n-8):
    if A[i]:
        if A[i + 2] and A[i + 6] and A[i + 8]:
            print(str(i) + " " + str(i + 2) +
                  " " + str(i + 6) + " " + str(i + 8))
