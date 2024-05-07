import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

file_path = 'insert_file_path'
data = pd.read_excel(file_path, sheet_name='insert_sheet_name')
data.set_index(data.columns[0], inplace=True)

data_filled = data.fillna(0)

G_filled = nx.Graph()
for i, location in enumerate(data_filled.index):
    for j, destination in enumerate(data_filled.columns):
        if i != j:
            # Adding an edge between each pair of locations with the distance as the weight
            G_filled.add_edge(location, destination, weight=data_filled.iloc[i, j])

mst_filled = nx.minimum_spanning_tree(G_filled)

# Visualizing the updated MST and the complete graph
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
pos_filled = nx.spring_layout(G_filled)  # positions for all nodes
nx.draw(G_filled, pos_filled, with_labels=True, font_weight='bold', node_size=700, node_color="lightblue")
plt.title("Complete Graph (Updated)")

# Plotting the MST
plt.subplot(1, 2, 2)
nx.draw(mst_filled, pos_filled, with_labels=True, font_weight='bold', node_size=700, node_color="lightgreen")
plt.title("Minimum Spanning Tree (Updated)")

plt.show()
print("Script ended")
