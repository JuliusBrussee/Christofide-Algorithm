import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
 
# Load the dataset from the Excel file
file_path = 'insert_file_path'
data = pd.read_excel(file_path, sheet_name='Sheet1')
data.set_index(data.columns[0], inplace=True)
 
# Create a complete graph from the distance matrix
G = nx.Graph()
for i, row in data.iterrows():
    for j, weight in row.items():
        if i != j and not pd.isna(weight):  # Check to ensure there is a valid distance
            G.add_edge(i, j, weight=weight)
 
# Create the Minimum Spanning Tree (MST)
mst_tree = nx.minimum_spanning_tree(G)
 
odd_degree_nodes = [v for v, degree in mst_tree.degree() if degree % 2 != 0]
 
odd_node_subgraph = G.subgraph(odd_degree_nodes)
 
matching = nx.algorithms.matching.min_weight_matching(odd_node_subgraph)
 
# Add the matching edges to the MST
mst_tree.add_edges_from(matching)
 
# Create an Eulerian circuit
eulerian_circuit = list(nx.eulerian_circuit(mst_tree))
 
# Convert the Eulerian circuit to a Hamiltonian circuit (a TSP solution)
hamiltonian_circuit = []
visited = set()
for u, v in eulerian_circuit:
    if u not in visited:
        hamiltonian_circuit.append(u)
        visited.add(u)
 
# Add the last connection back to the starting node
if hamiltonian_circuit[0] != hamiltonian_circuit[-1]:
    hamiltonian_circuit.append(hamiltonian_circuit[0])
 
# \calculate the length
circuit_length = sum(G[u][v]['weight'] for u, v in zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))
 
# Visualize the final Hamiltonian circuit
plt.figure(figsize=(12, 6))
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
# Highlight the Hamiltonian circuit
edges_in_circuit = list(zip(hamiltonian_circuit[:-1], hamiltonian_circuit[1:]))
nx.draw_networkx_edges(G, pos, edgelist=edges_in_circuit, edge_color='r', width=2)
plt.title('Hamiltonian Circuit based on Christofides Algorithm')
plt.show()
 
# output
print("Hamiltonian Circuit:", hamiltonian_circuit)
print("Length of the Hamiltonian Circuit:", circuit_length)
