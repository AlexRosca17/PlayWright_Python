from Persoana import Persoana
from Student import Student
from Angajat import Angajat


cristi = Angajat("Google", 5000, "Software Engineer", "Cristi", "Popescu", 30)
cristi.afisare_informatii()
print(cristi.firma)

print()
    
marcel = Student("ASE", 3, "Informatica Economica", "Marcel", "Ionescu", 22)
marcel.afisare_informatii()

marcel.mananca()
cristi.mananca()

print()

def mancare():
        persoane: list[Persoana | Student | Angajat]= [
        Persoana("Ion", "Popescu", 40),
        Student("ASE", 3, "Informatica Economica", "Marcel", "Ionescu", 22),
        Angajat("Google", 5000, "Software Engineer", "Cristi", "Popescu", 30)
        ]   

        for persoana in persoane:
            persoana.mananca()
    
mancare()