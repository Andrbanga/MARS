# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 14:23:31 2019

@author: Mi

"""


class Graph:
    def __init__(self):
        self.g = dict()
    
    def add_vertex(self, q): #*q):
#        if q not in self.g.keys():
#            for qq in q:
#                self.g[qq] = {}
        for node in q:
            if node not in self.g.keys():
                self.g[node] = {}
                
                
    def add_edge(self, q1, q2, feedback=False, weight=None):
        self.add_vertex(q1)
        self.add_vertex(q2)
        #print(self.g)
        self.g[q1][q2] = weight
        if feedback:
            self.g[q2][q1] = weight
             

    def remove_vertex(self, q):
        if q in self.g:
            for node in self.g[q].keys():
                self.g[node].pop(q)    
            self.g.pop(q)
        
        
    def remove_edge(self, q1, q2):
        if q1 in self.g.keys() and q2 in self.g.keys():
            self.g[q1].pop(q2)
            self.g[q2].pop(q1)
        
    
    def info(self):
        print(self.g.keys())
        print(self.g.values())
        
    
    def BFS(self, start_q, goal_q):
        # типо работает
        print('1st key in keys {0}'.format(start_q in self.g.keys()))
        if start_q in self.g.keys() and goal_q in self.g.keys():
            print('keys equal {0}'.format(start_q == goal_q))
            if start_q == goal_q:
                
                return True
            
            queue = []
            visited_nodes = []
            queue.extend(start_q)
            
            while not len(queue) == 0:
                curr_node = queue.pop()
                visited_nodes.append(curr_node)
                if curr_node == goal_q:
                    #print(visited_nodes)
                    return True
                else:
                    for k in self.g[curr_node].keys():
                        if k not in queue and k not in visited_nodes:
                            queue.extend(k)
                            
            return False
        
        else: 
            return False


    def DFS():
        pass
    
    def Dejkstra():
        pass

##############
### TEST 
##############

g = Graph()


nodes = ["A", "B : A", "C : A", "D : B C"]

#%%
def graph_(g, nodes):
    for node in nodes:
        if ':' in node:
            child, t = node.split(':')
            parents = t.strip().split(' ')
            
            for parent in parents:
                g.add_edge(parent.strip(), child.strip())
        else:
            g.add_vertex(node.strip())
    

#%%
graph_(g, nodes)
g.info()


print(g.BFS('A', 'B'))
print(g.BFS('B', 'D'))
print(g.BFS('C', 'D'))
print(g.BFS('D', 'A'))



#g.add_vertex('g', 'h', 'j', 'k')
#g.info()
#g.add_vertex('q')
#g.info()
#
#g.add_vertex('a')
#g.add_vertex('b')
#g.add_vertex('d')
#g.add_edge('a', 'c')
#g.add_edge('b', 'd')
#g.add_edge('d', 'e')
#g.info()
##g.remove_vertex('d')
#g.info()






#%%

test_node = [
    'G : F',  
    'A',
    'B : A',
    'C : A',
    'D : B C',
    'E : D',
    'F : D',
    'X',
    'Y : X A',  
    'Z : X',
    'V : Z Y',
    'W : V',
    ]

test_question = ['A G',      # Yes   # A предок G через B/C, D, F
                'A Z',      # No    # Y потомок A, но не Y
                'A W',      # Yes   # A предок W через Y, V
                'X W',      # Yes   # X предок W через Y, V
                'X QWE',    # No    # нет такого класса QWE
                'A X',      # No    # классы есть, но они нет родства :)
                'X X',      # Yes   # родитель он же потомок
                '1 1',      # No    # несуществующий класс
                ]


def check(g, quest):
    for que in quest:
        p, c = que.split(' ')
        print(g.BFS(p, c))


m = Graph()
m.info()
graph_(m, test_node)
m.info()


check(m, test_question)

print('out {0}'.format(m.BFS('1', '1')))



#%%

class Nav_Graph:
  def __init__(self):
    self.g = dict()
    self.map = dict()
  
  def add_vertex(self, q, x_q, y_q):
    if q not in self.g.keys():
      self.g[q] = {}
      self.map[q] = (x_q, y_q)
      return True
    else:
      return False
              
  def get_dist(self, q1, q2):
    x1, y1 = self.map[q1]
    x2, y2 = self.map[q2]
    # euclidian distance
    return ((x2-x1)**2 + (y2-y1)**2)**0.5
     
              
  def add_edge(self, q1, q2, feedback=True, autoweight=True):
    self.add_vertex(q1)
    self.add_vertex(q2)
    if autoweight:
      l = self.get_dist(q1, q2)
      self.g[q1][q2] = l
    if feedback:
        self.g[q2][q1] = l

  def remove_vertex(self, q):
    if q in self.g:
        for node in self.g[q].keys():
            self.g[node].pop(q)    
        self.g.pop(q)
      
      
  def remove_edge(self, q1, q2):
    if q1 in self.g.keys() and q2 in self.g.keys():
        self.g[q1].pop(q2)
        self.g[q2].pop(q1)
      
  
  def info(self):
    print(self.g.keys())
    print(self.g.values())
    
  def mapinfo(self):        
    print(self.map.keys())
    print(self.map.values())
    


##############
### TEST 
##############

nav = Nav_Graph()
nav.add_vertex('a0', 0, 1)
nav.add_vertex('b0', 3, 0)
nav.add_vertex('c0', 5, 2)
nav.add_vertex('d0', 0, -1)
nav.add_vertex('e0', 2, 1)
nav.add_vertex('f0', 3, -1)


nav.info()

nav.mapinfo()
