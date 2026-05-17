
a = 5
b = 10
nume = "Alex"
nume2 = 'Maria'

def afisare_numere():
    print(nume + " si " + nume2 + " " + "au " + str(a) + " mere")
    print(a + b)

afisare_numere()

def adunare_numere(x: int, y: int):
    print("Suma numerelor este: ", a + b)

adunare_numere(a, b)

def numele_participantilore(z: str):
    print(z)

numele_participantilore(nume)

def adunare_numere2(x: int, y: int) -> int:
    return x + y

rezultat = adunare_numere2(20, b)
print("Rezultatul adunarii este: ", rezultat)

def gender_check(x: str | None = None) -> str:
    if x == "Alex":
        return "Masculin"
    elif x == "Maria":
        return "Feminin"
    return "Necunoscut"

gender = gender_check("Maria")
gender = gender_check()
print("Gender:", gender)

def afisare_numere_multimi():
    numere = [1, 2, 3, 4, 5]
    numere.append(6)
    for numar in numere:
        print(numar)
        print()
    
    nume_si_numere: list[int | str | float] = [3, "alex", 5, "maria", 5.3]
    for element in nume_si_numere:
        print(element)

    nume_si_numere = nume_si_numere.__add__([7, "ana", 8.5])
    print(nume_si_numere)

afisare_numere_multimi()
    
