class Persona:
    '''
        Classe Persona: memorizza anagrafica di una persona

        Parametri:
            nome (str): Nome
            cognome (str): Cognome
            data_nascita (str): Data di Nascita
            cod_fiscale (str): Codice Fiscale
            telefono (str): Numero di Telefono
            email (str): Indirizzo E-mail
            indirizzo (Indirizzo): Indirizzo di residenza
    '''
    def __init__(self, nome, cognome, data_nascita, cod_fiscale, telefono, email, indirizzo):
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.cod_fiscale = cod_fiscale
        self.telefono = telefono
        self.email = email
        self.indirizzo = indirizzo

    def __str__(self):
        '''
            Ritorna la stringa della persona: Nome Cognome
        '''
        return f"{self.nome} {self.cognome}"
    