class Ponto():
    def __init__(self,pos,cor="black"):
        self.local_pos = pos
        self.global_pos = self.local_pos

        self.pos = pos
        self.cor = cor

    def get_local_pos(self):
        return self.local_pos

    def get_global_pos(self):
        return self.global_pos
    
    def set_pos(self,pos):
        self.global_pos = pos


    