'''
    Esempio: Creare una semplice rubrica con le funzioni stampa e aggiungi
    persone (Nome,Cognome,Telefono).
'''
try:
    op = int(input("Cosa vuoi fare? 1: Stampa rubrica | 2: Aggiungi persona"))
    if (op == 1):
        # Stampo la rubrica
        with open("rubrica.csv", "r") as file:
            next(file) # Salta intestazione (nome,cognome,telefono)
            for riga in file:
                # Stampa semplice (nome,cognome,telefono)
                # print(riga.strip())
                
                # Stampa dei dati
                nome, cognome, telefono = riga.strip().split(",")
                print(f"Nome e Cognome: {nome} {cognome} | Tel: {telefono}")
    elif (op == 2):
        # Se il file non esiste lo creo e aggiungo l'intestazione
        try:
            file = open("rubrica.csv", "r")
        except FileNotFoundError:
            with open("rubrica.csv", "w") as file:
                file.write("nome,cognome,telefono\n")

        # Aggiungo una persona alla rubrica
        nome = input("Inserisci il nome: ")
        cognome = input("Inserisci il cognome: ")
        telefono = input("Inserisci il numero di telefono: ")

        with open("rubrica.csv", "a") as file:
            file.write(f"{nome},{cognome},{telefono}\n")
    else:
        # Se l'utente ha inserito un numero, ma non è ne 1 ne 2 lancio ValueError
        raise ValueError

except ValueError:
    print("Scelta non valida. Scegli tra 1 e 2.")
except FileNotFoundError:
    print("La rubrica non esiste ancora. Aggiungi una persona per crearla!")