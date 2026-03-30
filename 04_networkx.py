import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph(directed=True)
G.add_node(1, label='A', color="lightblue")
G.add_node(2, label='B', color="white")
G.add_node(3, label='C', color="lightblue")
G.add_node(4, label='D', color="lightblue")
G.add_node(5, label='E', color="lightblue")
G.add_node(6, label='F', color="lightblue")

G.add_edge(1, 2, weight=4, color="black")
G.add_edge(1, 3, weight=2, color="blue")
G.add_edge(2, 3, weight=5, color="black")
G.add_edge(2, 4, weight=10, color="black")
G.add_edge(3, 5, weight=3, color="blue")
G.add_edge(5, 4, weight=4, color="blue")
G.add_edge(4, 6, weight=11, color="blue")

pos = nx.bfs_layout(G, 1, align="vertical")

node_colors = nx.get_node_attributes(G, 'color').values()
nodes = nx.draw_networkx_nodes(G, pos, node_shape="o", node_size=1000, node_color=node_colors)
nodes.set_edgecolor("black")

edge_colors = nx.get_edge_attributes(G,'color').values()
nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=25, width=3, edge_color=edge_colors)

node_labels = nx.get_node_attributes(G, 'label')
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=16)

edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="black")

pAtoE = nx.shortest_path(G, source=1, target=5, weight="weight")
print("Shortest path:")
for i in range (len(pAtoE)):
    print(node_labels[pAtoE[i]])

plt.show()