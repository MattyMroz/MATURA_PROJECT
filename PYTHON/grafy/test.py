def read_graph():
    graph = []
    with open('graf.txt', 'r') as f:
        for line in f:
            graph.append(line.strip().split())
    # print("Graf: ", graph)
    return graph

def dfs(start, graph, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for v in graph[start]:
        if v not in visited:
            dfs(v, graph, visited)
    return visited

def main():
    graph = read_graph()
    result = dfs(0, graph)
    print("Kolejność odwiedzania wierzchołków: ", result)

if __name__ == '__main__':
    main()

