import numpy as np
import numpy.random as rd
import matplotlib.pyplot as plt

class Point : 
    def _init_(self,x,y):
        self.x=x
        self.y=y
    
    def clockwise(a,b,c):
        if (b.y-a.y)(c.x-b.x)-(b.x-a.x)(c.y-b.y)>0: return True 
        else: return False 
    
