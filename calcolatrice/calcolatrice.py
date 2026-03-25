'''
    Libreria che contiene le funzioni della calcolatrice
'''

def calcolatrice(a:float, b: float, operatore: str) -> float:
    '''
        Ritorna il risultato dell'operazione o False se l'operatore non è
        supportato
        
        a (float): primo numero
        b (float): secondo numero

        float: risultato (o False in caso di operatore non valido)
    '''
    match operatore :
        case "+":
            return somma(a, b)
        case "-":
            return differenza(a, b)
        case "/":
            return divisione(a, b)
        case "*":
            return prodotto(a, b)
        case "**" | "^":
            return potenza(a, b)
        case _:
            return False

def somma(a: float, b: float) -> float:
    '''
        Ritorna la somma tra due numeri

        a (float): primo numero
        b (float): secondo numero

        float: risultato della somma
    '''
    return a + b

def differenza(a: float, b: float) -> float:
    '''
        Ritorna la differenza tra due numeri

        a (float): primo numero
        b (float): secondo numero

        float: risultato della differenza
    '''
    return a - b

def moltiplicazione(a: float, b: float) -> float:
    '''
        Ritorna il prodotto tra due numeri

        a (float): primo numero
        b (float): secondo numero

        float: risultato del prodotto
    '''
    return a * b

def divisione(a: float, b: float) -> float:
    '''
        Ritorna la divisione tra due numeri

        a (float): primo numero
        b (float): secondo numero

        float: risultato della divisione
    '''
    if b == 0:
        raise ZeroDivisionError("Impossibile dividere per 0")
    return a / b

def potenza(a: float, b: float) -> float:
    '''
        Ritorna a alla b

        a (float): primo numero
        b (float): secondo numero

        float: risultato del calcolo a^b
    '''
    return a ** b
