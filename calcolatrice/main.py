from calcolatrice import *
from check_input import *

ricomincia = True
while ricomincia :
    # Chiedi numeri e operatore
    numero1 = input_float("Inserisci il primo numero: ")
    operatore = input_operatore("Inserisci l'operatore: ")
    numero2 = input_float("Inserisci il secondo numero: ")

    # Risultato
    risultato = calcolatrice(numero1, numero2, operatore)
    if risultato :
        print("Risultato: ", risultato)

    continua = input("Vuoi fare un altro calcolo? (S/N)")
    if continua.lower() != "s" :
        ricomincia = False