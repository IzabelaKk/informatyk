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
            
            
        def dms(x,txt):
            """
            Funkcja przeliczająca wartość wyrażoną w radianach na wartość wyrażoną w stopniach, minutach i sekundach
            ----------
            x : FLOAT
                 wartość w radianach

            Returns
            -------
            lat
                [stopnie dziesiętne] - szerokość geodezyjna
            lon
                [stopnie dziesiętne] - długośc geodezyjna.
            h : TYPE
                [metry] - wysokość elipsoidalna
            output [STR] - optional, defoulf 
                dec_degree - decimal degree
                dms - degree, minutes, sec
            """
            sig = ' '
            if x < 0:
                sig = '-'
                x = abs(x)
            x = x * 180/pi
            d = int(x)
            m = int(60 * (x - d))
            s = (x - d - m/60)*3600
            print(txt,sig,'%3d' % d,'°', '%2d' % m,"'",'%7.5f' % s,'"')
            
            
        def XYZ2flh(self, X, Y, Z):
            p = np.sqrt(X**2 + Y**2)
            f = np.arctan(Z/(p*(1-self.e2)))
            dms(f)
            while True:
                N = Np(f, self.a, self.e2)
                h = (p/np.cos(f))-N
                fpop = f
                f = np.arctan(Z/(p*(1-self.e2*N/(N+h))))
                dms(f)
                if abs(fpop-f) < (0.000001/206265):
                    break
            l = np.arctan2(Y,X)
            return(f,l,h)