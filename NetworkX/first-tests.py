#
import networkx as nx
##from matplotlib import pyplot as plt
from pyvis.network import Network

G = nx.Graph()
G.add_node('A')
G.add_nodes_from(['B', 'C'])
G.add_edge('A', 'B')
G.add_edges_from([('B', 'C'), ('A', 'C')])

#plt.figure(figsize=(6, 6))
nx.draw_networkx(G)
#plt.show()

nt = Network('500px', '500px')
nt.from_nx(G)
nt.show('nx_simple.html')
