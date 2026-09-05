import heapq
import random

#from ER_graph_simulation import graph_vertices
#from ER_graph_simulation import n


def dijkstra(graph, graph_vertices, n):
    distances = [float('inf')] * n
    predecessors = [None] * n
    distances[0] = 0
    visited = [False] * n
    for _ in range(n):
        min_distance = float('inf')
        u = None
        for i in range(n):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                u = i

        if u is None:
            break
        if u == n//2:
            break

        visited[u] = True

        for v in range(n):
            if graph[u][v] != 0 and not visited[v]:
                alt = distances[u] + graph[u][v]
                if alt < distances[v]:
                    if u == 'None':
                        print("aaaaaaaaa")
                    distances[v] = alt
                    predecessors[v] = u

    return distances, predecessors
