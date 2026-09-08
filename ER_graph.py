import sys
import csv
import numpy as np

import Dijkstras_Algorithm as Dijkstras

'''
    @params
    Trial n l alpha start_vertex end_vertex random seed

'''
def main():
    # parameters
    trial = sys.argv[0]
    n = sys.argv[1]
    l = sys.argv[2]
    alpha = sys.argv[3]
    p = alpha/n
    start_vertex = sys.argv[4]
    end_vertex = sys.argv[5]

    # random graph
    r = np.random.default_rng(seed=123)
    A = np.zeros((n, n), dtype=int)
    # data for csv Trial, n, l, alpha, FirstPassageTime, Distance
    data = [1, n, l, alpha, start_vertex, end_vertex]
    for i in range(n):
        j = (i + 1) % n
        A[i, j] = 1
        A[j, i] = 1

    # generating shortcuts
    shortcuts = []

    for i in range(n):
        for j in range(i+1, n): # j > i
            distance = min((j-i), n - (j-i))

            if (2 <= distance <= l):
                if r.random() < p:
                    A[i, j] = 1
                    A[j, i] = 1
                    shortcuts.append((i, j))

    cycle_edges = []
    for i in range(n):
        cycle_edges.append((i, (i+1)%n))


    graph_vertices = []
    for i in range(n):
        graph_vertices.append(i)


    
    distances, predecessors = Dijkstras.dijkstra(A, graph_vertices, n)

    # calculate shortest path
    path = Dijkstras.get_path(
        predecessors,
        start_vertex,
        end_vertex
    )

    # calculate FirstPassageTime
    FirstPassageTime=0
    for i in range(len(path)-1):
        FirstPassageTime += A[path[i], path[i+1]]
    data.append(FirstPassageTime)

    # calculate optimal path distance
    data.append(len(path)-1)

    # write data to csv file
    with open('data.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        writer.writerow(data)

    
if __name__ == "__main__":
    main()
