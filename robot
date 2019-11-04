# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 22:54:44 2019

@author: Mi
"""

import numpy as np
import matplotlib.pyplot as plt 


#%%

class Mobile_Robot:
  def __init__(self, x_start, y_start, map_, technograph=None):
    self.x = x_start
    self.y = y_start
    self.map = map_
    self.map_shape = map_.shape
    #self.current_task = None #????
    #pass
  
  def getxy(self):
    return self.x, self.y
  
  
  def sense(self):
    if self.x != 0 and self.y != 0 and self.x != self.map_shape[0] and self.y != self.map_shape[1]:
      #условие на границы карты
      # добавить другие варианты
      p1 = self.map[self.y, self.x + 1]
      p3 = self.map[self.y, self.x - 1]
      p4 = self.map[self.y + 1, self.x]
      p2 = self.map[self.y - 1, self.x]
      
      return np.array([p1, p3, p4, p2]), np.array([[self.x + 1, self.x - 1, self.x, self.x], [self.y, self.y, self.y + 1, self.y - 1]])
    else:
      print('Ууу бля')
      
  
  def move(self, new_x, new_y):
    #print(self.x, self.y)
    self.x = new_x
    self.y = new_y
    #print(self.x, self.y)
  

#  FIX IT  
# добавить указание на старые точки ибо он прыгает от новой к старой
    
    
  def solver(self, res, coor):
    ind = np.argwhere(res == 1)[0]
    if ind.size > 1:
      pass
      #развилка
    elif ind.size == 0:
      pass
      # тупик 
    else:
      robot1.move(coor[0, ind[0]], 
                  coor[1, ind[0]])

    
  def work(self):
    self.sense()
    ind = np.where(out == 1)[0]
    print(ind)
    if ind.size > 1:
      pass
      #развилка
    elif ind.size == 0:
      pass
      # тупик 
    else:
      print('need to move')

#    if (p1 or p2) or (p2 or p3) or (p1 or p3):
#      pass
#      # коридор
#    
#    elif not all(p1, p2, p3):
#      pass
#      # варинат с тупиком 
#      # надо отметить в техн графе а что ДАЛЬШЕ?
#    
#    else:
#      pass
#      #перекресток с 3 дорогами
#      # 
      
  def main(self):
    self.work()
    
       
      

#%%%

mapp = np.zeros((15, 15), np.int32)

mapp[3, 3:12] = 1.
mapp[3:9, 3] = 1.

x_st = 3
y_st = 3
mapp[x_st, y_st+1]
mapp

def vis(_map, i, x, y):
  plt.figure(i, facecolor='w',figsize=(7,7))
  dmin,dmax = 0, 15
  plt.scatter(x, y)
  plt.imshow(mapp, vmin=dmin, vmax=dmax)



robot1 = Mobile_Robot(x_start=3, y_start=8, map_=mapp)
robot1.getxy()
vis(mapp, 1, 3, 8)

for i in range(5):
  x, y = robot1.getxy()
  print(x, y)
#  plt.figure(i, facecolor='w',figsize=(7,7))
#  dmin,dmax = 0, 15
#  plt.scatter(x, y)
#  plt.imshow(mapp, vmin=dmin, vmax=dmax)

  res, coor = robot1.sense()
  robot1.solver(res, coor)
  
  
