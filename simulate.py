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

    #number vertices
    n = 100
    for i in range(10):
        sys.argv = [i, n, int(n/2), 2, 0, int(n/2)]
        with open("ER_graph.py", "r") as f:
            exec(f.read())

if __name__ == "__main__":
    main()
