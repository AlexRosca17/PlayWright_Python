from Student import Student
from Angajat import Angajat


class Test:

    Cristi = Angajat("Google", 5000, "Software Engineer", "Cristi", "Popescu", 30)
    Cristi.afisare_informatii()

    print()
    
    Marcel = Student("ASE", 3, "Informatica Economica", "Marcel", "Ionescu", 22)
    Marcel.afisare_informatii()