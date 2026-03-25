from calcolatrice import *

ricomincia = True
while ricomincia :
    # Chiedi numeri e operatore
    numero1 = int(input("Inserisci il primo numero: "))
    operatore = input("Inserisci l'operatore: ")
    numero2 = int(input("Inserisci il secondo numero: "))

    # Risultato
    risultato = calcolatrice(numero1, numero2, operatore)
    if risultato :
        print("Risultato: ", risultato)

    continua = input("Vuoi fare un altro calcolo? (S/N)")
    if continua.lower() != "s" :
        ricomincia = False