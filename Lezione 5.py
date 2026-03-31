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
    Es 1. Aprire il file in modalità 'append' e inserire, uno per riga,
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