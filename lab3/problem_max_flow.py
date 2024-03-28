def divide_into_groups(graph):
    # Function to perform depth-first search (DFS) to identify strongly connected components (SCCs)
    def dfs(node, visited, closure, stack):
        visited.add(node)
        for neighbor in closure[node]:
            if neighbor not in visited:
                dfs(neighbor, visited, closure, stack)
        stack.append(node)

    # Function to transpose the graph (reverse the direction of edges)
    def transpose(graph):
        transposed_graph = {node: [] for node in graph}
        for node in graph:
            for neighbor in graph[node]:
                transposed_graph[neighbor].append(node)
        return transposed_graph

    # Function to identify SCCs using Kosaraju's algorithm
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
                    transitive_closure[node].add(neighbor)
                    stack.append(neighbor)

    # Print transitive closure for debugging
    print("Transitive Closure:")
    for node, neighbors in transitive_closure.items():
        print(f"{node}: {neighbors}")

    # Identify SCCs in the transitive closure
    scc_groups = kosaraju_scc(transitive_closure)

    # Print SCCs for debugging
    print("\nStrongly Connected Components (SCCs):")
    for i, group in enumerate(scc_groups, 1):
        print(f"Group {i}: {sorted(group)}")

    # Function to merge SCCs into groups based on mutual connections
    def merge_groups(graph, scc_groups):
        merged_groups = []
        visited = set()
        for group in scc_groups:
            merged_group = []
            for node in group:
                if node not in visited:
                    merged_group.append(node)
                    visited.add(node)
            merged_groups.append(merged_group)
        return merged_groups

    # Merge SCCs into groups based on mutual connections
    groups = merge_groups(graph, scc_groups)

    return groups






