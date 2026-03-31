from rubrica import *

ricomincia = True
rubrica = Rubrica()

while ricomincia :
    print("Operazioni:")
    print("1. Stampa rubrica")
    print("2. Aggiungi contatto")
    op = input("Cosa vuoi fare? ")
    match op:
        case "1":
            rubrica.stampaContatti()
        case "2":
            nome = input("Nome: ")
            cognome = input("Cognome: ")
            telefono = input("Telefono: ")
            contatto = Contatto(f"{nome},{cognome},{telefono}")
            rubrica.aggiungiContatto(contatto)
        case _:
            print("Scelta non valida")
            

    continua = input("Vuoi fare altro? (S/N)")
    if continua.lower() != "s" :
        ricomincia = False

rubrica.salva()