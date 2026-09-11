from abc import ABC, abstractmethod
import math 

class Form(ABC): 
    @abstractmethod 
    def flaeche(self): 
        pass 

class Kreis(Form): 
    def __init__(self, radius): 
        self.radius = radius 

    def flaeche(self): 
        return math.pi * self.radius**2 

class Rechteck(Form): 
    def __init__(self, breite, hoehe): 
        self.breite = breite 
        self.hoehe = hoehe 

    def flaeche(self): 
        return self.breite * self.hoehe 

# Objekte 
k = Kreis(5) 
r = Rechteck(4, 6) 

print("Fläche Kreis:", k.flaeche()) 
print("Fläche Rechteck:", r.flaeche()) 