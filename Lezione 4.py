'''
    Definisco una funzione che stampa a video la scritta "Hello World"
    ogni volta che viene chiamata.
'''
def saluta():
    print("Hello World")


'''
    Definizione di una funzione che prende in ingresso un numero e ne stampa
    il quadrato.
'''
def printSquare(numero):
    risultato = numero * numero
    print(risultato)
'''
Esempio di utilizzo:
    printSquare(8)
'''

'''
    Definizione di una funzione che prende in ingresso un numero e ritorna il
    suo quadrato
'''
def square(numero):
    risultato = numero * numero
    return risultato
'''
Esempio di utilizzo:
    quadrato = square(8)
    print(quadrato)
'''

'''
    Esercizio 1
    Definire una funzione che prende in ingresso due numeri e ne 
    restituisce la somma.
'''
def somma(a, b):
    return a + b

'''
Esempio di utilizzo
    risultato = somma(1, 2)
    print(risultato)
'''

'''
    Le variabili globali possono essere usate all'interno di tutto il programma,
    all'interno delle funzioni il parametro locale non è collegato 
    alla variabile globale!

    Quindi ogni modifica al parametro locale NON si riflette sulla variabile globale
'''
x = 10 # Variabile Globale -> Visibile in tutto il programma
def moltiplicaPerY(x) :
    y = 2 # Variabile Locale -> Visibile solo all'interno della funzione
    x = 5 # Variabile Locale -> Il parametro X assume valore 5 SOLO dentro la funzione
    risultato = x * y
    return risultato
'''
Esempio di utilizzo
    z = moltiplicaPerY(x)
    print(x) # X vale ancora 10, perché è stato modificato solo all'interno della funzione
'''

'''
    Definita una variabile globale 'numGlobale', se la usiamo dentro la funzione
    la possiamo leggere.
'''
numGlobale = 10
def stampaVariabileGlobale():
    print(numGlobale) # 10 | Qui posso usare la varibile in quanto GLOBALE

def nonModificaVariabileGlobale():
    numGlobale = 20   # Questa dichiarazione imposta la variabile LOCALE omonima a quella globale
    print(numGlobale) # 20 | Qui sto stampando la variabile LOCALE (scollegata dal quella globale)

def modificaVariabileGlobale():
    global numGlobale # Qui indico alla funzione che userò la variabile GLOBALE
    numGlobale = 20   # Questa è una modifica della variabile GLOBALE
    print(numGlobale) # 20 | Qui sto stampando la variabile GLOBALE -> 20

'''
Esempio di utilizzo
    stampaVariabileGlobale() # numGlobale vale 10 -> Stampo 10
    nonModificaVariabileGlobale() # numGlobale all'interno della funzione vale 20 -> Stampo 20
    stampaVariabileGlobale() # numGlobale è ancora 10 -> Stampo 10
    modificaVariabileGlobale() # numGlobale viene davvero modificata -> Stampo 20
    stampaVariabileGlobale() # numGlobale è diventata 20 -> Stampo 20
'''

'''
    Per evitare confusione, quando una funzione deve modificare un parametro,
    è bene che ritorni il valore modificato, così da poterlo salvare all'esterno
    della funzione nella variabile che riteniamo opportuna
'''
variabileGlobale = 10
def modificaValore(valoreDaModificare):
    valoreDaModificare = valoreDaModificare + 10
    return valoreDaModificare

variabileGlobaleModificata = modificaValore(variabileGlobale)

'''
    Esercizio 2:
    Creare una funzione che stampa la sequenza di numeri di Fibonacci finché 
    il numero non è superiore al parametro passato.
    1, 1, 2, 3, 5, 8, 13, 21...
'''
def stampaFibonacciMax(valoreMassimo: int):
    i = 0
    j = 1
    while j <= valoreMassimo :
        print(j, end=" ") # Stampa il numero seguito da spazio senza andare a capo
        
        '''
        Corrisponde a:
            temp = i
            i = j
            j = temp + i
        '''
        i, j = j, i + j

    print()

'''
Esempio di utilizzo:
    stampaFibonacciMax(100)
'''

'''
   Esercizio 3:
   Creare una funzione che stampa N numeri della serie di Fibonacci 
'''
def stampaFibonacci(n):
    a = 0
    b = 1
    i = 0
    while i < n :
        print(b, end=" ")
        
        '''
        Corrisponde a:
            temp = a
            a = b
            b = temp + a
        '''
        a, b = b, a + b

        i += 1
    print()

'''
Esempio di utilizzo
    stampaFibonacci(20)
'''

def funzioneDocumentata(n: int) -> int:
    '''
        Questo è il commento che descrive la funzione, cosa fa e come lo fa.

        Parametri:
        n (int): Questo descrive il parametro e a cosa serve

        Restistituisce:
        int: Qui descrive il risultato della funzione che viene ritornato all'esterno
    '''
    return n

'''
    Se in fase di dichiarazione dei parametri indico un valore di default,
    rendo il parametro opzionale
'''
def funzioneConParametroOpzionale(a, b = 1):
    return a

def calcola_lordo(netto: float, iva: float = 0.22) -> float:
    '''
        Calcola il valore lordo di un prodotto in base all'aliquota IVA

        Parametri:
        netto (float): valore netto del prodotto
        iva (float): aliquota iva (Default: 0.22)

        Restituisce:
        float: valore lordo del prodotto
    '''
    return netto + (netto * iva)

# Valore IVA standard
print(calcola_lordo(100))
# Valore IVA differente
print(calcola_lordo(100, 0.10))

'''
    Math è la libreria che contiene funzioni matematiche,
    posso importarla e usare le funzioni al suo interno usando
    import math
    math.nomeFunzione()
'''
import math
print(math.sqrt(16))

'''
    Random è la libreria che permette di generare numeri PSEUDOcasuali
'''
import random
print(random.randint(1, 10))

'''
    Datetime è la libreria che permette di lavorare con date e orari
'''
import datetime
oggi = datetime.date.today()
print(oggi)
oggiFormattato = datetime.datetime.now().strftime("%d/%m/%Y")
print(oggiFormattato)

'''
Dalle librerie posso anche importare singole parti usando il prefisso from per
indicare la libreria e import per indicare il modulo che voglio importare
'''
from math import sqrt
sqrt(16)
