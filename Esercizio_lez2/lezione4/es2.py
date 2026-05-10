
class CSVFile:
    def __init__(self, name):
        self.name = name

    def get_data(self):
        data = []
        try:
            with open(self.name, 'r') as file:
                for line in file:
                    elements = line.strip().split(',')
                    if elements != ['']:
                        data.append(elements)
        except FileNotFoundError:
            print(f"Errore: il file '{self.name}' non è stato trovato.")
        
        return datas