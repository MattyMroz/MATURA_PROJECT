# Graf  jest  strukturą złożoną z wierzchołków i krawędzi łączących te wierzchołki, która pozwala modelować wszelkiego rodzaju sieci oraz układy, w których występują skomplikowane zależności pomiędzy składnikami.

# Grafy mogą być nieskierowane lub skierowane, wagowe, o strukturze drzewa.

# Przeszukiwanie w głąb grafu (ang. depth-first search, DFS)


# 5 8
# 0 1
# 0 3
# 1 2
# 2 0
# 3 1
# 3 4
# 4 1
# 4 2

def read_graph():
    graph = []
    with open('graf.txt', 'r') as f:
        for line in f:
            graph.append(line.strip().split())
    # print("Graf: ", graph)
    return graph


def dfs(start):
    graph = read_graph()
    visited = []
    stack = [start]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                stack.append(w)

    print("Kolejnosc odwiedzania wierzcholkow: ", visited)

# 0 3 4 1 2
def main():
    print("Przeszukiwanie w głąb grafu (ang. depth-first search, DFS): ")
    dfs(0)


if __name__ == '__main__':
    main()
