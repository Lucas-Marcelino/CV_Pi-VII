import numpy as np

class hsv:
    def __init__(self, hue_min, hue_max, sat_min, sat_max, val_min, val_max):
        self.hue_min = hue_min
        self.sat_min = sat_min
        self.val_min = val_min
        self.hue_max = hue_max
        self.sat_max = sat_max
        self.val_max = val_max
    
    def getMin(self):
        return np.array([self.hue_min, self.sat_min, self.val_min])
    
    def getMax(self):
        return np.array([self.hue_max, self.sat_max, self.val_max])

    def setHSV(self): #Ajustar para fazer algo com o backend
        print('Falta implementar')
