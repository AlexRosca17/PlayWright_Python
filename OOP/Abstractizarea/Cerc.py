from OOP.Abstractizarea.FormaGeometrica import FormaGeometrica

class Cerc(FormaGeometrica):

    def __init__(self, raza: float):
        self.__raza = raza

    def calculeaza_aria(self) -> float:
        return 3.14 * self.__raza ** 2

    def calculeaza_perimetrul(self) -> float:
        return 2 * 3.14 * self.__raza
