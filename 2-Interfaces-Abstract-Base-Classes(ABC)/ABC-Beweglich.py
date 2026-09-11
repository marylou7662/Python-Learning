from abc import ABC, abstractmethod 

class Beweglich(ABC):
    @abstractmethod 
    def bewegen(self): 
        pass 

    @abstractmethod 
    def stoppen(self): 
        pass 

class Auto(Beweglich): 
    def bewegen(self): 
        print("Auto fährt los.") 
    def stoppen(self): 
        print("Auto hält an.") 

class Fahrrad(Beweglich): 
    def bewegen(self): 
        print("Fahrrad fährt los.") 
    def stoppen(self): 
        print("Fahrrad hält an.") 

class Bahn(Beweglich):
    def bewegen(self): 
        print("Bahn fährt los.") 
    def stoppen(self): 
        print("Bahn hält an.") 

# Liste aller Objekte 
fahrzeuge = [Auto(), Fahrrad(), Bahn()] 

for f in fahrzeuge: 
    f.bewegen() 
    f.stoppen() 