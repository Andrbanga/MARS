import random
import networkx as nx

import matplotlib.pyplot as plt
import matplotlib.patches as patches

from Leaf import Leaf
from math import hypot


class Tree():
    def __init__(self, n, m):
        self.list_leafs = []
        self.list_leafs.append(Leaf(n, m, 0, 0))

        did_split = True
        while did_split:
            did_split = False
            list_ = []
            for vert in self.list_leafs:
                if vert.width > vert.max_size or vert.height > vert.max_size or random.random() > 0.25:
                    if vert.split():
                        list_.append(vert.lchild)
                        list_.append(vert.rchild)
                        did_split = True
                    else:
                        list_.append(vert)
                else:
                    list_.append(vert)

            self.list_leafs = list_

        print ("binary splitted space created")

    def graph_to_lines(self, graph):
        lines = []
        for e in graph.edges:
            x1, x2 = list(list(e)[0])[0], list(list(e)[1])[0]
            y1, y2 = list(list(e)[0])[1], list(list(e)[1])[1]
            lines.append([[x1, y1], [x1, y2]])
            lines.append([[x1, y2], [x2, y2]])

        return lines


    def visualize_graph(self, graph, field_width, field_height):
        fig = plt.figure()
        ax = fig.add_subplot(111)

        for e in graph.edges:
            x1, x2 = list(list(e)[0])[0], list(list(e)[1])[0]
            y1, y2 = list(list(e)[0])[1], list(list(e)[1])[1]
            plt.plot([x1, x2], [y1, y2])

        for vertex in self.list_leafs:
            ax.add_patch(patches.Rectangle((vertex.x, vertex.y), vertex.width, vertex.height, fill=False, color="red", alpha=1.0, lw=4.0))

        plt.xlim(0, field_width)
        plt.ylim(0, field_height)

        plt.grid(True)

        plt.show()

    def visualize(self, field_width, field_height):
        fig = plt.figure()
        ax = fig.add_subplot(111)
    
        for vertex in self.list_leafs:
            ax.add_patch(patches.Rectangle((vertex.x, vertex.y), vertex.width, vertex.height, fill=False, color="red", alpha=1.0, lw=4.0))

        plt.xlim(0, field_width)
        plt.ylim(0, field_height)

        plt.grid(True)

        plt.show()

        print ("the end!")

    def visualize_all(self, graph, array, field_width, field_height):
        fig = plt.figure()
        ax = fig.add_subplot(111)

        # plot all edges
        for e in graph.edges:
            x1, x2 = list(list(e)[0])[0], list(list(e)[1])[0]
            y1, y2 = list(list(e)[0])[1], list(list(e)[1])[1]
            plt.plot([x1, x2], [y1, y2])
    
        # plot rectangles
        for vertex in self.list_leafs:
            ax.add_patch(patches.Rectangle((vertex.x, vertex.y), vertex.width, vertex.height, fill=False, color="red", alpha=1.0, lw=4.0))

        # plot bool array
        plt.imshow(array, interpolation='none', cmap='gray')


        plt.xlim(0, field_width)
        plt.ylim(0, field_height)

        plt.grid(True)

        plt.show()

        print ("the end!")

    def create_graph(self):
        graph = nx.Graph()

        for leaf in self.list_leafs:
            # graph.add_node(leaf)
            for leaf_ in self.list_leafs:
                if leaf_ == leaf:
                    continue
                if leaf.make_bigger().intersects(leaf_.poly):
                    x1, x2 = leaf.centre_x_wf, leaf_.centre_x_wf
                    y1, y2 = leaf.centre_y_wf, leaf_.centre_y_wf

                    length = hypot(x1 - x2, y1 - y2)
                    v1, v2 = (x1, y1), (x2, y2)
                    graph.add_edge(v1, v2, weight=length)
            
        print ("graph created")
        return graph