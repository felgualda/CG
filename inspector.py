from tkinter import *
import sys

class Inspector(Frame):
    def __init__(self, master=None, objects=["Teste1","Teste2"],net=None):
        super().__init__(master) 

        self.objects = objects
        self.net = net

        self.control_frame = Frame(self)
        self.control_frame.pack(side="top", fill="x", padx=5, pady=5)

        self.option_var = StringVar(self)
        self.option_menu = OptionMenu(self.control_frame, self.option_var,*self.objects.keys(), command=self.option_changed).pack(side="top")
        self.option_var.set("Selecione um objeto")

        self.control_position_frame = Frame(self.control_frame)
        self.control_position_frame.pack(side="top", fill="x", padx=5, pady=5)

        self.entries = {}
        self.vars = {}

        self.lock_entry_update = False

        Label(self.control_position_frame, text="Posição",font=("Arial", 10, "bold")).pack(side="top")

        self.var_x = StringVar(self)
        self.var_y = StringVar(self)
    
        self._create_entry_field(self.control_position_frame,"Pos X","x: ")
        self._create_entry_field(self.control_position_frame,"Pos Y","y: ")
        self._create_entry_field(self.control_position_frame,"Pos Z","z: ")

        # rotacao

        self.control_rotation_frame = Frame(self.control_frame)
        self.control_rotation_frame.pack(side="top", fill="x", padx=5, pady=5)

        Label(self.control_rotation_frame, text="Rotação",font=("Arial", 10, "bold")).pack(side="top")

        self._create_entry_field(self.control_rotation_frame,"Rot X","r: ")

        # escala

        self.control_scale_frame = Frame(self.control_frame)
        self.control_scale_frame.pack(side="top", fill="x", padx=5, pady=5)

        Label(self.control_scale_frame, text="Escala",font=("Arial", 10, "bold")).pack(side="top")

        self._create_entry_field(self.control_scale_frame,"Scl X","x: ")
        self._create_entry_field(self.control_scale_frame,"Scl Y","y: ")
        self._create_entry_field(self.control_scale_frame,"Scl Z","z: ")

        self.option_changed(None)


    def option_changed(self, selection):
            #nenhum objeto selecionado
            if selection == None:
                for entry in self.entries.values():
                    entry.config(state="disabled")
                return
            
            self.lock_entry_update = True

            obj = self.objects.get(selection)
            if obj:
                for key in self.entries.keys():
                    self.entries.get(key).config(state="normal")
                    self.entries.get(key).delete(0, END)
                    self.entries.get(key).insert(0, str(obj.get_param(key)))

            self.lock_entry_update = False
                

    def atualizar_objeto(self, *args):
        if self.lock_entry_update: return

        nome_obj = self.option_var.get()
        obj = self.objects.get(nome_obj)
        
        if obj:
            try:
                new_x = float(self.vars.get("Pos X").get()) if self.vars.get("Pos X").get() else 0
                new_y = float(self.vars.get("Pos Y").get()) if self.vars.get("Pos Y").get() else 0
                new_theta = float(self.vars.get("Rot X").get()) if self.vars.get("Rot X").get() else 0
                new_scale_x = float(self.vars.get("Scl X").get()) if self.vars.get("Scl X").get() else 1
                new_scale_y = float(self.vars.get("Scl Y").get()) if self.vars.get("Scl Y").get() else 1
                
                obj.set_offset([new_x, new_y]) 
                obj.set_angulo_rotacao(new_theta)
                obj.set_escala([new_scale_x, new_scale_y]) 
                obj.transform()
                self.net.clear()

                for _,obj in self.objects.items():
                    self.net.draw_obj(obj)
                
            except ValueError:
                pass

    def _create_entry_field(self, parent, entry_name,label):
        var = StringVar(self)
        var.trace_add("write", self.atualizar_objeto)

        Label(parent, text=label).pack(side="left")
        entry = Entry(parent, width=5, textvariable=var)
        entry.pack(side="left", padx=5)

        self.entries[entry_name] = entry
        self.vars[entry_name] = var


        return entry,var