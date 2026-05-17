from Student import Student
from Angajat import Angajat


class Test:

    cristi = Angajat("Google", 5000, "Software Engineer", "Cristi", "Popescu", 30)
    cristi.afisare_informatii()
    print(cristi.firma)

    print()
    
    marcel = Student("ASE", 3, "Informatica Economica", "Marcel", "Ionescu", 22)
    marcel.afisare_informatii()