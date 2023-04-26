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
            
            
    def dms(self, txt, x):
        """
        Funkcja przeliczająca wartość wyrażoną w radianach na wartość wyrażoną w stopniach, minutach i sekundach
        ----------
        x : FLOAT
        wartość w radianach
        
        Zwraca:
        -------
        dms - stopnie, minuty, sekundy
        """
 
        sig = ' '
        if x < 0:
            sig = '-'
            x = abs(x)
        x = x * 180/pi
        d = int(x)
        m = int(60 * (x - d))
        s = (x - d - m/60)*3600
        return f"{txt} {sig} {d:3d}° {m:2d}' {s:7.5f}\""
        
        
        
    def Np(self):
        """
        Funkcja okreslająca przekrój poprzeczny w I wertykale
        -------
        a - duża półoś elispoidy
        f - spłaszczenie
        e2 - mimośród podniesiony do kwadratu
        
        Zwraca:
        -------
        Wartosć przekroju poprzecznego w I wetykale

        """
        N = self.a / np.sqrt(1 - self.e2 * np.sin(self.f)**2)
        return(N)
    
    
    def Mp(self):
        """
        Funkcja wyznaczająca promień przekroju normalnego w kierunku głównym
        -------
        a - duża półoś elispoidy
        f - spłaszczenie
        e2 - mimośród podniesiony do kwadratu
        
        Zwraca:
        -------
        Wartosć promienia przekroju normalnego w kierunku głównym

        """
        M = self.a * (1 - self.e2) / np.sqrt((1 - self.e2 * np.sin(f)**2)**3)
        return(M)
            
            
    def XYZ2flh(self, X, Y, Z):
        """
        Algorytm Hirvonena - algorytm transformacji współrzędnych ortokartezjańskich (x, y, z)
        na współrzędne geodezyjne długość szerokość i wysokośc elipsoidalna (phi, lam, h). Jest to proces iteracyjny. 
        W wyniku 3-4-krotneej iteracji wyznaczenia wsp. phi można przeliczyć współrzędne z dokładnoscią ok 1 cm.     
        Parametry:
        ----------
        X, Y, Z : FLOAT
             współrzędne w układzie orto-kartezjańskim, 

        Zwraca:
        -------
        phi - szerokość geodezyjna w stopniach dziesiętnych
        lam - długośc geodezyjna w stopniach dziesiętnych
        h - wysokość elipsoidalna w metrach
        """
        p = np.sqrt(X**2 + Y**2)
        f = np.arctan(Z/(p*(1-self.e2)))
        self.dms('f', f)
        while True:
            N = self.Np()
            h = (p/np.cos(f))-N
            fpop = f
            fl = np.arctan(Z/(p*(1-self.e2*N/(N+h))))
            self.dms('f', f)
            if abs(fpop-f) < (0.000001/206265):
                break
        l = np.arctan2(Y,X)
        return(degrees(f), degrees(l), h)
    
    def flh2XYZ(self, f, l, h):
        """
        Funkcja przeliczająca współrzędne geodezyjne (phi, lam h) na współrzędne ortokartezjańskie (X, Y, Z)

        Parametry:
        ----------
        f : FLOAT
            szerokosć geodezyjna wyrażona w radianach ?????????????????
        l : FLOAT
            długosć geodezyjna wyrażona w radianach
        h : FLOAT
            wysokosć elipsoidalna wyrażona w metrach

        Returns
        -------
        X - [metry]
        Y - [metry]
        Z - [metry]

        """
        N = self.Np()
        X = (N + h) * cos(f) * cos(l)
        Y = (N + h) * cos(f) * sin(l)
        Z = (N * (1 - self.e2) + h) * sin(f)
        return(X,Y,Z)
    
    
    
if __name__ == "__main__":
    geo = transformacje(model = "wgs84")
    X = 3664940.500; Y = 1409153.590; Z = 5009571.170
    phi, lam, h = geo.XYZ2flh(X, Y, Z)
    print(phi, lam, h)  #h do poprawy

#if __name__ == "__main__":
 #   orto = transformacje(model = "wgs84")
    