class Persoana: 

    nume : str
    prenume : str
    varsta : int

    def __init__(self, nume: str, prenume: str, varsta: int):
        self.nume = nume
        self.prenume = prenume
        self.varsta = varsta
    
    def afisare_informatii(self):
        print(f"Numele persoanei este {self.nume}")
        print(f"Prenumele persoanei este {self.prenume}")
        print(f"Varsta persoanei este {self.varsta}")