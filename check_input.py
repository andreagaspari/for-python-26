'''
    Controlla la validità dell'input
'''

def input_int(prompt: str) -> int:
    '''
        Chiede all'utente un numero intero finché non è un intero valido

        prompt (str): il prompt della richiesta

        int: il numero intero valido
    '''
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("Numero intero non valido. Riprova.")

def input_float(prompt: str) -> float:
    '''
        Chiede all'utente un numero float finché non è un float valido

        prompt (str): il prompt della richiesta

        float: il numero float valido
    '''
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Numero float non valido. Riprova.")

def input_choice(prompt: str, valid_choices: list) -> str:
    '''
        Chiede all'utente di scegliere tra gli elementi della lista

        prompt (str): il prompt della richiesta

        str: l'elemento scelto
    '''
    while True:
        user_input = input(prompt)
        if user_input in valid_choices:
            return user_input
        else:
            print("Scegli uno dei valori validi:", valid_choices)
    