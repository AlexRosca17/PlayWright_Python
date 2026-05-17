from abc import ABC, abstractmethod


class FormaGeometrica(ABC):

    @abstractmethod
    def calculeaza_aria(self) -> float:
        pass

    @abstractmethod
    def calculeaza_perimetrul(self) -> float:
        pass
