# 4. Wiązka zadań Silniowy system pozycyjny
# ݊! = 1 ∙ 2 ∙ 3 ∙ … ∙ (݊n − 1) ∙ ݊n

def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)


print(silnia(4))


def silniowy_system_pozycyjny(n):
    if n == 0:
        return 0
    else:
        # zamień n na string
        s = str(n)
        sum = 0
        for i in range(len(s)):
            sum += int(s[i]) * silnia(len(s) - i)
        return sum

print(silniowy_system_pozycyjny(1200))
