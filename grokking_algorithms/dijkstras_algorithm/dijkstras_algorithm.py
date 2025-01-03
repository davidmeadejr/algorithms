"""
Problem: Find the Shortest Path in a Weighted Graph using Dijkstra's Algorithm

You are given a weighted, directed graph represented as a dictionary, where each node
has a dictionary of neighboring nodes and the associated edge weights. Your task is to 
find the shortest path from a given start node to all other nodes using Dijkstra's algorithm.

Graph Representation:
The graph is represented as a dictionary of dictionaries, where each key is a node, and 
its value is another dictionary representing the neighboring nodes and their respective weights.

Example:
graph = {
    "start": {"a": 6, "b": 2},
    "a": {"fin": 1},
    "b": {"a": 3, "fin": 5},
    "fin": {}
}

In this example:
- "start" connects to "a" with a weight of 6, and to "b" with a weight of 2.
- "a" connects to "fin" with a weight of 1.
- "b" connects to "a" with a weight of 3, and to "fin" with a weight of 5.
- "fin" has no outgoing edges.

Given an initial costs table for each node's cost to reach from the start node, a parents
table to track the paths, and a list to track the processed nodes, implement Dijkstra's algorithm 
to find the shortest path to each reachable node from the start.

Implement the following functions:

1. `find_lowest_cost_node(costs)`: A helper function to find the unprocessed node with the 
   lowest cost.
2. `dijkstra()`: The main function implementing Dijkstra's algorithm to update the costs and 
   parents tables for the shortest paths in the graph.

Function Signatures:
- `find_lowest_cost_node(costs: dict) -> str`
- `dijkstra() -> Tuple[dict, dict]`

The `dijkstra` function should return:
- `costs`: A dictionary with the lowest cost to reach each node from the start.

Constraints:
- All edge weights are non-negative.
- The graph may contain up to 1000 nodes and 10,000 edges.
- If a node is unreachable from the start, its cost remains set to infinity.

Example:
Input:
    graph = {
        "start": {"a": 6, "b": 2},
        "a": {"fin": 1},
        "b": {"a": 3, "fin": 5},
        "fin": {}
    }

    costs = {
        "a": 6,
        "b": 2,
        "fin": float("inf")
    }

    parents = {
        "a": "start",
        "b": "start",
        "fin": None
    }

Output:
    ({'a': 5, 'b': 2, 'fin': 6}, {'a': 'b', 'b': 'start', 'fin': 'a'})
"""

# Setup for the problem
# Graph setup with weights
graph = {
    "start": {"a": 6, "b": 2},
    "a": {"fin": 1},
    "b": {"a": 3, "fin": 5},
    "fin": {}
}

# Initialize costs table with initial costs from the start node
infinity = float("inf")
costs = {
    "a": 6,
    "b": 2,
    "fin": infinity
}

# Initialize parents table to track paths
parents = {
    "a": "start",
    "b": "start",
    "fin": None
}

# Implementation: 12

# List to track processed nodes
processed = []


# Write code below this line:
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        if costs[node] < lowest_cost and node not in processed:
            lowest_cost = costs[node]
            lowest_cost_node = node
    return lowest_cost_node


def dijkstra():
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbours = graph[node]
        for n in neighbours:
            new_cost = cost + neighbours[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

    return costs

print(dijkstra())



