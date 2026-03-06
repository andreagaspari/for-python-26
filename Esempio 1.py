'''
Questo è un commento, il programma:
ignorerà tutto il contenuto fino alla chiusura
del commento.
'''
print("Il mio nome è \"Andrea\"") #Anche questo è un commento, ma termina quando vado a capo
print('L\'albero è in fiore\\in frutto')
'''
    Il carattere di Escape "\" 
    indica un carattere speciale a seguire 
    (", ', t per tab, n per newline)
'''
print('Il mio nome è \t Andrea')


''' 
	Per chiedere all'utente di inserire un dato possiamo usare input()
'''
input("Inserisci il tuo nome: ")

''' 
    Salvo il nome inserito dall'utente in
    una variabile, poi lo stampo nella riga
    successiva. Per separare il nome dal testo
    possiamo usare la virgola (aggiunge spazio in mezzo)
    o il + (attacca i due elementi uno all'altro)
'''
nome = input("Inserisci il tuo nome: ")
print("Ciao", nome + ", bentornato!")
'''
    Possiamo usare anche la stringa formattata 
    (f-string), in cui possiamo inserire le 
    variabili chiuse tra parentesi graffe
'''
print(f"Ciao {nome}, bentornato!")

''' 
	In Python esistono due tipi di numeri: 
	interi e decimali, la conversione da 
	intero a decimale avviene in automatico, se necessario
''''
print(10) #Numero intero (int)
print(3.13) #Numero decimale (float)
print(10 / 3) #La divisione tra numeri interi può ritornare un numero decimale

'''
    Operatori aritmetici:
     +  somma
     -  sottrazione
     *  moltiplicazione
     /  divisione
     ** potenza
     %  resto della divisione
'''
print(2 + 3) # 5
print(2 * 3) # 6
print(8 - 5) # 3
print(5 - 8) # -3
print(24 / 5) # 4.8
print(2 ** 3) # 8
print(23 % 5) # 3 {(5 x 4 ) + 3 = 23}

''' 
	Esercizio:
		Chiedi all'utente Nome ed Età,
		Stampa la frase:
			Ciao Nome, tra 10 anni avrai N anni.
'''
nome = input("Inserisci il tuo nome: ")
eta = int(input("Inserisci la tua età: "))
print("Ciao", nome + ", tra 10 anni avrai", eta + 10, "anni.")
print(f"Ciao {nome}, tra 10 anni avrai {eta + 10} anni.")
