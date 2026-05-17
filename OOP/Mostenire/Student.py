from Persoana import Persoana


class Student(Persoana): 

    facultate : str
    an_studiu : int
    specializare : str

    def __init__(self, facultate: str, an_studiu: int, specializare: str, nume: str, prenume: str, varsta: int):
        super().__init__(nume, prenume, varsta)
        self.facultate = facultate
        self.an_studiu = an_studiu
        self.specializare = specializare

    def afisare_informatii(self):
        super().afisare_informatii()
        print(f"Facultatea studentului este {self.facultate}")
        print(f"Anul de studiu al studentului este {self.an_studiu}")
        print(f"Specializarea studentului este {self.specializare}")