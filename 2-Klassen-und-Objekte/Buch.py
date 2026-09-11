class Buch: 

    def __init__(self, titel, autor, seiten): 
        self.titel = titel 
        self.autor = autor 
        self.seiten = seiten 
        self.abgeschlossen = False 

    def kaufen(self): 
        print(f"Du hast das Buch '{self.titel}' gekauft.") 

    def lesen(self): 
        print(f"Du liest gerade '{self.titel}' von {self.autor}.") 

    def abschliessen(self): 
        self.abgeschlossen = True 
        print(f"Du hast das Buch '{self.titel}' abgeschlossen!") 

    def info(self): 
        print(f"Titel: {self.titel}") 
        print(f"Autor: {self.autor}") 
        print(f"Seiten: {self.seiten}") 
        print(f"Abgeschlossen: {self.abgeschlossen}") 

        # add libery with title, author, pages, and completed status