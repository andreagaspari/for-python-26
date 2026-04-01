'''
    Apro un file in modalità lettura ('r'), 
    lo leggo e ne stampo il contenuto;
    alla fine chiudo il file
'''
file = open('file.txt', 'r')
contenuto = file.read()
print(contenuto)
file.close()

'''
    Apro un file in modalità scrittura ('w'),
    lo modifico e lo chiudo
'''
file = open('file.txt', 'w')
file.write('Ciao mondo!\n')
file.close()

'''
    Apro un file in modalità aggiunta ('a')
    lo modifico e lo chiudo
'''
file = open('file.txt', 'a')
file.write('Hello world!\n')
file.close()


'''
    Finché sono all'interno del comando "with open"
    il file rimane disponibile, viene chiuso automaticamente
    alla fine del blocco
'''
with open('file.txt', 'r') as file:
    contenuto = file.read()
    print(contenuto)


'''
    Esercizio 1. 
    Aprire il file in modalità 'append' e inserire, uno per riga,
    i numeri da 1 a 100
'''
with open('file.txt', 'a') as file:
    i = 1
    while (i <= 100):
        file.write(str(i) + "\n")
        i += 1

    for i in range(1, 101):
        file.write(f"{i}\n")


'''
    Leggere riga per riga
'''
with open('file.txt', 'r') as file:
    for riga in file:
        print("Riga: " + riga)

    righe = file.readlines()


'''
    Leggere per riga mi permette di manipolare e utilizzare i dati contenuti
    nel file. Ad esempio posso leggere una lista di voti e calcolarne la media
'''
with open('voti.txt', 'r') as file:
    voti = file.readlines()
    somma = 0
    for voto in voti: 
        somma += int(voto)
    media = somma / len(voti)

print(f"La media di voti è: {media}")

'''
    Possiamo aprire il file anche in modalità combinate
'''
file = open('file.txt', 'r+')  # Lettura + Sovrascrittura
file = open('file.txt', 'a+')  # Lettura + Aggiunta in fondo al file
file = open('file.txt', 'w+')  # Scrittura + Lettura (SOVRASCRIVE il file all'apertura)

import json

with open('persone.json', 'r') as file:
    rubrica = json.load(file)

# Parte 1: chiedi i dati della nuova persona
persona = {
    "nome": "",
    "cognome": "",
    "città": "",
    "data_di_nascita": "",
    "codice_fiscale": ""
}
for chiave, valore in persona.items():
    persona[chiave] = input("Inserisci " + chiave + ": ")

# Parte 2: aggiungi la persona alla rubrica
rubrica.append(persona)  # Aggiunge in fondo alla rubrica

with open('persone.json', 'w') as file:
    json.dump(rubrica, file, indent = 4)


'''
    Per gestire gli errori che possono verificarsi in Python possiamo
    usare il costrutto try / except
'''
try:
    numero = "Ciao"
    int(numero)
except ValueError:
    print("Il dato non può essere convertito")

print("Il programma prosegue")

'''
    Try/except può gestire più tipologie di errori con rami except multipli,
    a seconda del tipo di errore lanciato (il primo errore lanciato è quello
    che conta)
'''
lista_nomi = ["Alice", "Bob", "Charlie"]
try:
    indice = input("Inserisci la posizione del nome (0, 1 o 2): ")
    # 1. Può generare ValueError se non è un numero
    pos = int(indice) 
    
    # 2. Può generare IndexError se il numero è fuori intervallo
    print(f"Hai scelto: {lista_nomi[pos]}")
except ValueError:
    print("Non hai inserito un numero (ValueError).")
except IndexError:
    print("Hai inserito un numero fuori dall'intervallo valido (0, 1, 2). (IndexError)")
except Exception as e:
    # In questo ramo posso gestire TUTTI gli errori diversi da quelli gestiti.
    print("Errore imprevisto:", e)

'''
    Il ramo "finally" viene SEMPRE eseguito alla fine delle istruzioni critiche,
    sia se sono stati lanciati errori (viene eseguito dopo la except) 
    sia se è andato tutto bene.
'''
try:
    numero = "Ciao"
    int(numero)
except ValueError:
    print("Numero non valido")
finally:
    print("Il numero inserito è", numero)

'''
    Il ramo else contiene istruzioni che vengono eseguito SOLO se il codice 
    critico non ha lanciato eccezioni
'''
lista_nomi = ["Alice", "Bob", "Charlie"]
try:
    indice = input("Inserisci la posizione del nome (0, 1 o 2): ")
    # 1. Può generare ValueError se non è un numero
    pos = int(indice) 
    
    # 2. Può generare IndexError se il numero è fuori intervallo
    print(f"Hai scelto: {lista_nomi[pos]}")
except ValueError:
    print("Non hai inserito un numero (ValueError).")
except IndexError:
    print("Hai inserito un numero fuori dall'intervallo valido (0, 1, 2). (IndexError)")
except Exception as e:
    # In questo ramo posso gestire TUTTI gli errori diversi da quelli gestiti.
    print("Errore imprevisto:", e)
else:
    print("Ottimo, hai inserito un indice valido e non si sono verificati errori")


'''
    L'apertura del file in modalità lettura è un'operazione sempre critica,
    se il file non esiste, viene lanciato il FileNotFoundError.
'''
try:
    file = open('fileNonEsistente.txt', 'r')
    try:
        # Qui eseguo tutte le operazioni sui dati contenuti nel file
        dati = file.read()
    finally:
        file.close()

except FileNotFoundError:
    print("File non trovato")


try:
    file = open('fileNonEsistente.txt', 'r')
    
    # Qui eseguo tutte le operazioni sui dati contenuti nel file
    dati = file.read()
    
except FileNotFoundError:
    print("File non trovato")

finally:
    try:
        file.close()
    except NameError:
        print("Il file non esiste")

'''
    Esercizio 2: 
    Creare una semplice rubrica con le funzioni stampa e aggiungi
    persone (Nome,Cognome,Telefono).
'''
try:
    op = int(input("Cosa vuoi fare? 1: Stampa rubrica | 2: Aggiungi persona"))
    if (op == 1):
        # Stampo la rubrica
        with open("rubrica.csv", "r") as file:
            next(file) # Salta intestazione (nome,cognome,telefono)
            for riga in file:
                # Stampa semplice
                print(riga.strip())
                # Parse dei dati
                nome, cognome, telefono = riga.strip().split(",")
                print(f"Nome e Cognome: {nome} {cognome} | Tel: {telefono}")
    elif (op == 2):
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
