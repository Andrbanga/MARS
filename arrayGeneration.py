import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from Leaf import Leaf
from Tree import Tree


field_width = 30
field_height = 30


def createMap(n, m):
    tree = Tree(n, m)
    graph = tree.create_graph()
    graph_ = nx.algorithms.tree.mst.minimum_spanning_tree(graph)

    array = lines_to_array(tree.graph_to_lines(graph_), n, m)
    
    # tree.visualize_all(graph_, array, field_width, field_height)

    plt.imshow(array, interpolation='none', cmap='gray')

    plt.xlim(0, field_width)
    plt.ylim(0, field_height)

    plt.grid(True)

    plt.show()


    return array

def lines_to_array(lines, n, m):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    array = np.zeros((n, m), dtype=bool)

    for line in lines:
        x1, x2 = line[0][0], line[1][0] 
        y1, y2 = line[0][1], line[1][1] 
        # plt.plot([x1, x2], [y1, y2])

        if x1 > x2:
            a = x2
            x2 = x1
            x1 = a

        if y1 > y2:
            a = y2
            y2 = y1
            y1 = a
        
        for i in range(x1, x2 + 1):
            array[y1][i] = True
        for i in range(y1, y2 + 1):
            array[i][x2] = True
        
    return array

def visualize_lines(lines):
    fig = plt.figure()
    ax = fig.add_subplot(111)

    for line in lines:
        # plt.plot([x1, x2], [y1, y2])
        x1, x2 = line[0][0], line[1][0] 
        y1, y2 = line[0][1], line[1][1] 
        plt.plot([x1, x2], [y1, y2])

    plt.xlim(0, field_width)
    plt.ylim(0, field_height)

    plt.grid(True)

    plt.show()

def main():
    # size of field n x m
    createMap(field_width, field_height)


if __name__ == '__main__':
  main()