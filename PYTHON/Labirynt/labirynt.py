lab = []
with open('./labirynt.txt', 'r') as f:
    for line in f:
        lab.append(line.strip().split())
for row in lab:
    for i in row:
        print(i, end=" ")
    print()

start_x = 3
start_y = 5
print(lab[start_x][start_y])


def way(x, y):
    max_x = len(lab) - 1
    max_y = len(lab[0]) - 1
    if x == 0 or x == max_x or y == 0 or y == max_y:
        return True

    if lab[x - 1][y] == 'W':
        lab[x - 1][y] = 'D'
        way(x, y - 1)
    if lab[x + 1][y] == 'W':
        lab[x + 1][y] = 'D'
        way(x + 1, y)
    if lab[x][y - 1] == 'W':
        lab[x][y - 1] = 'D'
        way(x + 1, y)
    if lab[x][y + 1] == 'W':
        lab[x][y + 1] = 'D'
        way(x + 1, y)

    return False

way(start_x, start_y)
for row in lab:
    for i in row:
        print(i, end=" ")
    print()
