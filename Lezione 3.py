'''
i = 0
print(i) # Stampa 0
i += 1
print(i) # Stampa 1
i += 1 
print(i) # Stampa 2
i += 1 
# [...]
print(i) # Stampa 5
'''

'''
    Stampa i numeri da 0 a 5
    Inizializzo un contatore, all'interno del ciclo while
    lo stampo e lo incremento finché non assume un
    valore superiore a 5
'''
i = 0
while i <= 5:
    print(i)
    i += 1
print("Fine del ciclo")

'''
    Esercizio 1:
    Stampare i numeri della serie di Fibonacci inferiori a 100
    1 1 2 3 5 8...
'''
i = 0
j = 1
while j <= 100 :
    print(j, end=" ") # Stampa il numero seguito da spazio senza andare a capo
    '''
        Con la doppia assegnazione, le due istruzioni vengono
        eseguite contemporaneamente, usando i valori originali:
            al primo ciclo 
                i passa da 0 a 1,
                j somma i = 0 e j = 1 quindi rimane 1
            al secondo ciclo
                i rimane 1 (perché j = 1)
                j somma i = 1 e j = 1 quindi diventa 2
            al terzo ciclo 
                i passa da 1 a 2,
                j somma i = i e j = 2 quindi diventa 3
    '''
    i, j = j, i + j

print()

'''
    Esercizio 2:
    Stampare N numeri della serie di Fibonacci
    1 1 2 3 5 8...
'''
a = 0
b = 1
n = int(input("Quanti numeri della serie vuoi stampare? "))
i = 0
while i < n :
    print(b, end=" ")
    
    # Aggiorno i valori della serie
    temp = a        # Salvo valore iniziale di A
    a = b           # Sposto B dentro A
    b = temp + b    # Incremento B del valore iniziale di A

    # Incremento il contatore di numeri stampati
    i += 1

print()


voti = [6, 8, 7, 6, 7, 9, 7]

# Leggere il primo numero della lista
print("Il primo voto è", voti[0])

# Leggere il quarto numero della lista
print("Il quarto voto è", voti[3])

# Leggere l'ultimo elemento
print("L'ultimo voto è", voti[6])
print("L'ultimo voto è", voti[len(voti) - 1])
print("L'ultimo voto è", voti[-1])

'''
    Usando For ... in posso scorrere tutti gli elementi
    di una lista, usando una variabile che ad ogni
    iterazione assume il valore successivo della lista
'''
sommaVoti = 0
for voto in voti :
    sommaVoti += voto
# len(voti) mi dice quanti elementi sono presenti nella lista
mediaVoti = sommaVoti / len(voti)
print(mediaVoti)

# Tutti i numeri da 1 a 100
listaNumeri = range(1, 100, 1)    #[1, 2, 3, 4, ... , 99, 100]

'''
    Stampa tutti multipli di 5 compresi tra 1 e 100
'''
for numero in range(0, 100, 5) :
    print(numero, end=" ")
print()

'''
    Esercizio 3:
    Chiedere all'utente quanti animali vuole stampare
    e mostrarli (massimo 5)
'''
listaAnimali = ["gatto", "cane", "pesce", "cavallo", "coniglio"]
numeroAnimali = int(input("Quanti animali? (max 5)"))
for animale in listaAnimali[0:numeroAnimali]:
    print(animale)

'''
    I Dizionari permettono di assegnare un'etichetta (chiave)
    ai dati presenti nell'elenco (valori), e accedere ad essi
    usando la chiave stessa
'''
voti = [6, 7, 8, 9]
studente = {
    "nome": "Andrea",
    "cognome": "Gaspari",
    "matricola": "1234",
    "voti": voti
}
studente["cognome"]

studenti = [
    {
        "nome": "Luca",
        "cognome": "Rossi",
        "voti": [6, 7, 8, 9]
    },
    {
        "nome": "Mario",
        "cognome": "Bianchi",
        "voti": [6, 7, 5, 9, 7]
    },
    {
        "nome": "Lucia",
        "cognome": "Verdi",
        "voti": [4, 7, 8, 9]
    },
    {
        "nome": "Maria",
        "cognome": "Marroni",
        "voti": [8, 7, 8, 9]
    }
]

# Ciclo gli elementi nella lista studenti
for studente in studenti:
    # Calcolo la media dei voti dello studente
    sommaVoti = 0
    for voto in studente["voti"]:
        sommaVoti += voto
    mediaVoti = sommaVoti / len(studente["voti"]);
    # Stampo "Nome Cognome ha una media di Media"
    print(studente["nome"], studente['cognome'], 
        "ha una media di", mediaVoti);
    # In alternativa (con la f-string)
    # print(f"{studente["nome"]} {studente["cognome"]} ha una media di {mediaVoti}")
    
persona = {
    "città": "Rimini",
    "nome": "Mario",
    "data_di_nascita": "12/03/1998",
    "cognome": "Rossi",
    "codice_fiscale": "RSSMRA98C12H294N"
}
for chiave, valore in persona.items() :
    print(chiave + ": " + valore)

rubrica = [
    {
        "nome": "Mario",
        "cognome": "Rossi",
        "città": "Rimini",
        "data_di_nascita": "12/03/1998",
        "codice_fiscale": "RSSMRA98C12H294N"
    },
    {
        "nome": "Maria",
        "cognome": "Rossi",
        "città": "Rimini",
        "data_di_nascita": "21/06/1998",
        "codice_fiscale": "RSSMRA98F61H294N"
    }
]

persona = { "nome": '' }
persona["nome"] = "Luca" # La chiave esiste: sovrascrivo il valore
# { "nome": "Luca" }
persona["cognome"] = "Bianchi" # La chiave non esiste: la aggiungo
# { "nome": "Luca", "cognome": "bianchi" }

rubrica.append(persona) # Aggiungi un elemento ad una lista
rubrica.insert(2, persona) # Aggiungi un elemento alla posizione 2

'''
    Esercizio 4:
    Chiedi all'utente i dati di una persona,
    aggiungila alla rubrica,
    stampa tutte le persone nella rubrica
'''
rubrica = [
    {
        "nome": "Mario",
        "cognome": "Rossi",
        "città": "Rimini",
        "data_di_nascita": "12/03/1998",
        "codice_fiscale": "RSSMRA98C12H294N"
    },
    {
        "nome": "Maria",
        "cognome": "Rossi",
        "città": "Rimini",
        "data_di_nascita": "21/06/1998",
        "codice_fiscale": "RSSMRA98F61H294N"
    }
]
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

''' 
    In alternativa usiamo una lista di campi da chiedere
    e una persona vuota:

    persona = {}
    campi = ["nome", "cognome", "città", "data_di_nascita","codice_fiscale"]
    for campo in campi :
        persona[campo] = input("Inserisci " + campo)
'''

# Parte 2: aggiungi la persona alla rubrica
rubrica.append(persona)  # Aggiunge in fondo alla rubrica

'''
    Alternativa
    è possibile concatenare due liste tra loro:
    
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    lista3 = lista1 + lista2 # [1, 2, 3, 4, 5, 6]

    Usando l'operatore += possiamo quindi concatenare la persona
    alla rubrica
    lista1 += lista2 # Equivale a lista1 = lista1 + lista2
    
    Concatena una lista composta dalla sola persona 
    in fondo alla rubrica
    rubrica += [persona]
'''

# Parte 3: Stampa le persone della rubrica
for persona in rubrica:
    for etichetta, valore in persona.items():
        print(etichetta, valore, sep=": ")



'''
    Per tenere aperta una sessione, possiamo usare un flag
    e un ciclo while che racchiude il nostro programma.
'''
ricomincia = True
while ricomincia :
    esci = input("Vuoi uscire? (S/N)")
    if esci == "s" or esci == "S" :
        ricomincia = False
print("Sessione conclusa. Chiusura in corso...")


'''
    Esercizio 5
    Crea una calcolatrice in grado di fare somma o sottrazione
    di due numeri chiesti all'utente. Finché l'utente non vuole
    uscire, permettigli di fare nuovi calcoli.
'''
ricomincia = True
while ricomincia :
    # Chiedi numeri e operatore
    numero1 = int(input("Inserisci il primo numero: "))
    operatore = input("Inserisci l'operatore (+/-): ")
    numero2 = int(input("Inserisci il secondo numero: "))

    # Risultato
    '''
        if operatore == "+" :
            risultato = numero1 + numero2
        elif operatore == "-":
            risultato = numero1 - numero2
        else:
            print("Operatore non valido.")
    '''
    match operatore :
        case "+":
            risultato = numero1 + numero2
        case "-":
            risultato = numero1 - numero2
        case "/":
            risultato = numero1 / numero2
        case "*":
            risultato = numero1 * numero2
        case _:
            print("Operatore non valido")

    if risultato :
        print("Risultato: ", risultato)

    continua = input("Vuoi fare un altro calcolo? (S/N)")
    if continua.lower() != "s" :
        ricomincia = False