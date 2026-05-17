from Persoana import Persoana


class Angajat(Persoana): 

    def __init__(self, firma: str, salariu: float, functie: str, nume: str, prenume: str, varsta: int):
        super().__init__(nume, prenume, varsta)
        self.__firma = firma
        self.__salariu = salariu
        self.__functie = functie

    @property
    def firma(self):
        return self.__firma
    @property
    def salariu(self):
        return self.__salariu
    @property
    def functie(self):
        return self.__functie
    
    @firma.setter
    def firma(self, valoare: str):
        self.__firma = valoare
    @salariu.setter
    def salariu(self, valoare: float):
        self.__salariu = valoare
    @functie.setter
    def functie(self, valoare: str):
        self.__functie = valoare

    def afisare_informatii(self):
        super().afisare_informatii()
        print(f"Firma angajatului este {self.__firma}")
        print(f"Salariul angajatului este {self.__salariu}")
        print(f"Functia angajatului este {self.__functie}")
    
    def mananca(self):
        print("Angajatul mananca la cantina")