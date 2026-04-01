
from tkinter import *
import sys

class Plot(Frame):
    def __init__(self, master=None,width=800,height=500,grid_size=30):
        super().__init__(master)

        self.width = width
        self.height = height
        self.grid_size = grid_size

        self.canvas = Canvas(self,width=self.width,height=self.height)
        self.canvas.pack(fill="both", expand=True)

        self.desenhar_grid()

    def desenhar_grid(self):
        meio_x = self.width/2 + (self.width % self.grid_size)
        meio_y = self.height/2 + (self.height % self.grid_size)

        for x in range(0, self.width, self.grid_size):
            self.canvas.create_line(x, 0, x, self.height, fill="#E0E0E0",width=3 if x == meio_x else 1)


        for y in range(0, self.height, self.grid_size):
            self.canvas.create_line(0, y, self.width, y, fill="#E0E0E0",width=3 if y == meio_y else 1)

    def draw_line(self, xan, yan, xbn, ybn,color="black"):

        xa, ya = self._normalize_coords(xan, yan)
        xb, yb = self._normalize_coords(xbn, ybn)

        self.canvas.create_line(xa, ya, xb, yb, fill=color)
        
    def draw_point(self,xn,yn):

        x,y = self._normalize_coords(xn, yn)

        self.canvas.create_oval(x-1, y-1, x+1, y+1, fill="black")

    def draw_obj(self, object):
        object.transform()
        transformado = object.get_pontos()

        #for ar, br in zip(transformado, transformado[1:]):
        #    a = ar.get_global_pos()
        #    b = br.get_global_pos()
        #    self.draw_line(a[0],a[1],b[0],b[1])
        #self.draw_line(transformado[0].get_global_pos()[0],transformado[0].get_global_pos()[1],transformado[-1].get_global_pos()[0],transformado[-1].get_global_pos()[1])  
         
        tupla_transformado = self.points_to_polygon(transformado)
        self.canvas.create_polygon(tupla_transformado,outline="black",fill=object.get_cor())

    def _normalize_coords(self, x, y):
        x = (self.grid_size * x) + (self.width % self.grid_size) + self.width/2
        y = (self.grid_size * -y ) + (self.height % self.grid_size) + self.height/2
        return x,y
        
    def clear(self):
        self.canvas.delete("all")
        self.desenhar_grid()

    def points_to_polygon(self,points):
        r = []
        for p in points:
            pos_x,pos_y = self._normalize_coords(p.get_global_pos()[0],p.get_global_pos()[1])
            r.append((pos_x,pos_y))

        return r