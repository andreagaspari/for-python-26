'''
Operatori Logici:
    - AND: Entrambe le condizioni devono essere vere
    - OR: Almeno una delle condizioni deve essere vere
    - NOT: La condizione deve essere falsa
'''
eta = input("Inserisci l'età: ")
eta = int(eta)
if eta > 0 and eta < 18 :
    print("Utente ammesso")
    # qui potrei aggiungere altre istruzioni 
else :
    print("Utente non ammesso")
    # altre istruzioni se una delle cond. è falsa


''' 
    Conversione di dati
        input() ritorna sempre una stringa, se dobbiamo
        manipolare il dato, dobbiamo poterlo convertire in 
        formato numerico:
            int(valore) -> Converte in numero intero
            float(valore) -> Converte in numero decimale
            str(valore) -> Converte in stringa
'''
eta = input ("Inserisci l'età: ")
eta = int(eta) # Il valore viene convertito in formato intero
eta = float(eta) # Il valore viene convertito in formato decimale

'''
    Se non convertiamo il valore, non possiamo fare controlli 
    numerici. Nell'esempio che segue faccio il confronto tra
    due stringhe, per cui viene valutato l'ordine ALFABETICO 
    delle due stringhe quindi:
        "19" < "18"  ---> Falso
        "019" < "18" ---> Vero
'''
eta = input("inserisci l'età:")
if (eta < "18") :
    print ("utente minorenne")
else :
    print ("utente maggiorenne")

'''
    Per controllare un valore numerico, convertiamolo prima:
'''
eta = input("inserisci l'età:")
eta = int(eta)
if (eta < 18) :
    print ("utente minorenne")
else :
    print ("utente maggiorenne")

'''
    Per leggere un booleano, meglio chiedere un carattere
    e valutarlo con if/elif/else
'''
maggiorenne = input ("Sei maggiorenne? (S/N)")
if maggiorenne == 'S' :
    maggiorenne = True
elif maggiorenne == 'N' :
    maggiorenne = False
else :
    maggiorenne = "Errore"
print(maggiorenne)

'''
    L'uso di ELIF corrisponde a due IF annidati, 
    il codice seguente è uguale a quello appena visto:
'''
maggiorenne = input ("Sei maggiorenne? (S/N)")
if maggiorenne == 'S' :
    maggiorenne = True
else :
    if maggiorenne == 'N' :
        maggiorenne = False
    else :
        maggiorenne = "Errore"
print(maggiorenne)

'''
    Esercizio 1:
    Chiedere all'utente un numero intero, moltiplicalo per 4
    e stampa un messaggio che indica se il risultato 
    è maggiore o minore di 100.
'''
numero = input("Inserisci un numero intero: ")
numero = int(numero)
moltiplicazione = numero * 4

if moltiplicazione > 100 :
    output = f"{moltiplicazione} è maggiore di 100"
elif moltiplicazione < 100 :
    output = f"{moltiplicazione} è minore di 100"
else :
    output = f"{moltiplicazione} è uguale a 100"

print(output)

'''
    Le stringhe possono essere sommate (concatenazione)
    o moltiplicate (ripetizione)
'''
stringa1 = 'Questa è una stringa. '
stringa2 = 'Altra stringa.'
print(stringa1 + stringa2) # Stampa: 'Questa è una stringa. Altra stringa'
print(stringa1 * 3) # Stampa: 'Questa è una stringa. Questa è una stringa. Questa è una stringa. '

'''
    Per misurare la lunghezza di una stringa possiamo
    usare la funzione len(stringa).
'''
password = input("Inserisci una password (almeno 8 caratteri): ")
if len(password) < 8 :
    print("La password è troppo breve")
else:
    print("Password ok")

'''
    Possiamo verificare il tipo di dato usando la funzione 
    type().
'''
eta = 25
nome = "Andrea"
altezza = 1.70
is_maggiorenne = True

print(type(eta))
print(type(nome))
print(type(altezza))
print(type(is_maggiorenne))

'''
    Esercizio 2:
    Calcola l'area di un rettangolo dati base e altezza
'''
base = int(input("Inserisci la base: "))
altezza = int(input("Inserisci l'altezza: "))
area = base * altezza
print("L'area del rettangolo è", area)

'''
    Esercizio 3:
    Calcola l'area di un triangolo dati base e altezza
'''
base = int(input("Inserisci la base: "))
altezza = int(input("Inserisci l'altezza: "))
print(f"L'area del triangolo è {base * altezza / 2}")

'''
    Esercizio 4:
    Dati base e altezza, calcola l'area della figura scelta
    dall'utente: Rettangolo, Triangolo o Parallelogramma
'''
base = int(input("Inserisci la base: "))
altezza = int(input("Inserisci l'altezza: "))

print("Di quale forma vuoi calcolare l'area?")
print("1: Triangolo")
print("2: Rettangolo")
print("3: Parallelogramma")
forma = input("Inserisci il numero corrispondente: ")

# Inizializzo la variabile area fuori dall'if, per evitare di usare una variabile indefinita
area = False
if forma == "1" :
    area = base * altezza / 2
elif forma == "2" or forma == "3":
    area = base * altezza
else :
    print("Forma non valida")

# Se area ha assunto un valore diverso da False, la stampo
if area :
    print("L'area è", area)

''' 
    Esercizio 5:
    Chiedere l'importo totale, se maggiore di 100 applicare
    uno sconto del 10%, altrimenti indicare che non si ha
    diritto allo sconto. In entrambi i casi mostrare l'importo
    finale.
'''
spesa = float(input("Inserisci l'importo: "))

if spesa > 100:
    importo_finale = spesa - (spesa / 10)
else:
    print("Non hai diritto allo sconto.")
    importo_finale = spesa
    
print("L'importo finale è", importo_finale)

'''
	Esercizio 6:
    Dato nome utente e password noti (esempio "admin" e 
    "P4$$w0rd"), chiedere all'utente di loggarsi e
    mostrare il messaggio di errore corretto:
	    - Nome utente errato
	    - Password troppo corta
	    - Password errata
	Oppure indicare che è stato effettuato il Login.
'''
nome_utente = "admin"
password = "P4$$w0rd"

input_nome_utente = input("Inserisci il nome utente")
input_password = input("Inserisci la password")

if input_nome_utente != nome_utente :
    print("Nome utente errato")
elif len(input_password) < 8 :
    print("Password troppo corta")
elif input_password != password :
    print("Password errata")
else :
    print("Login effettuato")

