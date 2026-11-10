from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """

    # Initialize distances and edge counts
    best = {v: (float('inf'), float('inf')) for v in graph}
    best[source] = (0, 0)

    # Priority queue: (distance, number_of_edges, counter, vertex)
    pq = [(0, 0, 0, source)]
    counter = 0

    while pq:
        dist, edges, _, vertex = heappop(pq)

        # Skip outdated entries
        if (dist, edges) != best[vertex]:
            continue

        # Examine each neighboring vertex
        for neighbor, weight in graph[vertex]:
            new_dist = dist + weight
            new_edges = edges + 1

            # Update if path is shorter, or same weight with fewer edges
            if (new_dist, new_edges) < best[neighbor]:
                best[neighbor] = (new_dist, new_edges)
                counter += 1
                heappush(pq, (new_dist, new_edges, counter, neighbor))

    return best

    
