import csv
import sys
import numpy as np
import Dijkstras_Algorithm as Dijkstras
from datetime import datetime

def main():
    header = ['Trial', 'n', 'l', 'alpha', 'StartVertex', 'EndVertex', 'FirstPassageTime', 'Distance'] 
    with open('data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)

    n = 10000 # 10 thousand vertices
    l = n/100 # shortcut neighbors
    p = 0.7 # probability of shortcut
    for i in range(1000): # 1 thousand trials
        #Trial n l p start_vertex, end_vertex
        sys.argv = [i, n, l, p, 0, int(n/2)]
        with open("ER_graph.py", "r") as f:
            exec(f.read())

if __name__ == "__main__":
    main()
