from Studente import Studente
from Indirizzo import Indirizzo
from Classe import Classe

classe = Classe(1, "A")

print("Benvenuto nel registro della 1A")

while True:
    print("Menu")
    print("1: Aggiungi Studente")
    print("2: Stampa lista studenti")
    print("3: Salva il registro")
    print("X: Esci")
    scelta = input("Cosa vuoi fare? ")
    match scelta:
        case "1":
            studente = Studente(
                input("Nome: "),
                input("Cognome: "),
                input("Data di nascita: "),
                input("Codice fiscale: "),
                input("Telefono: "),
                input("Email: "),
                Indirizzo(
                    input("Via: "),
                    input("Numero: "),
                    input("CAP: "),
                    input("Città: "),
                    input("Provincia: "),
                    input("Stato: ")
                ),
                input("Matricola: ")
            )
            classe.aggiungi_studente(studente)
        case "2":
            print(classe)
            classe.stampa_lista_studenti()
        case "3":
            classe.salva()
        case "X" | "x":
            salva = input("Vuoi salvare il registro prima di uscire (s/n)?")
            if (salva.lower() == 's'):
                classe.salva()
            break
        case _:
            print("Scelta non valida")

print("Grazie per aver usato il Registro")