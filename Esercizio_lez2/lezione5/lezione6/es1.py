class CSVFile:
    def __init__(self, name):
        self.name = name
        try:
            with open(self.name, 'r') as file:
                file.readline()
        except FileNotFoundError:
            print(f"Errore: il file '{self.name}' non esiste.")

    def get_data(self):
        try:
            data = []
            with open(self.name, 'r') as file:
                for line in file:
                    elements = line.strip().split(',')
                    if elements[0] != 'Date':
                        data.append(elements)
            return data
        except FileNotFoundError:
            return []
