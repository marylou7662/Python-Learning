from abc import ABC, abstractmethod 
import math 

class Speicherbar(ABC): 
    @abstractmethod 
    def speichern(self): 
        pass 

class Form(ABC): 
    @abstractmethod 
    def flaeche(self): 
        pass 

class Kreis(Form, Speicherbar): 
    def __init__(self, radius): 
        self.radius = radius 

    def flaeche(self): 
        return math.pi * self.radius**2

    def speichern(self): 
        print(f"Kreis mit Radius {self.radius} wurde gespeichert.") 
    
# Objekt 
k = Kreis(3) 

print("Fläche:", k.flaeche()) 
k.speichern() 