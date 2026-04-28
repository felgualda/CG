from src.EDs.ponto import Ponto
import numpy as np
import math
import src.util as util
class Objeto():
    def __init__(self,nome,pontos = [],offset=[0,0],escala=[1,1],angulo=0,origem=Ponto([0,0,1]),pai=None,cor=""):
        self.nome = nome
        self.pontos_locais = pontos
        self.offset = offset
        self.escala = escala
        self.angulo = angulo
        self.pai = pai
        self.cor = cor
        self.origem = origem

        self.pontos_logicos = []

    def transform(self):

        m = self.offset[0]
        n = self.offset[1]

        # matriz de translação em coordenadas homogêneas vista em aula
        transl = np.array([
            [1,0,m],
            [0,1,n],
            [0,0,1]
        ])

        tht = np.radians(self.get_reference_rot()) 

        # matriz de rotação em coordenadas homogêneas vista em aula
        rot = np.array([
            [math.cos(tht),-math.sin(tht),0],
            [math.sin(tht),math.cos(tht),0],
            [0,0,1]
        ])

        k = self.get_reference_scl()

        # matriz de escala em coordenadas homogêneas vista em aula
        escl = np.array([
            [k[0],0,0],
            [0,k[1],0],
            [0,0,1]
        ])

        # matriz de translação para a origem do objeto
        ox = self.origem.get_global_pos()[0]
        oy = self.origem.get_global_pos()[1]

        origem = np.array([
            [1,0,ox + self.get_reference_pos()[0]],
            [0,1,oy + self.get_reference_pos()[1]],
            [0,0,1]
        ])
        origem_compl = np.array([
            [1,0,-ox - self.get_reference_pos()[0]],
            [0,1,-oy - self.get_reference_pos()[1]],
            [0,0,1]
        ])

        for pt in self.pontos_locais:
            p = pt.get_local_pos()
            
            # coordenadas do ponto
            a = np.array([
                [p[0]],
                [p[1]],
                [1]
            ])

            r =  origem @ rot @ escl @ origem_compl @ transl @ origem @ a
            nova_pos = [r[0,0],r[1,0],1]

            pt.set_pos(nova_pos)

        for pt in self.pontos_logicos:
            p = pt.get_local_pos()
            
            # coordenadas do ponto
            a = np.array([
                [p[0]],
                [p[1]],
                [1]
            ])

            r =  origem @ rot @ escl @ origem_compl @ transl @ origem @ a
            nova_pos = [r[0,0],r[1,0],1]

            pt.set_pos(nova_pos)
    
    def get_pontos(self):
        return self.pontos_locais
    
    def display_pontos_globais(self):
        print(f"{self.nome}:")

        i = 0
        for p in self.pontos_locais:
            print(f"v{i} = ( {p.get_global_pos()[0]+12.5} , {p.get_global_pos()[1]+2.5} , 0 )")
            i += 1

    def set_offset(self,novo_offset):
        self.offset = novo_offset

    def get_offset(self):
        return self.offset 

    def set_escala(self,nova_escala):
        self.escala = nova_escala

    def get_escala(self):
        return self.escala

    def set_angulo_rotacao(self,novo_angulo):
        self.angulo = novo_angulo

    def get_angulo_rotacao(self):
        return self.angulo
    
    def set_cor(self, cor):
        self.cor = cor
        
    def get_cor(self):
        return self.cor

    def add_ponto_logico(self,ponto):
        self.pontos_logicos.append(ponto)

    def add_ponto_local(self,ponto):
        self.pontos_locais.append(ponto)

    def set_origem(self,origem):
        self.origem = origem

    def get_origem(self):
        return self.origem
    
    def set_pai(self,pai):
        self.pai = pai

    def get_reference_pos(self):
        return self.pai.get_reference_pos() if self.pai else self.get_origem().get_global_pos()
    
    def get_reference_rot(self):
        return self.pai.get_reference_rot() + self.get_angulo_rotacao() if self.pai else self.get_angulo_rotacao()
    
    def get_reference_scl(self):
        return util.mult_vetor(self.pai.get_reference_scl(),self.get_escala()) if self.pai else self.get_escala()
    
    def get_param(self,param):
        if param == "Pos X": return self.get_offset()[0]
        if param == "Pos Y": return self.get_offset()[1]
        if param == "Pos Z": return 1
        if param == "Rot X": return self.get_angulo_rotacao()
        if param == "Scl X": return self.get_escala()[0]
        if param == "Scl Y": return self.get_escala()[1]
        if param == "Scl Z": return 1
        if param == "Cor": return self.get_cor()

        print(f"ERRO: Parâmetro {param} não encontrado na função objeto.get_param()")
        return 404