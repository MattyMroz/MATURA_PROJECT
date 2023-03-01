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
        n = str(n)
        silnia = len(n)
        num = 0
        for element in n:
            num += int(element) * silnia(silnia)
            silnia -= 1
        return num


print(silniowy_system_pozycyjny(310))
