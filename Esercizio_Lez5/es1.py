class Studente:
    def __init__(self, nome, cognome, corsi):
        self.nome = nome
        self.cognome = cognome
        self.corsi = corsi  # Memorizza la lista dei corsi

    def saluta(self):
        print(f"Ciao, sono {self.nome} {self.cognome}.")
        print("Frequento i seguenti corsi:")
        for corso in self.corsi:
            print(f"- {corso}")

class Docente:
    def __init__(self, nome, cognome, corsi):
        self.nome = nome
        self.cognome = cognome
        self.corsi = corsi  # Memorizza la lista dei corsi insegnati

    def saluta(self):
        print(f"Buongiorno, sono il docente {self.nome} {self.cognome}.")
        print("Insegno i seguenti corsi:")
        for corso in self.corsi:
            print(f"- {corso}")