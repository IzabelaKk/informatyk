from math import *
import numpy as np

class transformacje():
    
    def __init__(self, model: str):
        """
        
        Parametry elipsolidy:
        ----------
        a - duża półoś elispoidy
        b - mała półoś elipsoidy
        f - spłaszczenie
        e - mimośród
        e2 - mimośród podniesiony do kwadratu

        """
        if model == "grs80":
            if model == "wgs84":
                self.a = 6378137
                self.b = 6356752.31424518 
            elif model == "grs80":
                self.a = 6378137
                self.b = 6356752.31414036
            elif model == "krasowski":
                self.a = 6378245
                self.b = 6356863.019  #jakby był potrzebny mimosrod i f http://uriasz.am.szczecin.pl/naw_bezp/elipsoida.html
            else:
                raise NotImplementedError(f"{model} nie został zaimplementowany")
            self.f = (self.a - self.b) / self.a
            self.e = sqrt(2 * self.f - self.f ** 2) 
            self.e2 = (2 * self.f - self.f ** 2) 