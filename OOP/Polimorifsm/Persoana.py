class Persoana:

    def __init__(self, nume: str, prenume: str, varsta: int):
        self.__nume = nume
        self.__prenume = prenume
        self.__varsta = varsta

    @property
    def nume(self):
        return self.__nume

    @nume.setter
    def nume(self, valoare: str):
        self.__nume = valoare

    @property
    def prenume(self):
        return self.__prenume

    @prenume.setter
    def prenume(self, valoare: str):
        self.__prenume = valoare

    @property
    def varsta(self):
        return self.__varsta

    @varsta.setter
    def varsta(self, valoare: int):
        self.__varsta = valoare

    def afisare_informatii(self):
        print(f"Numele persoanei este {self.__nume}")
        print(f"Prenumele persoanei este {self.__prenume}")
        print(f"Varsta persoanei este {self.__varsta}")

    def mananca(self):
        print("Persoana mananca la cantina")
