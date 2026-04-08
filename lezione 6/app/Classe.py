import csv
from Studente import Studente
from Indirizzo import Indirizzo

class Classe:
    def __init__(self, anno, sezione):
        self.anno = anno
        self.sezione = sezione
        self.studenti = []
        self.esami = []

        self.carica()

    def __str__(self):
        return f"La classe {self.anno}{self.sezione} ha {len(self.studenti)} studenti"
    
    def aggiungi_studente(self, studente):
        self.studenti.append(studente)

    def aggiungi_esame(self, esame):
        self.esami.append(esame)

    def stampa_lista_studenti(self):
        for studente in self.studenti:
            print(studente)

    def salva(self):
        nome_file = f"registro_{self.anno}{self.sezione}.csv"

        with open(nome_file, "w") as file:
            file.write("nome,cognome,data_nascita,cod_fiscale,telefono,email,via,numero,cap,citta,provincia,stato,matricola\n")

            for studente in self.studenti:
                file.write(studente.to_csv())

    def carica(self):
        nome_file = f"registro_{self.anno}{self.sezione}.csv"

        with open(nome_file, "r") as file:
            reader = csv.reader(file)

            next(reader) # salta intestazione

            for riga in reader:
                studente = Studente(
                    riga[0],
                    riga[1],
                    riga[2],
                    riga[3],
                    riga[4],
                    riga[5],
                    Indirizzo(
                        riga[6],
                        riga[7],
                        riga[8],
                        riga[9],
                        riga[10],
                        riga[11]
                    ),
                    riga[12]
                )
                self.aggiungi_studente(studente)

        print(f"Caricati {len(self.studenti)} studenti")