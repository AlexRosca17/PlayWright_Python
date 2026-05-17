class Masina:

    marca : str
    model : str
    an_fabricatie : int
    pret : float
    capacitate_cilindrica : float

    def __init__(self, marca: str, model:str, an_fabricatie:int, pret:float, capacitate_cilindrica:float):
        self.marca = marca
        self.model = model
        self.an_fabricatie = an_fabricatie
        self.pret = pret
        self.capacitate_cilindrica = capacitate_cilindrica
    
    def afisare_informatii(self):
        print(f"Masina este marca {self.marca})")
        print(f"Modelul masinii este {self.model}")
        print(f"Masina a fost fabricata in anul {self.an_fabricatie}")
        print(f"Pretul masinii este {self.pret}")
        print(f"Capacitatea cilindrica a masinii este {self.capacitate_cilindrica}")

