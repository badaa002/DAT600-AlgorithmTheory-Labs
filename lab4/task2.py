from networkx import DiGraph, maximum_flow

# Creating the flow network graph, G 
G = DiGraph()
edges = [('S', 'V1', {'capacity': 14}), ('V1', 'V4', {'capacity': 21}), ('V1', 'V3', {'capacity': 6}), ('V3', 'V1', {'capacity': 3}), ('V4', 't', {'capacity': 20}), ('V4', 'V3', {'capacity': 10}), ('S', 'V2', {'capacity': 25}), ('V2', 'V3', {'capacity': 13}), ('V2', 'V5', {'capacity': 7}), ('V5', 't', {'capacity': 10}), ('V3', 'V5', {'capacity': 15}), ('V5', 'V4', {'capacity': 5})]
G.add_edges_from(edges)

# Finding maximum flow
flow_value, flow_dict = maximum_flow(G, 'S', 't')

# Finding bottleneck cut & checking if edges are fully utilized
bottleneck_cut = [(u, v) for u, neighbors in flow_dict.items() for v, flow in neighbors.items() if flow > 0]
fully_utilized_edges = [(u, v) for u, v in bottleneck_cut if flow_dict[u][v] == G[u][v]['capacity']]

print("Bottleneck cut:", bottleneck_cut)
print("Fully utilized edges in bottleneck cut:", fully_utilized_edges)
print("Maximum flow:", flow_value)
