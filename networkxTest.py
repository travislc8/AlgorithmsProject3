import networkx as nx

g = nx.Graph()
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)

g.add_edge(1, 2, weight=10)
g.add_edge(1, 3, weight=25)
g.add_edge(1, 4, weight=10)
g.add_edge(1, 1, weight=40)
g.add_edge(2, 3, weight=5)
g.add_edge(3, 4, weight=7)

sp = dict(nx.all_pairs_dijkstra(g))
print("nodes", list(g.nodes))
print("edges", list(g.edges))
print("shortest path from node 1 to n: ", list(sp[1]))
