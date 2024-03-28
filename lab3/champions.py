from problem_max_flow import *


class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append(v)

    def get_adjacent_nodes(self, u):
        return self.adjacency_list.get(u, [])

    def print_graph(self):
        for node, neighbors in graph.adjacency_list.items():
            print(node, '->', neighbors)

def findChampions(graph):
    champions = []
    for node in graph.adjacency_list:
        visited = set()
        DFS(node, visited, graph.adjacency_list)
        if len(visited) == len(graph.adjacency_list):
            champions.append(node)
    print(f"Champions: {champions}")
    return champions

def DFS(node, visited, graph):
    if node not in visited:
        visited.add(node)
        for neighbor in graph[node]:
            DFS(neighbor, visited, graph)

def print_groups(groups):
    # Output the groups
    print("Groups divided based on nodes that have defeated each other:")
    for i, group in enumerate(groups, 1):
        print(f"Group {i}: {sorted(group)}")

if __name__=="__main__":
    graph= Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'A')
    graph.add_edge('A', 'D')
    graph.add_edge('D', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('D', 'C')
    graph.add_edge('C', 'E')
    graph.add_edge('C', 'F')
    graph.add_edge('F', 'E')
    graph.add_edge('E', 'G')
    graph.add_edge('G', 'F')
    graph.print_graph()

    findChampions(graph)

    # Dividing the graph into groups
    groups = divide_into_groups(graph.adjacency_list)
    print_groups(groups)


