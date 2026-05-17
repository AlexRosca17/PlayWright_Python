from Persoana import Persoana


class Student(Persoana): 

    def __init__(self, facultate: str, an_studiu: int, specializare: str, nume: str, prenume: str, varsta: int):
        super().__init__(nume, prenume, varsta)
        self.__facultate = facultate
        self.__an_studiu = an_studiu
        self.__specializare = specializare

    @property
    def facultate(self):
        return self.__facultate
    @property
    def an_studiu(self):
        return self.__an_studiu
    @property
    def specializare(self):
        return self.__specializare
    
    @facultate.setter
    def facultate(self, valoare: str):
        self.__facultate = valoare
    @an_studiu.setter
    def an_studiu(self, valoare: int):
        self.__an_studiu = valoare
    @specializare.setter
    def specializare(self, valoare: str):
        self.__specializare = valoare

    def afisare_informatii(self):
        super().afisare_informatii()
        print(f"Facultatea studentului este {self.__facultate}")
        print(f"Anul de studiu al studentului este {self.__an_studiu}")
        print(f"Specializarea studentului este {self.__specializare}")
    
    def mananca(self):
        print("Studentul mananca la cantina")
    
    def marire_an_studiu(self, valoare: int):
        self.__an_studiu += valoare