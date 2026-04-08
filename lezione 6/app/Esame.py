class Esame:
    def __init__(self, materia, studente):
        self.materia = materia
        self.studente = studente
    
    def sostieni_esame(self, voto):
        self.voto = voto

    def __str__(self):
        if (self.voto) :
            return f"{self.studente} ha sostenuto l'esame in {self.materia} con voto {self.voto}"
        else :
            return f"{self.studente} non ha ancora sostenuto l'esame in {self.materia}"