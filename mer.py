import random
class Mer:
    def __init__(self):
        self.profondeur=random.randint(1,20)
        self.type="Mer"
    def getProfondeur(self):
        return self.profondeur
    def setPronfondeur(self,new):
        if new > 0 and new < 20:
            self.profondeur=new