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
    self.x_prev = None
    self.y_prev = None
    self.map = map_
    self.map_shape = map_.shape
    #self.current_task = None #????

  
  def getxy(self, prev=False):
    if prev:
      return self.x, self.y, self.x_prev, self.y_prev  
    else:
      return self.x, self.y
  
  def find(self, coor):
    if self.x_prev != None and self.x_prev != None:
      arg_x = np.argwhere(coor[0, :] == self.x_prev)[0]
      arg_y = coor[1, arg_x[:]] == self.y_prev
      del_ind = arg_x[np.where(arg_y == True)[0]]
      return np.delete(coor, del_ind, 1)    
    else:
      return coor
    
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
    self.x_prev = self.x
    self.y_prev = self.y
    self.x = new_x
    self.y = new_y
        
    
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
    # один рабочий цикл
    res, coor = self.sense()
    coor_upd = self.find(coor)
    self.solver(res, coor_upd)
    
    
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


def vis(_map, x, y, i, save=False):
  plt.figure(i, facecolor='w',figsize=(7,7))
  dmin,dmax = 0, 15
  plt.scatter(x, y, color='magenta')
  img = plt.imshow(mapp, vmin=dmin, vmax=dmax, animated=True)
  if save:
    plt.savefig('iter_{0}'.format(i), dpi=200)
  return img 


robot1 = Mobile_Robot(x_start=3, y_start=8, map_=mapp)

for i in range(10):
  x1, y1 = robot1.getxy()
  print(x1, y1)
  vis(mapp, x1, y1, i)
  res, coor = robot1.sense()
  coor_upd = robot1.find(coor)
  robot1.solver(res, coor_upd)
  print(robot1.getxy(True))
  
 
  
