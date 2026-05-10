class CSVFile:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Errore: il nome del file deve essere una stringa")
        
        self.name = name
        
        try:
            with open(self.name, 'r') as file:
                file.readline()
        except FileNotFoundError:
            print(f"Errore: il file '{self.name}' non esiste.")

    def get_data(self, start=None, end=None):
        try:
            with open(self.name, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            return []

        if not lines:
            return []

        try:
            total_lines = len(lines)
            
            if start is None:
                start = 1
            else:
                start = int(start)
            
            if end is None:
                end = total_lines
            else:
                end = int(end)

            if start < 1: start = 1
            if end > total_lines: end = total_lines
            
            if start > end:
                return []

            data = []
            selected_lines = lines[start-1 : end]

            for line in selected_lines:
                elements = line.strip().split(',')
                if elements:
                    data.append(elements)
            
            return data

        except (ValueError, TypeError):
            return []