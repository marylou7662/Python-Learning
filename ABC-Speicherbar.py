from abc import ABC, abstractmethod

class Speicherbar(ABC):
    @abstractmethod
    def speichern(self):
        pass

class Datei(Speicherbar):
    def speichern(self):
        print("Datei wurde gespeichert.")

class Datenbank(Speicherbar):
    def speichern(self):
        print("Eintrag wurde in der Datenbank gespeichert.")

# Aufruf
d1 = Datei()
d2 = Datenbank()

d1.speichern()
d2.speichern()
