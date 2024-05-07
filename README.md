# Christofide-Algorithm

## Introduction

This repository contains Python code for solving the Traveling Salesman Problem (TSP) using Christofides' algorithm. This project is part of my International Baccalaureate Mathematics Internal Assessment (Math IA), focusing on determining the most efficient route for a delivery vehicle among a set of addresses.

## Algorithm Overview

Christofides' algorithm is employed to find an approximate solution to the TSP. The algorithm is well-regarded for its performance guarantee, offering a solution within 1.5 times the optimal route length. The implementation follows these key steps:

1. **Graph Construction**: Build a complete graph where nodes represent addresses and edges represent distances between them.
2. **Minimum Spanning Tree (MST)**: Compute an MST to minimize the sum of edge weights. Using the MSTplotting.py file you can also print a diagram of the Minimum Spanning Tree if it is necessary.
3. **Perfect Matching**: Identify nodes with odd degrees and find a minimum weight perfect matching to achieve an Eulerian graph.
4. **Eulerian Circuit**: Formulate an Eulerian circuit that visits each edge exactly once.
5. **Hamiltonian Circuit**: Convert the Eulerian circuit to a Hamiltonian circuit by avoiding revisits to the already visited nodes.

## Installation and Usage

### Dependencies

- Python 3.x
- Libraries: `pandas`, `networkx`, `matplotlib`

### Setup

Install the required libraries:

```bash
pip install pandas networkx matplotlib
```

### Execution

1. Modify the `file_path` variable in the script to point to your Excel file containing the distance matrix.
2. Execute the script to compute the route and visualize the Hamiltonian circuit.

## Visualization

The final output includes a visual representation of the Hamiltonian circuit and the calculation of its total length, displayed through a matplotlib plot.

## License

This project is licensed under the MIT License.

## Contact

For inquiries or issues, please open an issue on this GitHub repository.
