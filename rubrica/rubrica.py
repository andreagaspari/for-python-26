class Contatto:
    def __init__(self, stringaCsv):
        self.nome, self.cognome, self.telefono = stringaCsv.split(",")

    def stampa(self):
        print(f"Nome e Cognome: {self.nome} {self.cognome} | Telefono: {self.telefono}")

    def stringaCsv(self):
        return f"{self.nome},{self.cognome},{self.telefono}\n"

class Rubrica:
    def __init__(self):
        self.contatti = []
        try:
            with open("rubrica.csv", "r") as file:
                next(file) # Salta intestazione
                for riga in file:
                    contatto = Contatto(riga.strip())
                    self.contatti.append(contatto)
        except FileNotFoundError:
            print("Rubrica non trovata. La rubrica sarà vuota")
    
    def aggiungiContatto(self, contatto):
        self.contatti.append(contatto)

    def stampaContatti(self):
        for contatto in self.contatti:
            contatto.stampa()

    def salva(self):
        with open("rubrica.csv", "w") as file:
            file.write("nome,cognome,telefono\n")
            for contatto in self.contatti:
                file.write(contatto.stringaCsv())