from EDs.ponto import Ponto
from EDs.objeto import Objeto
import scanner
from tkinter import *
from plot import Plot
from inspector import Inspector
import time

gato = scanner.carregar_objeto("gato.txt")
print(f"Grupos carregados: {list(gato.keys())}")
print(f"Grupos carregados: {list(gato.items())}")

root = Tk()
mainframe = Frame(root)
mainframe.pack(fill="both", padx=5, pady=5)

net = Plot(mainframe)
net.pack(side="left", fill="both", expand=True)

objects = []
objects_dict = {}

for key in gato.keys():
    corpo = gato.get(key)
    objects.append(corpo)

    print(f"{key}:{corpo}")
    objects_dict[key] = corpo
   

for _,obj in objects_dict.items():
    net.draw_obj(obj)

inspector = Inspector(mainframe,objects_dict,net)
inspector.pack(side="right", fill="y", expand=True)

#teste para verificar que alterações funcionam em tempo real
#i = 0
#j = 0
#states_tail1 = [1,2]
#states_tail2 = [3,4]
#curr_state1 = 1
#curr_state2 = 3
#def animar():
#    global i
#    global j
#    global curr_state1
#    global curr_state2
#    net.clear()
    
#    objects[1].set_angulo_rotacao(i)
#    objects[2].set_angulo_rotacao(j)
#    objects[3].set_angulo_rotacao(j)
    
    # Desenha todos os objetos
#    for o in objects:
#        net.draw_obj(o)
#
#    if i > 30:
#        curr_state1 = 2
#    if i < -30:
#        curr_state1 = 1
#
#    if curr_state1 == 1:
#        i += 3
#    if curr_state1 == 2:
#        i -= 3
#
#    if j > 10:
#        curr_state2 = 3
#    if j < -10:
#        curr_state2 = 4
#
#    if curr_state2 == 4:
#        j += 3
#    if curr_state2 == 3:
#        j -= 3
#    
#    root.after(20, animar)


#animar()

root.mainloop()

