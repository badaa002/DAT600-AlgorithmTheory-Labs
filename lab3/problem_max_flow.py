def divide_into_groups(graph):
    # DFS to find SCCs
    def dfs(node, visited, closure, stack):
        visited.add(node)
        for neighbor in closure[node]:
            if neighbor not in visited:
                dfs(neighbor, visited, closure, stack)
        stack.append(node)

    # Reverse the direction of edges
    def transpose(graph):
        transposed_graph = {node: [] for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                transposed_graph[neighbor].append(node)
        return transposed_graph

    # Find SCCs using Kosaraju's algorithm
    def kosaraju_scc(graph):
        visited = set()
        stack = []
        for node in graph:
            if node not in visited:
                dfs(node, visited, graph, stack)

        transposed = transpose(graph)
        visited.clear()
        scc_groups = []
        while stack:
            node = stack.pop()
            if node not in visited:
                scc_group = []
                dfs(node, visited, transposed, scc_group)
                scc_groups.append(scc_group)
        return scc_groups

    # Create the transitive closure of the graph
    transitive_closure = {node: set() for node in graph}
    for node in graph:
        visited = set()
        stack = [node]
        while stack:
            current_node = stack.pop()
            if current_node not in visited:
                visited.add(current_node)
                for neighbor in graph[current_node]:
                    # Current node in its own transitive closure
                    transitive_closure[node].add(current_node)
                    transitive_closure[node].add(neighbor)
                    stack.append(neighbor)



    # Identify SCCs in the transitive closure and merging into groups
    scc_groups = kosaraju_scc(transitive_closure)
    groups = [sorted(set(group)) for group in scc_groups]

    return groups
