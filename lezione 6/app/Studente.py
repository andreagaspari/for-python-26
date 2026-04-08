from Persona import Persona

class Studente(Persona):
    def __init__(self, nome, cognome, data_nascita, cod_fiscale, telefono, email, indirizzo, matricola):
        super().__init__(nome, cognome, data_nascita, cod_fiscale, telefono, email, indirizzo)
        self.matricola = matricola

    def __str__(self):
        return f"{self.nome} {self.cognome} ({self.matricola})"
    
    def to_csv(self):
        return (
            f"{self.nome},"
            f"{self.cognome},"
            f"{self.data_nascita},"
            f"{self.cod_fiscale},"
            f"{self.telefono},"
            f"{self.email},"
            f"{self.indirizzo.to_csv()},"
            f"{self.matricola}\n"
        )