from Persoana import Persoana


class Angajat(Persoana): 

    firma : str
    salariu : float
    functie : str

    def __init__(self, firma: str, salariu: float, functie: str, nume: str, prenume: str, varsta: int):
        super().__init__(nume, prenume, varsta)
        self.firma = firma
        self.salariu = salariu
        self.functie = functie

    def afisare_informatii(self):
        super().afisare_informatii()
        print(f"Firma angajatului este {self.firma}")
        print(f"Salariul angajatului este {self.salariu}")
        print(f"Functia angajatului este {self.functie}")