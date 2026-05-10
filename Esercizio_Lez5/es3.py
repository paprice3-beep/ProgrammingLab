class Studente:
    def __init__(self, nome, cognome, corsi):
        self.nome = nome
        self.cognome = cognome
        self.corsi = corsi

    def saluta(self):
        print(f"Ciao, sono {self.nome} {self.cognome}.")
        print("Frequento i seguenti corsi:")
        for corso in self.corsi:
            print(f"- {corso}")

class Docente:
    def __init__(self, nome, cognome, corsi):
        self.nome = nome
        self.cognome = cognome
        self.corsi = corsi

    def saluta(self):
        print(f"Buongiorno, sono il docente {self.nome} {self.cognome}.")
        print("Insegno i seguenti corsi:")
        for corso in self.corsi:
            print(f"- {corso}")

    def insegna_tutto_a(self, studente):
        for corso in studente.corsi:
            if corso not in self.corsi:
                return False
        return True

def verifica_copertura_corsi(studenti, docenti):
    for studente in studenti:
        corsi_coperti = []
        for corso in studente.corsi:
            trovato = False
            for docente in docenti:
                if corso in docente.corsi:
                    trovato = True
                    break
            if trovato:
                corsi_coperti.append(corso)
        
        if len(corsi_coperti) != len(studente.corsi):
            return False
    return True

