class Indirizzo:
    '''
        Classe che definisce un indirizzo

        Parametri:
            via (str): Via
            civico (str): Numero civico
            cap (str): CAP
            citta (str): Città
            provincia (str): Provincia
            stato (str): Nazione (opzionale, default 'IT')
    '''
    def __init__(self, via, civico, cap, citta, provincia, stato = "IT"):
        self.via = via
        self.civico = civico
        self.cap = cap
        self.citta = citta
        self.provincia = provincia
        self.stato = stato
    
    def __str__(self):
        '''
            Stampa un'istanza della classe Indirizzo usando una stringa
            nel formato 'Via Fasulla, 123 - Rimini (RN) - IT'
        '''
        return f"{self.via}, {self.civico} - {self.cap} {self.citta} ({self.provincia}) - {self.stato}"
    
    def to_csv(self):
        return (
            f"{self.via},"
            f"{self.civico},"
            f"{self.cap},"
            f"{self.citta},"
            f"{self.provincia},"
            f"{self.stato}"
        )